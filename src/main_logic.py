from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
from PyQt5 import QtWidgets, QtCore, QtGui

from main_interface import Ui_MainWindow
from mpl_widget import MplGraphicsModulated, MplGraphicsResearch
from signal_generator import SignalGenerator
from defaults import *
from enums import *


class MainApp(QtWidgets.QMainWindow, Ui_MainWindow):
    """
    Реализация графического интерфейса основного приложения
    """
    def __init__(self, screen: QtCore.QRect):
        QtWidgets.QMainWindow.__init__(self)
        self.setupUi(self)

        # Конфигурация окна приложения
        # Скрытие системных кнопок
        self.setWindowFlag(QtCore.Qt.WindowType.FramelessWindowHint)

        # Тени
        self.shadow = QtWidgets.QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(50)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QtGui.QColor(0, 92, 157, 550))
        self.centralwidget.setGraphicsEffect(self.shadow)

        # Добавление области масштабирования в правый нижний угол
        QtWidgets.QSizeGrip(self.resize_frame)

        # Перетаскивание окна
        self.header_container.mouseMoveEvent = self.move_window
        self.click_position = None

        # Боковое меню
        self.animation_menu = QtCore.QPropertyAnimation(self.side_menu_container, b"maximumWidth")
        self.animation_geometry = QtCore.QPropertyAnimation(self, b"geometry")

        # Логика
        # Обработчики кнопок
        self.minimized_button.clicked.connect(lambda: self.showMinimized())
        self.close_button.clicked.connect(lambda: self.close())
        self.open_main_page_button.clicked.connect(lambda: self.stacked_widget.setCurrentWidget(self.main_page))
        self.open_parameters_page_button.clicked.connect(lambda: self.stacked_widget.setCurrentWidget(self.parameters_page))
        self.open_research_page_button.clicked.connect(lambda: self.stacked_widget.setCurrentWidget(self.research_page))
        self.maximized_button.clicked.connect(self.restore_or_maximized)
        self.side_menu_button.clicked.connect(self.slide_left_menu)
        self.draw_button.clicked.connect(self.draw_main_page_graphics)
        self.calc_filters.clicked.connect(self.calc_filters_logic)
        self.start_calc_button.clicked.connect(lambda: self.open_main_page_button.click())
        self.start_research_button.clicked.connect(self.start_research_logic)

        # Инициализация значений по умолчанию
        self.stacked_widget.setCurrentWidget(self.parameters_page)
        self.full_screen_geometry = screen
        self.last_geometry = None
        self.sampling_rate_edit.setText(DEFAULT_SAMPLING_RATE)
        self.snr_edit.setText(DEFAULT_SNR)
        self.bits_count_edit.setText(DEFAULT_BITS_COUNT)
        self.bits_per_second_edit.setText(DEFAULT_BITS_PER_SECOND)
        self.average_count_edit.setText(DEFAULT_AVERAGE_COUNT)
        self.signal_generator = SignalGenerator()

        # Обработка событий редактирования параметров
        self.sampling_rate_edit.textChanged.connect(self.sr_change_logic)
        self.bits_count_edit.textChanged.connect(self.bits_count_change_logic)
        self.bits_per_second_edit.textChanged.connect(self.bits_per_second_change_logic)
        self.snr_edit.textChanged.connect(self.snr_change_logic)

        # Инициализация основных графиков
        self.graphics = MplGraphicsModulated()
        self.toolbar = NavigationToolbar(self.graphics, self.graphics, coordinates=True)
        self.verticalLayout_16.addWidget(self.toolbar)
        self.verticalLayout_16.addWidget(self.graphics)

        # Инициализация графика исследования
        self.research_graphics = MplGraphicsResearch()
        self.research_toolbar = NavigationToolbar(self.research_graphics, self.research_graphics, coordinates=True)
        self.verticalLayout_10.addWidget(self.research_toolbar)
        self.verticalLayout_10.addWidget(self.research_graphics)

    def draw(self, graph_type: GraphType, x: list, y: list):
        """
        Нарисовать график.
        """
        if graph_type == GraphType.INPUT_BITS:
            self.graphics.clear_plot_ax1()
            self.graphics.plot_graph_ax1(x, y)
        elif graph_type == GraphType.I_COMP:
            self.graphics.clear_plot_ax2()
            self.graphics.plot_graph_ax2(x, y)
        elif graph_type == GraphType.Q_COMP:
            self.graphics.clear_plot_ax3()
            self.graphics.plot_graph_ax3(x, y)
        elif graph_type == GraphType.RESTORED:
            self.graphics.clear_plot_ax5()
            self.graphics.plot_graph_ax5(x, y)

        self.graphics.draw()
        self.graphics.flush_events()

    def draw_responses(self, x1: list, y1: list, x2: list, y2: list,
                       x3: list, y3: list, x4: list, y4: list):
        """
        Отобразить отклики согласованных фильтров.
        """
        self.graphics.clear_plot_ax4()
        self.graphics.plot_graph_ax4(x1, y1, x2, y2, x3, y3, x4, y4)
        self.graphics.draw()
        self.graphics.flush_events()

    def draw_ber_of_snr(self, x: list, y: list):
        """
        Отобразить график исследования.
        """
        self.research_graphics.clear_plot()
        self.research_graphics.plot_graph(x, y)
        self.research_graphics.draw()
        self.research_graphics.flush_events()

    def draw_main_page_graphics(self):
        """
        Отрисовка графиков на главной странице.
        """
        # Получение исходных битов
        bits = self.signal_generator.generate_bits(self.signal_generator.bits_count)
        self.signal_generator.input_bits = bits
        in_b_x, in_b_y = self.signal_generator.get_bits_to_plot(bits)
        self.draw(GraphType.INPUT_BITS, in_b_x, in_b_y)

        # Заменить на коды Голда
        if self.signal_generator.bits_count % 2 != 0:
            print("Указано некорректное количество информационных бит")
            return

        gold_bits = self.signal_generator.get_gold_bits(bits)
        self.signal_generator.gold_bits = gold_bits

        # Получение IQ компонент
        i_comp, q_comp = self.signal_generator.get_qpsk_components(self.signal_generator.gold_bits)

        # Наложить шум на полученные последовательности бит
        _, i_comp_noise = self.signal_generator.generate_noise([[], i_comp])
        _, q_comp_noise = self.signal_generator.generate_noise([[], q_comp])

        # Отрисовка битов
        self.signal_generator.i_component = i_comp_noise
        self.signal_generator.q_component = q_comp_noise
        i_plot = self.signal_generator.get_bits_to_plot(i_comp)
        q_plot = self.signal_generator.get_bits_to_plot(q_comp)
        self.draw(GraphType.I_COMP, i_plot[0], i_plot[1])
        self.draw(GraphType.Q_COMP, q_plot[0], q_plot[1])

        # Получить комплексную огибающую исходной последовательности
        z = self.signal_generator.get_complex_array(i_comp_noise, q_comp_noise)

        # Свёртка QPSK сигнала с импульсными характеристиками согласованных фильтров
        if self.signal_generator.filters:
            responses = self.signal_generator.calc_convolution(z)
            self.signal_generator.response_signal = responses
            self.draw_responses(responses[0][0], responses[0][1],
                                responses[1][0], responses[1][1],
                                responses[2][0], responses[2][1],
                                responses[3][0], responses[3][1])

            # Анализ максимумов откликов
            resotred_bits = self.signal_generator.restore_input_bits(responses)
            self.signal_generator.restored_bits = resotred_bits
            restored_plot = self.signal_generator.get_bits_to_plot(resotred_bits)
            self.draw(GraphType.RESTORED, restored_plot[0], restored_plot[1])
            print(bits)
            print(resotred_bits)

    def calc_filters_logic(self):
        """
        Рассчитать согласованные фильтры.
        """
        # 1. ФМ4 модуляция каждого кода Голда
        self.signal_generator.filters.clear()
        for k, v in self.signal_generator.gold_codes.items():
            # Получение IQ компонент
            i, q = self.signal_generator.get_qpsk_components(v)
            # Получение комплексной огибающей
            z = self.signal_generator.get_complex_array(i, q)
            # Зеркалирование QPSK
            self.signal_generator.filters[k] = z
        print("Импульсные характеристики согласованных фильтров успешно рассчитаны!")

    def start_research_logic(self):
        """
        Обработчик запуска исследования.
        """
        # Запуск исследования
        try:
            average_count = int(self.average_count_edit.text())
        except ValueError:
            return

        print("calc_research")

    def sr_change_logic(self):
        """
        Обработка события изменения значения в поле "Частота дискретизации".
        """
        if self.sampling_rate_edit.text().isdigit():
            self.signal_generator.sampling_rate = float(self.sampling_rate_edit.text())

    def bits_count_change_logic(self):
        """
        Обработка события изменения значения в поле "Количество информационных бит".
        """
        new_value = self.bits_count_edit.text()
        if new_value.isdigit() and int(new_value) % 2 == 0:
            self.signal_generator.bits_count = float(self.bits_count_edit.text())

    def bits_per_second_change_logic(self):
        """
        Обработка события изменения значения в поле "Скорость передачи данных".
        """
        if self.bits_per_second_edit.text().isdigit():
            self.signal_generator.bits_per_second = float(self.bits_per_second_edit.text())

    def snr_change_logic(self):
        """
        Обработка события изменения значения в поле "ОСШ".
        """
        try:
            self.signal_generator.snr = float(self.snr_edit.text())
        except ValueError:
            pass

    def restore_or_maximized(self):
        """
        Логика сворачивания и разворачивания окна.
        """
        current_geometry = self.geometry()
        if current_geometry.width() == self.full_screen_geometry.width() and \
                current_geometry.height() == self.full_screen_geometry.height():
            new_geometry = self.last_geometry
        else:
            new_geometry = self.full_screen_geometry
            self.last_geometry = current_geometry

        self.animation_geometry.setDuration(DURATION_MAXIMIZED)
        self.animation_geometry.setStartValue(current_geometry)
        self.animation_geometry.setEndValue(new_geometry)
        self.animation_geometry.setEasingCurve(QtCore.QEasingCurve.Type.InOutQuart)
        self.animation_geometry.start()

    def mousePressEvent(self, event):
        """
        Получение координат курсора при клике.
        """
        self.click_position = event.globalPos()

    def move_window(self, e):
        """
        Логика перетаскивания окна приложения.
        """
        if not self.isMaximized():
            if e.buttons() == QtCore.Qt.MouseButton.LeftButton:
                self.move(self.pos() + e.globalPos() - self.click_position)
                self.click_position = e.globalPos()
                e.accept()

    def slide_left_menu(self):
        """
        Логика работы бокового меню.
        """
        width = self.side_menu_container.width()
        if width == MIN_WIDTH:
            new_width = MAX_WIDTH
            self.side_menu_button.setIcon(QtGui.QIcon(HIDE_MENU_ICON))
        else:
            new_width = MIN_WIDTH
            self.side_menu_button.setIcon(QtGui.QIcon(OPEN_MENU_ICON))

        self.animation_menu.setDuration(DURATION_SIDE_MENU)
        self.animation_menu.setStartValue(width)
        self.animation_menu.setEndValue(new_width)
        self.animation_menu.setEasingCurve(QtCore.QEasingCurve.Type.InOutQuad)
        self.animation_menu.start()
