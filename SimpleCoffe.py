import numpy as py  

class SimpleCoffee:
    
    # initialize coffe with name and price
    
    def __init__(self, name, price):
        
        self. name = name
        
        self.price = price
        
class Order:
            # initialize order with empty list
            
            def __init__(self):
                
                self.items = []
                
            # add coffe to order
            
            def add_item(self, coffe):
                
                self.items.append(coffe)
                
                print(f"Added {coffe.name} to your order.")
                
            # calculate total price
            
            def total(self):
                
                return sum(item.price for item in self.items)
            
            # show order summary
            
            def show_order(self):
                
                if not self.items:
                    
                    print("No items in order.")
                    
                    return
                
                print("\nYour Order:")
                
                for i, item in enumerate(self.items, 1):
                    
                    print("f{i}. {item.name} - ${item.price}")
                    
                print(f"Total: ${self.total()}\n")
                
            # handle checkout process
            
            def checkout(self):
                
                if not self.items:
                    
                    print("Your cart is empty.")
                    
                    return
                
                self.show_order()
                
                confirm = input("Proceed to checkout? (yes/no):").strip().lower()
                
                if confirm == 'yes':
                    
                    print("Order confirmed! Thank you.")
                    
                    self.items.clear()
                    
                else:
                    
                    print("Checkout cancelled.")
                    
# display menu and handle user input

def main():
    
    menu = [

        SimpleCoffee("Espresso", 2.5),

        SimpleCoffee("Latte", 3.5),

        SimpleCoffee("Cappuchino", 3.0),

        SimpleCoffee("Americano", 2.0)

    ]
    
    order = Order()
    
    # User interaction
    
    while True:
        
        print("\n--- Coffe Menu ---")
        
        for i, coffe in enumerate(menu, 1):
            
            print(f"{i}. {coffe.name} - ${coffe.price}")
            
        print("5. View Order")
        
        print("6. Checkout")
        
        print("7. Exit")
        
        choice = input("Choose an option: ")
        
        if choice in ['1', '2', '3', '4']:
            
            order.add_item(menu[int(choice) -1])
            
        elif choice == '5':
            
            order.show_order()
            
        elif choice == '6':
            
            order.checkout()
            
        elif choice == '7':
            
            print("Thanks for visiting. Goodbye!")
                  
            break
        
        else:
            
            print("Invalid choice. Try again.")
            
if __name__ == "__main__":
    
    main()
