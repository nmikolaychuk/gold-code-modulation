import random
import numpy as np
from collections import deque
from statsmodels.api import tsa


from defaults import *
from enums import *


class SignalGenerator:
    """
    Объект для генерации опорного сигнала
    """
    def __init__(self, b_count=DEFAULT_BITS_COUNT, snr=DEFAULT_SNR):

        # Параметры сигнала
        self.bits_count = int(b_count)
        self.snr = float(snr)

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

    def get_gold_bits(self, bits: list):
        """
        Замена битов на соответствующие коды Голда.

        :return: None.
        """
        output_bits = []
        for i in range(0, len(bits), 2):
            symbol = str(bits[i]) + str(bits[i+1])
            for item in self.gold_codes[symbol]:
                output_bits.append(item)
        return output_bits

    @staticmethod
    def get_qpsk_components(bits: list):
        """
        Получить I и Q компоненты.

        :return: I и Q компоненты.
        """
        if len(bits) % 2 != 0:
            bits.append(0)

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

    def calc_convolution(self, z: list):
        """
        Получить свёртку QPSK сигнала с импульсными характеристиками согласованных фильтров.

        :param z: Комплексная огибающая сигнала.
        :return: Отклики.
        """
        if not self.filters:
            return

        output = []
        research = np.array(z)
        research = research - research.mean(keepdims=True)
        for k, v in self.filters.items():
            modulate = np.array(v)
            modulate = modulate - modulate.mean(keepdims=True)

            y = np.abs(np.correlate(research, modulate, 'same'))
            x = [i for i in range(len(y))]

            output.append([x, y])
        return output

    @staticmethod
    def get_complex_array(i_comp: list, q_comp: list):
        """
        Получить комплексную огибающую сигнала по квадратурным компонентам.

        :param i_comp: Синфазная компонента.
        :param q_comp: Квадратурная компонента.
        :return: Комплексный список.
        """
        output = []
        for i in range(len(i_comp)):
            output.append(complex(i_comp[i], q_comp[i]))

        return output

    def restore_input_bits(self, responses: list):
        """
        Восстановить исходную информацию по откликам согласованных фильтров.

        :return: Биты.
        """
        # Количество переданных символов
        bits_count = int(self.bits_count / 2)
        # Количество отсчетов после корреляции
        length = len(responses[0][1])
        # Интервал, в котором обязательно находится пик
        interval_for_max = int(length / bits_count)
        # Возможные символы в сообщении
        symbols = list(self.gold_codes.keys())

        # Анализ каждого интервала
        output = []
        for i in range(0, length, interval_for_max):
            begin = i
            end = i + interval_for_max
            # Нахождение максимума среди всех откликов
            resp_index = None
            max_value = 0
            for j, resp in enumerate(responses):
                current_max = np.max(resp[1][begin:end])
                if current_max > max_value:
                    max_value = current_max
                    resp_index = j
            # Добавление наиболее вероятного символа в результат
            output.append(symbols[resp_index])

        # Постобработка восстановленной последовательности
        result = []
        for item in output:
            for i in item:
                result.append(int(i))

        return result

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

    @staticmethod
    def calc_acf(x1: list, x2: list):
        """
        Вычислить взаимную корреляционную функцию.
        """
        acf_y = tsa.stattools.ccf(x1, x2, adjusted=False)
        acf_x = [i for i in range(len(acf_y))]
        return [acf_x, acf_y]
