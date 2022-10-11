from enum import Enum


class GraphType(Enum):
    """
    Типы графиков для отрисовки
    """
    INPUT_BITS = 0
    GOLD_BITS = 1
    I_COMP = 2
    Q_COMP = 3
    RESPONSE = 4
    RESTORED = 5
