import random
import numpy as np

from defaults import *


class SignalGenerator:
    """
    Объект для генерации опорного сигнала
    """
    def __init__(self,
                 s_r=DEFAULT_SAMPLING_RATE, s_freq=DEFAULT_SIGNAL_FREQ,
                 b_count=DEFAULT_BITS_COUNT, bps=DEFAULT_BITS_PER_SECOND,
                 t_delay=DEFAULT_TIME_DELAY, snr=DEFAULT_SNR):

        # Параметры сигнала
        self.sampling_rate = float(s_r)
        self.signal_freq = float(s_freq)
        self.bits_count = int(b_count)
        self.bits_per_second = float(bps)
        self.time_delay = float(t_delay)
        self.snr = float(snr)
        self.signal_phase = 0.

        # Буферы для хранения сигналов
        self.input_bits = []
        self.gold_bits = []
        self.i_component = []
        self.q_component = []
        self.response_signal = []
        self.restored_bits = []

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

    def calc_modulated_signal(self):
        """
        Построить ФМ4 манипулированный сигнал.
        """
        # TODO

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
        av = 12
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
        d = 1. / (10 ** (snr / 10))

        # Случайная шумовая добавка к каждому отсчету
        noise = []
        random_energy = 0.
        for i in range(len(signal[1])):
            random_value = self._get_random_value()
            noise.append(random_value)
            random_energy += random_value ** 2

        # Зашумленный сигнал
        alpha = np.sqrt(d * signal_energy / random_energy)
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
