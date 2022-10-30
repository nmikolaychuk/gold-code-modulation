import random
import numpy as np
from collections import deque

from defaults import *
from enums import *


class SignalGenerator:
    """
    Объект для генерации опорного сигнала
    """
    def __init__(self, s_r=DEFAULT_SAMPLING_RATE, b_count=DEFAULT_BITS_COUNT,
                 bps=DEFAULT_BITS_PER_SECOND, snr=DEFAULT_SNR):

        # Параметры сигнала
        self.sampling_rate = float(s_r)
        self.bits_count = int(b_count)
        self.bits_per_second = float(bps)
        self.snr = float(snr)
        self.signal_freq = 20000

        # Буферы для хранения сигналов
        self.input_bits = []
        self.gold_bits = []
        self.i_component = []
        self.q_component = []
        self.qpsk_signal = []
        self.response_signal = []
        self.restored_bits = []

        # Закрепление кодов Голда за входными символами
        self.m_seq1 = self.get_m_sequence(ShiftRegisterType.FIVE_THREE)
        self.m_seq2 = self.get_m_sequence(ShiftRegisterType.FIVE_FOUR_THREE_TWO)
        self.gold_codes = {}
        self.filters = {}
        self.get_gold_codes_for_inputs()

    @staticmethod
    def generate_bits(bits_count):
        """
        Формирование случайной битовой информационной последовательности.
        """
        bits = []
        for i in range(int(bits_count)):
            x = random.randint(0, 1)
            bits.append(x)

        return bits

    def _get_signal_parameters(self, sf: float, bits_count: int):
        """
        Рассчитать параметры сигналов.
        """
        # Длительность одного бита
        bit_time = 1. / self.bits_per_second
        # Длительность сигнала
        signal_duration = bit_time * bits_count
        # Частота опорного сигнала
        w = 2. * np.pi * sf
        # Количество отсчётов сигнала
        n = self.sampling_rate * signal_duration
        # Шаг времени
        timestep = signal_duration / n
        return signal_duration, timestep, bit_time, w

    @staticmethod
    def get_m_sequence(shift_type: ShiftRegisterType):
        """
        Сгенерировать м-последовательность с заданным регистром сдвига.

        :param shift_type: Тип регистра сдвига ([5,3] или [5,4,3,2]).
        :return: М-последовательности длиной 31 бит.
        """
        # Начальное состояние регистра
        shift_condition = [1, 1, 1, 1, 1]

        # Конфигурация регистра
        shift_config = []
        if shift_type == ShiftRegisterType.FIVE_THREE:
            # Конфигурация [5,3]
            shift_config = [4, 2]
        elif shift_type == ShiftRegisterType.FIVE_FOUR_THREE_TWO:
            # Конфигурация [5,4,3,2]
            shift_config = [4, 3, 2, 1]

        output = []
        while len(output) != LEN_SEQUENCE:
            # 1. Получение выхода
            output.append(shift_condition[-1])
            # 2. Суммирование
            drains = []
            for idx in shift_config:
                drains.append(shift_condition[idx])
            mod_sum = sum(drains) % 2
            # 3. Сдвиг
            shift_condition = [mod_sum] + shift_condition[:-1]
        return output

    @staticmethod
    def get_shifted_m_sequence(m_sequence: list, shift_value: int):
        """
        Получить циклически сдвинутую M-последовательность.

        :param m_sequence: М-последовательность.
        :param shift_value: Величина сдвига.
        :return: Сдвинутая М-последовательность.
        """
        deque_m_seq = deque(m_sequence)
        deque_m_seq.rotate(LEN_SEQUENCE - shift_value % LEN_SEQUENCE)
        return list(deque_m_seq)

    @staticmethod
    def calc_sum_m_sequence(m_seq1: list, m_seq2: list):
        """
        Поэлементная сумма М-последовательностей по модулю 2.

        :param m_seq1: М-последовательность.
        :param m_seq2: М-последовательность.
        :return: Результат суммирования.
        """
        output = []
        for i in range(LEN_SEQUENCE):
            output.append((m_seq1[i] + m_seq2[i]) % 2)
        return output

    def get_gold_codes_for_inputs(self):
        """
        Закрепить коды Голда за каждым возможным входным символом.

        :return: None.
        """
        m_seq2 = self.get_shifted_m_sequence(self.m_seq2, 0)
        self.gold_codes["00"] = self.calc_sum_m_sequence(self.m_seq1, m_seq2)
        m_seq2 = self.get_shifted_m_sequence(self.m_seq2, 1)
        self.gold_codes["01"] = self.calc_sum_m_sequence(self.m_seq1, m_seq2)
        m_seq2 = self.get_shifted_m_sequence(self.m_seq2, 2)
        self.gold_codes["10"] = self.calc_sum_m_sequence(self.m_seq1, m_seq2)
        m_seq2 = self.get_shifted_m_sequence(self.m_seq2, 3)
        self.gold_codes["11"] = self.calc_sum_m_sequence(self.m_seq1, m_seq2)

    def get_gold_bits(self):
        """
        Замена исходных битов на соответствующие коды Голда.

        :return: None.
        """
        add_to_end = None
        output_bits = []
        bits = self.input_bits.copy()
        if len(bits) % 2 == 1:
            add_to_end = bits[-1]
            del bits[-1]

        for i in range(0, len(bits), 2):
            symbol = str(self.input_bits[i]) + str(self.input_bits[i+1])
            for item in self.gold_codes[symbol]:
                output_bits.append(item)

        if add_to_end is not None:
            output_bits.append(add_to_end)
        return output_bits

    @staticmethod
    def get_qpsk_components(bits: list):
        """
        Получить I и Q компоненты.

        :return: I и Q компоненты.
        """
        i_component = []
        q_component = []

        if not bits:
            return None, None

        for i in range(len(bits)):
            if i % 2 == 0:
                i_component.append(bits[i])
            else:
                q_component.append(bits[i])
        return i_component, q_component

    def calc_modulated_signal(self, i_c: list, q_c: list):
        """
        Построить ФМ4 манипулированный сигнал.
        """
        x, y = [], []
        bits_count = len(i_c) + len(q_c)
        signal_duration, timestep, bit_time, w = self._get_signal_parameters(self.signal_freq, bits_count)
        iq_step = signal_duration / (bits_count / 2.)
        for t in np.arange(0, signal_duration, timestep):
            iq_index = int(t / iq_step)

            try:
                i_buf = -1 if i_c[iq_index] == 0 else 1
            except IndexError:
                i_buf = 0

            try:
                q_buf = -1 if q_c[iq_index] == 0 else 1
            except IndexError:
                q_buf = 0

            x.append(t)
            y.append(i_buf * np.cos(w * t) - q_buf * np.sin(w * t))
        return x, y

    def calc_convolution(self, qpsk: list):
        """
        Получить свёртку QPSK сигнала с импульсными характеристиками согласованных фильтров.

        :param qpsk: ФМ4 модулированный сигнал.
        :return: Отклики.
        """
        if not self.filters:
            return

        outputs = []
        big_signal_length = len(qpsk[1])
        research = np.array(qpsk[1])
        for k, v in self.filters.items():
            x, y = [], []
            small_signal_length = len(v[1])
            modulate = np.array(v[1])
            for i in np.arange(0, big_signal_length - small_signal_length - 1):
                summary = np.sum(np.multiply(modulate, research[i:small_signal_length+i])) / small_signal_length
                x.append(qpsk[0][i])
                y.append(summary)
            outputs.append([x, y])

        return outputs

    def restore_input_bits(self, responses: list):
        """
        Восстановить исходную информацию по откликам согласованных фильтров.

        :return: Биты.
        """
        positions = {}
        symbols = list(self.gold_codes.keys())
        for i, resp in enumerate(responses):
            avg_value = max(resp[1]) - sum(resp[1]) / len(resp[1])
            print(avg_value)
            pos = [resp[0][i] for i, v in enumerate(resp[1]) if v >= avg_value]
            print(len(pos))
            positions[symbols[i]] = pos


    @staticmethod
    def _calc_signal_energy(signal: list):
        """
        Расчет энергии сигнала
        """
        energy = 0.
        for i in range(len(signal[1])):
            energy += signal[1][i] ** 2
        return energy

    @staticmethod
    def _get_random_value():
        """
        Рандомизация чисел для шума
        """
        av = 20
        value = 0.
        for i in range(av):
            value += random.uniform(-1, 1)
        return value / av

    def generate_noise(self, signal: list):
        """
        Генерация шума для сигнала
        """
        snr = self.snr
        if not signal:
            return

        # Расчет энергии шума
        signal_energy = self._calc_signal_energy(signal)
        noise_energy = signal_energy / (10 ** (snr / 10))

        # Случайная шумовая добавка к каждому отсчету
        noise = []
        random_energy = 0.
        for i in range(len(signal[1])):
            random_value = self._get_random_value()
            noise.append(random_value)
            random_energy += random_value ** 2

        # Зашумленный сигнал
        alpha = np.sqrt(noise_energy / random_energy)
        noise_signal = []
        for i in range(len(signal[1])):
            noise_signal.append(signal[1][i] + alpha * noise[i])

        return signal[0], noise_signal

    @staticmethod
    def get_bits_to_plot(bits: list):
        """
        Получение информационных бит для отображения.
        """
        if not bits:
            return

        bits_count = len(bits)

        x = []
        y = []
        for i in range(bits_count):
            x.append(i)
            y.append(bits[i])
            if i < bits_count - 1:
                if bits[i] != bits[i + 1]:
                    x.append(i + 1)
                    y.append(bits[i])
            else:
                x.append(i + 1)
                y.append(bits[i])

        return x, y
