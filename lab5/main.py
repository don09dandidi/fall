# ADAUGĂ ACESTE LINII LA ÎNCEPUT
from coffee_shop.barista import Barista
from coffee_shop.coffee import Coffee, Cappuccino, Americano, PumpkinSpiceLatte, SyrupCappuccino
from coffee_shop.enums import Intensity, SyrupType

def demo_predefined_orders():
    """Demonstrație cu comenzi pre-definite"""
    print("🚀 DEMO MODE: Pre-defined Orders\n")
    
    # Creăm Barista (singura clasă accesibilă din main)
    barista = Barista()
    
    # Adăugăm diferite tipuri de cafea
    barista.add_order(Coffee(Intensity.NORMAL))
    barista.add_order(Cappuccino(Intensity.NORMAL, 50))
    barista.add_order(PumpkinSpiceLatte(Intensity.STRONG, 60, 15))
    barista.add_order(Americano(Intensity.LIGHT, 100))
    barista.add_order(SyrupCappuccino(Intensity.NORMAL, 50, SyrupType.VANILLA))
    
    # Procesăm toate comenzile
    barista.process_orders()


def interactive_mode():
    """Mod interactiv - utilizatorul comandă cafea"""
    print("☕ INTERACTIVE MODE: Coffee Shop\n")
    
    barista = Barista()
    
    while True:
        barista.take_interactive_order()
        
        print(f"\nCurrent orders in queue: {barista.get_order_count()}")
        
        choice = input("\nOptions:\n1. Add another order\n2. Process all orders\n3. Exit\nChoose (1-3): ")
        
        if choice == "2":
            barista.process_orders()
        elif choice == "3":
            if barista.get_order_count() > 0:
                process = input("You have pending orders. Process them? (y/n): ")
                if process.lower() == 'y':
                    barista.process_orders()
            print("\n👋 Thank you! Come again!")
            break


def main():
    """Funcția principală"""
    print("="*50)
    print("   ☕ WELCOME TO COFFEE SHOP OOP LAB ☕")
    print("="*50)
    
    mode = input("\nChoose mode:\n1. Demo (pre-defined orders)\n2. Interactive\nChoice (1-2): ")
    
    if mode == "1":
        demo_predefined_orders()
    elif mode == "2":
        interactive_mode()
    else:
        print("Invalid choice!")


if __name__ == "__main__":
    main()