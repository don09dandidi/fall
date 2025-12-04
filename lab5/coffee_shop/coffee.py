# ADAUGĂ ACEST IMPORT LA ÎNCEPUT
from coffee_shop.enums import Intensity, SyrupType


class Coffee:
    """
    Clasa de bază pentru toate tipurile de cafea.
    Conține doar intensitatea cafelei.
    """
    def __init__(self, coffee_intensity: Intensity):
        self._coffee_intensity = coffee_intensity
        self._name = "Coffee"
    
    @property
    def coffee_intensity(self):
        return self._coffee_intensity
    
    @property
    def name(self):
        return self._name
    
    # TASK 2: Metodă pentru afișarea detaliilor
    def print_coffee_details(self):
        """Afișează detaliile cafelei"""
        print(f"Coffee name: {self._name}")
        print(f"Coffee intensity: {self._coffee_intensity.value}")
    
    # TASK 3: Metodă pentru prepararea cafelei
    def make_coffee(self):
        """Prepară cafeaua (metodă de bază)"""
        print(f"Making {self._name}")
        print(f"Intensity set to {self._coffee_intensity.value}")
        return self


class Americano(Coffee):
    """
    Americano - moștenește Coffee și adaugă apă.
    Adaugă UN singur câmp nou: mlOfWater
    """
    def __init__(self, coffee_intensity: Intensity, ml_of_water: int):
        super().__init__(coffee_intensity)
        self._ml_of_water = ml_of_water
        self._name = "Americano"
    
    @property
    def ml_of_water(self):
        return self._ml_of_water
    
    # TASK 2: Suprascrie și extinde metoda părinte
    def print_coffee_details(self):
        """Afișează detaliile Americano"""
        print(f"Coffee name: {self._name}")
        print(f"Coffee intensity: {self._coffee_intensity.value}")
        print(f"Water: {self._ml_of_water} ml")
    
    # TASK 3: Metodă specifică Americano
    def make_americano(self):
        """Prepară Americano cu pașii specifici"""
        print(f"Making {self._name}")
        # Refolosim logica de bază
        super().make_coffee()
        # Adăugăm pasul specific
        print(f"Adding {self._ml_of_water} ml of water")
        return self


class Cappuccino(Coffee):
    """
    Cappuccino - moștenește Coffee și adaugă lapte.
    Adaugă UN singur câmp nou: mlOfMilk
    """
    def __init__(self, coffee_intensity: Intensity, ml_of_milk: int):
        super().__init__(coffee_intensity)
        self._ml_of_milk = ml_of_milk
        self._name = "Cappuccino"
    
    @property
    def ml_of_milk(self):
        return self._ml_of_milk
    
    # TASK 2: Suprascrie metoda - principiul DRY
    def print_coffee_details(self):
        """Afișează detaliile Cappuccino"""
        print(f"Coffee name: {self._name}")
        print(f"Coffee intensity: {self._coffee_intensity.value}")
        print(f"Milk: {self._ml_of_milk} ml")
    
    # TASK 3: Metodă specifică Cappuccino
    def make_cappuccino(self):
        """Prepară Cappuccino cu pașii specifici"""
        print(f"Making {self._name}")
        # Refolosim logica de bază (super keyword)
        super().make_coffee()
        # Adăugăm pasul specific
        print(f"Frothing {self._ml_of_milk} ml of milk")
        return self


class SyrupCappuccino(Cappuccino):
    """
    SyrupCappuccino - moștenește Cappuccino și adaugă sirop.
    Adaugă UN singur câmp nou: syrup
    """
    def __init__(self, coffee_intensity: Intensity, ml_of_milk: int, syrup: SyrupType):
        super().__init__(coffee_intensity, ml_of_milk)
        self._syrup = syrup
        self._name = "SyrupCappuccino"
    
    @property
    def syrup(self):
        return self._syrup
    
    # TASK 2: Extinde funcționalitatea părintelui
    def print_coffee_details(self):
        """Afișează detaliile SyrupCappuccino"""
        print(f"Coffee name: {self._name}")
        print(f"Coffee intensity: {self._coffee_intensity.value}")
        print(f"Milk: {self._ml_of_milk} ml")
        print(f"Syrup: {self._syrup.value}")
    
    # TASK 3: Metodă specifică SyrupCappuccino
    def make_syrup_cappuccino(self):
        """Prepară SyrupCappuccino cu pașii specifici"""
        print(f"Making {self._name}")
        # Refolosim logica bunicului (Coffee)
        Coffee.make_coffee(self)
        # Adăugăm pașii specifici
        print(f"Frothing {self._ml_of_milk} ml of milk")
        print(f"Adding {self._syrup.value} syrup")
        return self


class PumpkinSpiceLatte(Cappuccino):
    """
    PumpkinSpiceLatte - moștenește Cappuccino și adaugă condiment dovleac.
    Adaugă UN singur câmp nou: mgOfPumpkinSpice
    """
    def __init__(self, coffee_intensity: Intensity, ml_of_milk: int, mg_of_pumpkin_spice: int):
        super().__init__(coffee_intensity, ml_of_milk)
        self._mg_of_pumpkin_spice = mg_of_pumpkin_spice
        self._name = "PumpkinSpiceLatte"
    
    @property
    def mg_of_pumpkin_spice(self):
        return self._mg_of_pumpkin_spice
    
    # TASK 2: Extinde metoda părinte
    def print_coffee_details(self):
        """Afișează detaliile PumpkinSpiceLatte"""
        print(f"Coffee name: {self._name}")
        print(f"Coffee intensity: {self._coffee_intensity.value}")
        print(f"Milk: {self._ml_of_milk} ml")
        print(f"Pumpkin spice: {self._mg_of_pumpkin_spice} mg")
    
    # TASK 3: Metodă specifică PumpkinSpiceLatte
    def make_pumpkin_spice_latte(self):
        """Prepară PumpkinSpiceLatte cu pașii specifici"""
        print(f"Making {self._name}")
        # Refolosim logica de bază
        Coffee.make_coffee(self)
        # Adăugăm pașii specifici în ordine
        print(f"Frothing {self._ml_of_milk} ml of milk")
        print(f"Adding {self._mg_of_pumpkin_spice} mg of pumpkin spice")
        return self
