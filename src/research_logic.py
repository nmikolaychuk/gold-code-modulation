from signal_generator import SignalGenerator


def calc_research(average_count: int, from_noise: int = 20, to_noise: int = -21, step_noise: int = -1):
    # Объект для генерации сигналов
    signal_generator = SignalGenerator()

    # Рассчет фильтров
    signal_generator.filters.clear()
    for k, v in signal_generator.gold_codes.items():
        # Получение IQ компонент
        i, q = signal_generator.get_qpsk_components(v)
        # Получение комплексной огибающей
        signal_generator.filters[k] = signal_generator.get_complex_array(i, q)

    # Буферы с результатами
    x, y = [], []

    # Изменение уровня шума
    for snr in range(from_noise, to_noise, step_noise):
        print(f"Запускается расчет исследования при {snr} дБ...")
        # Обновление уровня шума
        signal_generator.snr = float(snr)
        probability = 0
        # Цикл для усреднений
        for avg in range(average_count):
            # Получение исходных битов
            bits = signal_generator.generate_bits(signal_generator.bits_count)
            signal_generator.input_bits = bits
            # Замена исходных битов кодами Голда
            gold_bits = signal_generator.get_gold_bits(bits)
            signal_generator.gold_bits = gold_bits
            # Получение IQ компонент
            i_comp, q_comp = signal_generator.get_qpsk_components(signal_generator.gold_bits)
            # Наложение шума на полученные последовательности бит
            _, i_comp_noise = signal_generator.generate_noise([[], i_comp])
            _, q_comp_noise = signal_generator.generate_noise([[], q_comp])
            # Отрисовка битов
            signal_generator.i_component = i_comp_noise
            signal_generator.q_component = q_comp_noise
            # Получить комплексную огибающую исходной последовательности
            z = signal_generator.get_complex_array(i_comp_noise, q_comp_noise)
            # Свёртка QPSK сигнала с импульсными характеристиками согласованных фильтров
            responses = signal_generator.calc_convolution(z)
            signal_generator.response_signal = responses
            # Анализ максимумов откликов
            restored_bits = signal_generator.restore_input_bits(responses)
            signal_generator.restored_bits = restored_bits
            # Сравнение последовательностей
            bad_restored_count = 0
            for i in range(len(bits)):
                if bits[i] != restored_bits[i]:
                    bad_restored_count += 1
            # Вычисление вероятности ошибки
            probability += bad_restored_count / signal_generator.bits_count
        # Формирование массивов для отрисовки
        x.append(snr)
        y.append(probability / average_count)

    return x, y
