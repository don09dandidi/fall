from enum import Enum

class Intensity(Enum):
    """Intensitatea cafelei"""
    LIGHT = "Light"
    NORMAL = "Normal"
    STRONG = "Strong"

class SyrupType(Enum):
    """Tipuri de sirop disponibile"""
    MACADAMIA = "Macadamia"
    VANILLA = "Vanilla"
    COCONUT = "Coconut"
    CARAMEL = "Caramel"
    CHOCOLATE = "Chocolate"
    POPCORN = "Popcorn"