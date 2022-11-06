from enum import Enum


class GraphType(Enum):
    """
    Типы графиков для отрисовки
    """
    INPUT_BITS = 0
    I_COMP = 1
    Q_COMP = 2
    RESPONSE = 3
    RESTORED = 4


class ShiftRegisterType(Enum):
    """
    Возможные конфигурации сдвигового регистра
    """
    FIVE_THREE = 0
    FIVE_FOUR_THREE_TWO = 1
