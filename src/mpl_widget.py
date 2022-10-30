from PyQt5 import QtWidgets
import numpy as np
import matplotlib.pyplot as plt
plt.rcParams.update({'font.size': 7})

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure


class MplGraphicsResearch(FigureCanvas):
    """
    Функция отрисовки
    """
    def __init__(self, dpi=100):
        self.fig = Figure(dpi=dpi, facecolor=(.94, .94, .94, 0.), figsize=(4, 3))

        # Добавление области графа
        self.ax = self.fig.add_subplot(111)
        self.add_text()

        # Инициализация
        FigureCanvas.__init__(self, self.fig)
        FigureCanvas.setSizePolicy(self, QtWidgets.QSizePolicy.Policy.Expanding,
                                   QtWidgets.QSizePolicy.Policy.Expanding)
        FigureCanvas.updateGeometry(self)

    def add_text(self):
        """
        Инициализация графика.
        """
        # Инициализация области графика модулированного сигнала
        self.ax.set_title("График зависимости вероятности ошибки от SNR")
        self.ax.grid(linestyle="dotted", alpha=0.65)

    def plot_graph(self, x: list, y: list):
        """
        Построение графика функции модулированного сигнала.
        """
        self.ax.plot(x, y, linestyle="-", markersize=2, color='g', label="Исходный информационный сигнал")
        self.ax.legend(loc="upper right", framealpha=1.0)
        self.ax.margins(y=0.8)

    def clear_plot(self):
        """
        Очистка области графика.
        """
        self.ax.clear()
        self.add_text()


class MplGraphicsModulated(FigureCanvas):
    """
    Функция отрисовки
    """
    def __init__(self, dpi=100):
        self.fig = Figure(dpi=dpi, facecolor=(.94, .94, .94, 0.), figsize=(5, 3))

        self.fig.set_constrained_layout(True)
        axd = self.fig.subplot_mosaic(
            """
            AAAA
            BBBB
            IIQQ
            CCCC
            DDDD
            EEEE
            """)

        self.ax1 = axd['A']
        self.ax2 = axd['B']
        self.ax3 = axd['I']
        self.ax4 = axd['Q']
        self.ax5 = axd['C']
        self.ax6 = axd['D']
        self.ax7 = axd['E']
        self.add_text()

        # Инициализация
        FigureCanvas.__init__(self, self.fig)
        FigureCanvas.setSizePolicy(self, QtWidgets.QSizePolicy.Policy.Expanding,
                                   QtWidgets.QSizePolicy.Policy.Expanding)
        FigureCanvas.updateGeometry(self)

    def add_text(self):
        """
        Инициализация графика.

        :return: None.
        """
        # Инициализация области графика модулированного сигнала
        self.ax1.set_title("Исходный информационный сигнал")
        self.ax1.grid(linestyle="dotted", alpha=0.65)
        self.ax2.set_title("Информационный сигнал, заменённый кодами Голда")
        self.ax2.grid(linestyle="dotted", alpha=0.65)
        self.ax3.set_title("Синфазная компонента (I)")
        self.ax3.grid(linestyle="dotted", alpha=0.65)
        self.ax4.set_title("Квадратурная компонента (Q)")
        self.ax4.grid(linestyle="dotted", alpha=0.65)
        self.ax5.set_title("QPSK сигнал")
        self.ax5.grid(linestyle="dotted", alpha=0.65)
        self.ax6.set_title("Отклики согласованных фильтров")
        self.ax6.grid(linestyle="dotted", alpha=0.65)
        self.ax7.set_title("Восстановленный информационный сигнал")
        self.ax7.grid(linestyle="dotted", alpha=0.65)

    def plot_graph_ax1(self, x_list: list, y_list: list):
        """
        Построение исходной информационной последовательности.

        :param x_list: Список временный отсчётов.
        :param y_list: Список значений.
        :return: None.
        """
        self.ax1.plot(x_list, y_list, linestyle="-", markersize=2, color='r')
        self.ax1.margins(y=0.2, x=0.01)

    def plot_graph_ax2(self, x_list: list, y_list: list):
        """
        Построение последовательности после замены на коды Голда.

        :param x_list: Список временный отсчётов.
        :param y_list: Список значений.
        :return: None.
        """
        self.ax2.plot(x_list, y_list, linestyle="-", markersize=2, color='g')
        self.ax2.margins(y=0.2, x=0.01)

    def plot_graph_ax3(self, x_list: list, y_list: list):
        """
        Построение I компоненты.

        :param x_list: Список временный отсчётов.
        :param y_list: Список значений.
        :return: None.
        """
        self.ax3.plot(x_list, y_list, linestyle="-", markersize=2, color='orange')
        self.ax3.margins(y=0.2, x=0.01)

    def plot_graph_ax4(self, x_list: list, y_list: list):
        """
        Построение Q компоненты.

        :param x_list: Список временный отсчётов.
        :param y_list: Список значений.
        :return: None.
        """
        self.ax4.plot(x_list, y_list, linestyle="-", markersize=2, color='brown')
        self.ax4.margins(y=0.2, x=0.01)

    def plot_graph_ax5(self, x_list: list, y_list: list):
        """
        Построение QPSK сигнала.

        :param x_list: Список временный отсчётов.
        :param y_list: Список значений.
        :return: None.
        """
        self.ax5.plot(x_list, y_list, linestyle="-", markersize=2, color='cadetblue')
        self.ax5.margins(y=0.2, x=0.01)

    def plot_graph_ax6(self, x1: list, y1: list, x2: list, y2: list,
                       x3: list, y3: list, x4: list, y4: list):
        """
        Построение откликов после свёртки.

        :return: None.
        """
        self.ax6.plot(x1, y1, linestyle="-", markersize=2, color='darksalmon')
        self.ax6.plot(x2, y2, linestyle="-", markersize=2, color='olivedrab')
        self.ax6.plot(x3, y3, linestyle="-", markersize=2, color='darkkhaki')
        self.ax6.plot(x4, y4, linestyle="-", markersize=2, color='cornflowerblue')
        self.ax6.margins(y=0.2, x=0.01)

    def plot_graph_ax7(self, x_list: list, y_list: list):
        """
        Построение восстановленной информации.

        :param x_list: Список временный отсчётов.
        :param y_list: Список значений.
        :return: None.
        """
        self.ax7.plot(x_list, y_list, linestyle="-", markersize=2, color='purple')
        self.ax7.margins(y=0.2, x=0.01)

    def clear_plot_ax1(self):
        """
        Очистка области графика.

        :return: None.
        """
        self.ax1.clear()
        self.add_text()

    def clear_plot_ax2(self):
        """
        Очистка области графика.

        :return: None.
        """
        self.ax2.clear()
        self.add_text()

    def clear_plot_ax3(self):
        """
        Очистка области графика.

        :return: None.
        """
        self.ax3.clear()
        self.add_text()

    def clear_plot_ax4(self):
        """
        Очистка области графика.

        :return: None.
        """
        self.ax4.clear()
        self.add_text()

    def clear_plot_ax5(self):
        """
        Очистка области графика.

        :return: None.
        """
        self.ax5.clear()
        self.add_text()

    def clear_plot_ax6(self):
        """
        Очистка области графика.

        :return: None.
        """
        self.ax6.clear()
        self.add_text()

    def clear_plot_ax7(self):
        """
        Очистка области графика.

        :return: None.
        """
        self.ax7.clear()
        self.add_text()
