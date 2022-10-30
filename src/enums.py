from enum import Enum


class GraphType(Enum):
    """
    Типы графиков для отрисовки
    """
    INPUT_BITS = 0
    GOLD_BITS = 1
    I_COMP = 2
    Q_COMP = 3
    QPSK = 4
    RESPONSE = 5
    RESTORED = 6


class ShiftRegisterType(Enum):
    """
    Возможные конфигурации сдвигового регистра
    """
    FIVE_THREE = 0
    FIVE_FOUR_THREE_TWO = 1
