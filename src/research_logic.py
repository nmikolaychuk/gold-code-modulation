from signal_generator import SignalGenerator
from defaults import *
from enums import *


def calc_research(average_count: int, from_noise: int = 20, to_noise: int = -11, step_noise: int = -1):
    # Объект для генерации сигналов
    signals_generator = SignalGenerator()
    # Изменение уровня шума
    x, y = [], []
    for snr in range(from_noise, to_noise, step_noise):
        print(f"Запускается расчет исследования при {snr} дБ...")
        # Обновление уровня шума
        signals_generator.snr = float(snr)
        # Цикл для усреднений
        for avg in range(average_count):
            ...