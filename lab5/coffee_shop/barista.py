from coffee_shop.coffee import Coffee, Cappuccino, Americano, PumpkinSpiceLatte, SyrupCappuccino
from coffee_shop.enums import Intensity, SyrupType

class Barista:
    """
    Barista - intermediarul care procesează comenzi de cafea.
    
    Acest nivel de abstractizare asigură că:
    - Main nu poate accesa direct clasele Coffee
    - Logica de business este encapsulată
    - Separăm interfața de implementare
    """
    
    def __init__(self):
        self._orders = []
    
    def add_order(self, coffee: Coffee):
        """Adaugă o comandă în lista de așteptare"""
        self._orders.append(coffee)
        print(f"✓ Order added: {coffee.name}")
    
    def take_interactive_order(self):
        """Ia o comandă interactivă de la utilizator"""
        print("\n" + "="*50)
        print("☕ COFFEE MENU ☕")
        print("="*50)
        print("1. Coffee (Basic)")
        print("2. Americano")
        print("3. Cappuccino")
        print("4. Syrup Cappuccino")
        print("5. Pumpkin Spice Latte")
        print("="*50)
        
        try:
            choice = int(input("Choose coffee (1-5): "))
            
            print("\nIntensity:")
            print("0 = Light, 1 = Normal, 2 = Strong")
            intensity_choice = int(input("Choose intensity (0-2): "))
            intensity_map = {0: Intensity.LIGHT, 1: Intensity.NORMAL, 2: Intensity.STRONG}
            intensity = intensity_map.get(intensity_choice, Intensity.NORMAL)
            
            if choice == 1:
                coffee = Coffee(intensity)
                self.add_order(coffee)
                
            elif choice == 2:
                water = int(input("Water amount (ml): "))
                coffee = Americano(intensity, water)
                self.add_order(coffee)
                
            elif choice == 3:
                milk = int(input("Milk amount (ml): "))
                coffee = Cappuccino(intensity, milk)
                self.add_order(coffee)
                
            elif choice == 4:
                milk = int(input("Milk amount (ml): "))
                print("\nSyrup types:")
                print("0=Macadamia, 1=Vanilla, 2=Coconut")
                print("3=Caramel, 4=Chocolate, 5=Popcorn")
                syrup_choice = int(input("Choose syrup (0-5): "))
                syrup_map = {
                    0: SyrupType.MACADAMIA, 1: SyrupType.VANILLA,
                    2: SyrupType.COCONUT, 3: SyrupType.CARAMEL,
                    4: SyrupType.CHOCOLATE, 5: SyrupType.POPCORN
                }
                syrup = syrup_map.get(syrup_choice, SyrupType.VANILLA)
                coffee = SyrupCappuccino(intensity, milk, syrup)
                self.add_order(coffee)
                
            elif choice == 5:
                milk = int(input("Milk amount (ml): "))
                spice = int(input("Pumpkin spice (mg): "))
                coffee = PumpkinSpiceLatte(intensity, milk, spice)
                self.add_order(coffee)
            
            else:
                print("Invalid choice!")
                
        except ValueError:
            print("Invalid input! Please enter numbers only.")
    
    def process_orders(self):
        """
        Procesează toate comenzile din coadă.
        Aici aplicăm TASK 3 - apelăm metodele specifice fiecărei clase.
        """
        if not self._orders:
            print("\n⚠ No orders to process!")
            return
        
        print("\n" + "="*50)
        print("🔥 BARISTA STARTS WORKING 🔥")
        print("="*50)
        print(f"Total orders: {len(self._orders)}\n")
        
        for idx, coffee in enumerate(self._orders, 1):
            print(f"\n{'─'*50}")
            print(f"📋 ORDER #{idx}")
            print(f"{'─'*50}")
            
            # TASK 2: Afișăm detaliile
            coffee.print_coffee_details()
            print()
            
            # TASK 3: Preparăm cafeaua folosind metoda specifică
            # Folosim isinstance() pentru a determina tipul și a apela metoda corectă
            if isinstance(coffee, PumpkinSpiceLatte):
                coffee.make_pumpkin_spice_latte()
            elif isinstance(coffee, SyrupCappuccino):
                coffee.make_syrup_cappuccino()
            elif isinstance(coffee, Cappuccino):
                coffee.make_cappuccino()
            elif isinstance(coffee, Americano):
                coffee.make_americano()
            else:
                coffee.make_coffee()
            
            print(f"\n✅ Order #{idx} ready!")
        
        print("\n" + "="*50)
        print("🎉 ALL ORDERS COMPLETED 🎉")
        print("="*50)
        
        # Golim lista după procesare
        self._orders.clear()
    
    def get_order_count(self):
        """Returnează numărul de comenzi în așteptare"""
        return len(self._orders)

