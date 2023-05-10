from enum import auto, Enum


class RenderOrder(Enum):
    """
    Enum is a set of immutable values, and auto() is a self-incrementing integer.
    If more values are needed, we can simply arrange them in order! 
    CORPSE is currently lowest in render order, and ACTOR is highest.
    """
    CORPSE = auto()
    ITEM = auto()
    ACTOR = auto()

    