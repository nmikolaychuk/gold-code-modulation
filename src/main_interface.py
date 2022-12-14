# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '../ui/main.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(1100, 700)
        MainWindow.setMinimumSize(QtCore.QSize(1100, 700))
        MainWindow.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        MainWindow.setStyleSheet("background-color: rgb(240, 240, 240);")
        MainWindow.setToolButtonStyle(QtCore.Qt.ToolButtonTextBesideIcon)
        MainWindow.setAnimated(True)
        MainWindow.setDocumentMode(False)
        MainWindow.setDockNestingEnabled(False)
        MainWindow.setUnifiedTitleAndToolBarOnMac(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("border: none;")
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.side_menu_container = QtWidgets.QFrame(self.centralwidget)
        self.side_menu_container.setMinimumSize(QtCore.QSize(0, 0))
        self.side_menu_container.setMaximumSize(QtCore.QSize(200, 16777215))
        self.side_menu_container.setStyleSheet("background-color: rgb(21, 28, 77);\n"
"border: none;")
        self.side_menu_container.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.side_menu_container.setFrameShadow(QtWidgets.QFrame.Raised)
        self.side_menu_container.setObjectName("side_menu_container")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.side_menu_container)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.side_menu = QtWidgets.QFrame(self.side_menu_container)
        self.side_menu.setMinimumSize(QtCore.QSize(200, 0))
        self.side_menu.setStyleSheet("")
        self.side_menu.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.side_menu.setFrameShadow(QtWidgets.QFrame.Raised)
        self.side_menu.setObjectName("side_menu")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.side_menu)
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.buttons_frame = QtWidgets.QFrame(self.side_menu)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.buttons_frame.sizePolicy().hasHeightForWidth())
        self.buttons_frame.setSizePolicy(sizePolicy)
        self.buttons_frame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.buttons_frame.setFrameShadow(QtWidgets.QFrame.Plain)
        self.buttons_frame.setObjectName("buttons_frame")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.buttons_frame)
        self.verticalLayout_7.setContentsMargins(10, 0, 0, 0)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        spacerItem = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_7.addItem(spacerItem)
        self.open_parameters_page_button = QtWidgets.QPushButton(self.buttons_frame)
        self.open_parameters_page_button.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.open_parameters_page_button.setFont(font)
        self.open_parameters_page_button.setStyleSheet("color: rgb(255, 255, 255);")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../ui\\../icons/settings.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.open_parameters_page_button.setIcon(icon)
        self.open_parameters_page_button.setIconSize(QtCore.QSize(30, 30))
        self.open_parameters_page_button.setObjectName("open_parameters_page_button")
        self.verticalLayout_7.addWidget(self.open_parameters_page_button, 0, QtCore.Qt.AlignLeft)
        self.open_main_page_button = QtWidgets.QPushButton(self.buttons_frame)
        self.open_main_page_button.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.open_main_page_button.setFont(font)
        self.open_main_page_button.setStyleSheet("color: rgb(255, 255, 255);")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("../ui\\../icons/main_graphs.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.open_main_page_button.setIcon(icon1)
        self.open_main_page_button.setIconSize(QtCore.QSize(30, 30))
        self.open_main_page_button.setObjectName("open_main_page_button")
        self.verticalLayout_7.addWidget(self.open_main_page_button, 0, QtCore.Qt.AlignLeft)
        self.open_research_page_button = QtWidgets.QPushButton(self.buttons_frame)
        self.open_research_page_button.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.open_research_page_button.setFont(font)
        self.open_research_page_button.setStyleSheet("color: rgb(255, 255, 255);")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("../ui\\../icons/research.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.open_research_page_button.setIcon(icon2)
        self.open_research_page_button.setIconSize(QtCore.QSize(30, 30))
        self.open_research_page_button.setObjectName("open_research_page_button")
        self.verticalLayout_7.addWidget(self.open_research_page_button, 0, QtCore.Qt.AlignLeft)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_7.addItem(spacerItem1)
        self.verticalLayout_6.addWidget(self.buttons_frame)
        self.verticalLayout_2.addWidget(self.side_menu)
        self.horizontalLayout.addWidget(self.side_menu_container)
        self.main_container = QtWidgets.QFrame(self.centralwidget)
        self.main_container.setStyleSheet("background-color: rgb(229, 229, 229);")
        self.main_container.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.main_container.setFrameShadow(QtWidgets.QFrame.Raised)
        self.main_container.setObjectName("main_container")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.main_container)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.header_container = QtWidgets.QFrame(self.main_container)
        self.header_container.setStyleSheet("background-color: rgb(21, 28, 77);\n"
"border: none;")
        self.header_container.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.header_container.setFrameShadow(QtWidgets.QFrame.Raised)
        self.header_container.setObjectName("header_container")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.header_container)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.side_menu_button_frame = QtWidgets.QFrame(self.header_container)
        self.side_menu_button_frame.setStyleSheet("border: none;")
        self.side_menu_button_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.side_menu_button_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.side_menu_button_frame.setObjectName("side_menu_button_frame")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.side_menu_button_frame)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.side_menu_button = QtWidgets.QPushButton(self.side_menu_button_frame)
        self.side_menu_button.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("../ui\\../icons/back_menu.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.side_menu_button.setIcon(icon3)
        self.side_menu_button.setIconSize(QtCore.QSize(30, 30))
        self.side_menu_button.setObjectName("side_menu_button")
        self.verticalLayout_3.addWidget(self.side_menu_button)
        self.horizontalLayout_2.addWidget(self.side_menu_button_frame, 0, QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.title_frame = QtWidgets.QFrame(self.header_container)
        self.title_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.title_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.title_frame.setObjectName("title_frame")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.title_frame)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_4 = QtWidgets.QLabel(self.title_frame)
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(10)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_3.addWidget(self.label_4, 0, QtCore.Qt.AlignHCenter)
        self.horizontalLayout_2.addWidget(self.title_frame)
        self.window_buttons_frame = QtWidgets.QFrame(self.header_container)
        self.window_buttons_frame.setStyleSheet("border: none;")
        self.window_buttons_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.window_buttons_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.window_buttons_frame.setObjectName("window_buttons_frame")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.window_buttons_frame)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.minimized_button = QtWidgets.QPushButton(self.window_buttons_frame)
        self.minimized_button.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("../ui\\../icons/minimize_button.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.minimized_button.setIcon(icon4)
        self.minimized_button.setIconSize(QtCore.QSize(30, 30))
        self.minimized_button.setObjectName("minimized_button")
        self.horizontalLayout_4.addWidget(self.minimized_button)
        self.maximized_button = QtWidgets.QPushButton(self.window_buttons_frame)
        self.maximized_button.setText("")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("../ui\\../icons/maximize_button.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.maximized_button.setIcon(icon5)
        self.maximized_button.setIconSize(QtCore.QSize(30, 30))
        self.maximized_button.setObjectName("maximized_button")
        self.horizontalLayout_4.addWidget(self.maximized_button)
        self.close_button = QtWidgets.QPushButton(self.window_buttons_frame)
        self.close_button.setText("")
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("../ui\\../icons/close_button.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.close_button.setIcon(icon6)
        self.close_button.setIconSize(QtCore.QSize(30, 30))
        self.close_button.setObjectName("close_button")
        self.horizontalLayout_4.addWidget(self.close_button)
        self.horizontalLayout_2.addWidget(self.window_buttons_frame, 0, QtCore.Qt.AlignRight|QtCore.Qt.AlignTop)
        self.verticalLayout.addWidget(self.header_container, 0, QtCore.Qt.AlignTop)
        self.main_frame_container = QtWidgets.QFrame(self.main_container)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.main_frame_container.sizePolicy().hasHeightForWidth())
        self.main_frame_container.setSizePolicy(sizePolicy)
        self.main_frame_container.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.main_frame_container.setFrameShadow(QtWidgets.QFrame.Raised)
        self.main_frame_container.setObjectName("main_frame_container")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.main_frame_container)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.stacked_widget = QtWidgets.QStackedWidget(self.main_frame_container)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.stacked_widget.sizePolicy().hasHeightForWidth())
        self.stacked_widget.setSizePolicy(sizePolicy)
        self.stacked_widget.setStyleSheet("")
        self.stacked_widget.setObjectName("stacked_widget")
        self.parameters_page = QtWidgets.QWidget()
        self.parameters_page.setObjectName("parameters_page")
        self.formLayout = QtWidgets.QFormLayout(self.parameters_page)
        self.formLayout.setObjectName("formLayout")
        self.names_container = QtWidgets.QFrame(self.parameters_page)
        self.names_container.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.names_container.setFrameShadow(QtWidgets.QFrame.Raised)
        self.names_container.setObjectName("names_container")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.names_container)
        self.verticalLayout_8.setSizeConstraint(QtWidgets.QLayout.SetMaximumSize)
        self.verticalLayout_8.setContentsMargins(20, 20, 0, 0)
        self.verticalLayout_8.setSpacing(10)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.label_5 = QtWidgets.QLabel(self.names_container)
        self.label_5.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_5.setFont(font)
        self.label_5.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_8.addWidget(self.label_5)
        self.label_9 = QtWidgets.QLabel(self.names_container)
        self.label_9.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_9.setFont(font)
        self.label_9.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_9.setObjectName("label_9")
        self.verticalLayout_8.addWidget(self.label_9)
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.names_container)
        self.edit_container = QtWidgets.QFrame(self.parameters_page)
        self.edit_container.setStyleSheet("")
        self.edit_container.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.edit_container.setFrameShadow(QtWidgets.QFrame.Raised)
        self.edit_container.setObjectName("edit_container")
        self.verticalLayout_12 = QtWidgets.QVBoxLayout(self.edit_container)
        self.verticalLayout_12.setSizeConstraint(QtWidgets.QLayout.SetMaximumSize)
        self.verticalLayout_12.setContentsMargins(0, 20, 20, 0)
        self.verticalLayout_12.setSpacing(10)
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        self.bits_count_edit = QtWidgets.QLineEdit(self.edit_container)
        self.bits_count_edit.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.bits_count_edit.setFont(font)
        self.bits_count_edit.setStyleSheet("border: 1px solid black;\n"
"border-radius: 10px;")
        self.bits_count_edit.setAlignment(QtCore.Qt.AlignCenter)
        self.bits_count_edit.setObjectName("bits_count_edit")
        self.verticalLayout_12.addWidget(self.bits_count_edit)
        self.snr_edit = QtWidgets.QLineEdit(self.edit_container)
        self.snr_edit.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.snr_edit.setFont(font)
        self.snr_edit.setStyleSheet("border: 1px solid black;\n"
"border-radius: 10px;")
        self.snr_edit.setAlignment(QtCore.Qt.AlignCenter)
        self.snr_edit.setObjectName("snr_edit")
        self.verticalLayout_12.addWidget(self.snr_edit)
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.edit_container)
        self.start_button_container = QtWidgets.QFrame(self.parameters_page)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.start_button_container.sizePolicy().hasHeightForWidth())
        self.start_button_container.setSizePolicy(sizePolicy)
        self.start_button_container.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.start_button_container.setFrameShadow(QtWidgets.QFrame.Raised)
        self.start_button_container.setObjectName("start_button_container")
        self.verticalLayout_14 = QtWidgets.QVBoxLayout(self.start_button_container)
        self.verticalLayout_14.setContentsMargins(0, 40, 0, 0)
        self.verticalLayout_14.setSpacing(0)
        self.verticalLayout_14.setObjectName("verticalLayout_14")
        self.start_calc_button = QtWidgets.QPushButton(self.start_button_container)
        self.start_calc_button.setMinimumSize(QtCore.QSize(350, 60))
        self.start_calc_button.setMaximumSize(QtCore.QSize(200, 40))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(16)
        self.start_calc_button.setFont(font)
        self.start_calc_button.setStyleSheet("background-color: rgb(21, 28, 77);\n"
"color: rgb(255, 255, 255);\n"
"border: 1px solid black;\n"
"border-radius: 20px;")
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap("../ui\\../icons/start.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.start_calc_button.setIcon(icon7)
        self.start_calc_button.setIconSize(QtCore.QSize(30, 30))
        self.start_calc_button.setObjectName("start_calc_button")
        self.verticalLayout_14.addWidget(self.start_calc_button, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.SpanningRole, self.start_button_container)
        self.stacked_widget.addWidget(self.parameters_page)
        self.main_page = QtWidgets.QWidget()
        self.main_page.setObjectName("main_page")
        self.verticalLayout_15 = QtWidgets.QVBoxLayout(self.main_page)
        self.verticalLayout_15.setObjectName("verticalLayout_15")
        self.plots_frame = QtWidgets.QFrame(self.main_page)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.plots_frame.sizePolicy().hasHeightForWidth())
        self.plots_frame.setSizePolicy(sizePolicy)
        self.plots_frame.setMaximumSize(QtCore.QSize(16777215, 580))
        self.plots_frame.setStyleSheet("")
        self.plots_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.plots_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.plots_frame.setObjectName("plots_frame")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.plots_frame)
        self.verticalLayout_9.setSizeConstraint(QtWidgets.QLayout.SetMaximumSize)
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.verticalLayout_16 = QtWidgets.QVBoxLayout()
        self.verticalLayout_16.setSizeConstraint(QtWidgets.QLayout.SetMaximumSize)
        self.verticalLayout_16.setSpacing(0)
        self.verticalLayout_16.setObjectName("verticalLayout_16")
        self.verticalLayout_9.addLayout(self.verticalLayout_16)
        self.verticalLayout_15.addWidget(self.plots_frame)
        self.button_frame = QtWidgets.QFrame(self.main_page)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_frame.sizePolicy().hasHeightForWidth())
        self.button_frame.setSizePolicy(sizePolicy)
        self.button_frame.setMinimumSize(QtCore.QSize(0, 30))
        self.button_frame.setStyleSheet("")
        self.button_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.button_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.button_frame.setObjectName("button_frame")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.button_frame)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.calc_filters = QtWidgets.QPushButton(self.button_frame)
        self.calc_filters.setMinimumSize(QtCore.QSize(200, 30))
        self.calc_filters.setMaximumSize(QtCore.QSize(200, 30))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(10)
        self.calc_filters.setFont(font)
        self.calc_filters.setStyleSheet("background-color: rgb(21, 28, 77);\n"
"color: rgb(255, 255, 255);\n"
"border: 1px solid black;\n"
"border-radius: 15px;")
        self.calc_filters.setObjectName("calc_filters")
        self.horizontalLayout_5.addWidget(self.calc_filters)
        self.draw_button = QtWidgets.QPushButton(self.button_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.draw_button.sizePolicy().hasHeightForWidth())
        self.draw_button.setSizePolicy(sizePolicy)
        self.draw_button.setMinimumSize(QtCore.QSize(200, 30))
        self.draw_button.setMaximumSize(QtCore.QSize(200, 30))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.draw_button.setFont(font)
        self.draw_button.setStyleSheet("background-color: rgb(21, 28, 77);\n"
"color: rgb(255, 255, 255);\n"
"border: 1px solid black;\n"
"border-radius: 15px;")
        self.draw_button.setObjectName("draw_button")
        self.horizontalLayout_5.addWidget(self.draw_button)
        self.verticalLayout_15.addWidget(self.button_frame)
        self.stacked_widget.addWidget(self.main_page)
        self.research_page = QtWidgets.QWidget()
        self.research_page.setObjectName("research_page")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.research_page)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.frame_3 = QtWidgets.QFrame(self.research_page)
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.frame_3)
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout()
        self.verticalLayout_10.setSpacing(0)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.horizontalLayout_7.addLayout(self.verticalLayout_10)
        self.horizontalLayout_6.addWidget(self.frame_3)
        self.frame_4 = QtWidgets.QFrame(self.research_page)
        self.frame_4.setStyleSheet("border: 1px solid black;\n"
"border-radius: 20px;")
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.verticalLayout_13 = QtWidgets.QVBoxLayout(self.frame_4)
        self.verticalLayout_13.setObjectName("verticalLayout_13")
        self.average_count_edit = QtWidgets.QLineEdit(self.frame_4)
        self.average_count_edit.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(10)
        self.average_count_edit.setFont(font)
        self.average_count_edit.setStyleSheet("border: 1px solid black;\n"
"border-radius: 10px;")
        self.average_count_edit.setText("")
        self.average_count_edit.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.average_count_edit.setObjectName("average_count_edit")
        self.verticalLayout_13.addWidget(self.average_count_edit)
        self.label_3 = QtWidgets.QLabel(self.frame_4)
        self.label_3.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("border: none;")
        self.label_3.setObjectName("label_3")
        self.verticalLayout_13.addWidget(self.label_3)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_13.addItem(spacerItem2)
        self.start_research_button = QtWidgets.QPushButton(self.frame_4)
        self.start_research_button.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(10)
        self.start_research_button.setFont(font)
        self.start_research_button.setStyleSheet("background-color: rgb(21, 28, 77);\n"
"color: rgb(255, 255, 255);\n"
"border: 1px solid black;\n"
"border-radius: 15px;")
        self.start_research_button.setObjectName("start_research_button")
        self.verticalLayout_13.addWidget(self.start_research_button)
        self.horizontalLayout_6.addWidget(self.frame_4, 0, QtCore.Qt.AlignRight)
        self.stacked_widget.addWidget(self.research_page)
        self.verticalLayout_5.addWidget(self.stacked_widget)
        self.verticalLayout.addWidget(self.main_frame_container)
        self.footer_container = QtWidgets.QFrame(self.main_container)
        self.footer_container.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.footer_container.setFrameShadow(QtWidgets.QFrame.Raised)
        self.footer_container.setObjectName("footer_container")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.footer_container)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.resize_frame = QtWidgets.QFrame(self.footer_container)
        self.resize_frame.setMinimumSize(QtCore.QSize(10, 10))
        self.resize_frame.setMaximumSize(QtCore.QSize(10, 10))
        self.resize_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.resize_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.resize_frame.setObjectName("resize_frame")
        self.verticalLayout_4.addWidget(self.resize_frame, 0, QtCore.Qt.AlignRight|QtCore.Qt.AlignBottom)
        self.verticalLayout.addWidget(self.footer_container, 0, QtCore.Qt.AlignRight|QtCore.Qt.AlignBottom)
        self.horizontalLayout.addWidget(self.main_container)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1100, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)

        self.retranslateUi(MainWindow)
        self.stacked_widget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.open_parameters_page_button.setText(_translate("MainWindow", "   ?????????????????? ????????????"))
        self.open_main_page_button.setText(_translate("MainWindow", "   ??????????????"))
        self.open_research_page_button.setText(_translate("MainWindow", "   ????????????????????????"))
        self.label_4.setText(_translate("MainWindow", "?????????????????????????? ????4, ?????????????????????????????? ?????????????????????????????????????? ??????????"))
        self.label_5.setText(_translate("MainWindow", "?????????? ???????????????????????????? ??????"))
        self.label_9.setText(_translate("MainWindow", "?????? ?? ?????????????????????? ????????????, ????"))
        self.start_calc_button.setText(_translate("MainWindow", "?????????????? ?? ????????????????????"))
        self.calc_filters.setText(_translate("MainWindow", "???????????? ????"))
        self.draw_button.setText(_translate("MainWindow", "??????????????????"))
        self.label_3.setText(_translate("MainWindow", "???????????????????? ????????????????????"))
        self.start_research_button.setText(_translate("MainWindow", "??????????????????"))
