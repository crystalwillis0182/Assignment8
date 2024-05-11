class ItemToPurchase:
    def __init__(self, item_name="none", item_price=0, item_quantity=0, item_description="none"):
        self.item_name = item_name
        self.item_price = item_price
        self.item_quantity = item_quantity
        self.item_description = item_description

    def print_item_description(self):
        print(f"{self.item_name}: {self.item_description}")

class ShoppingCart:
    def __init__(self, customer_name="none", current_date="January 1, 2016"):
        self.customer_name = customer_name
        self.current_date = current_date
        self.cart_items = []

    def add_item(self, item):
        self.cart_items.append(item)

    def remove_item(self, item_name):
        for i in self.cart_items:
            if i.item_name == item_name:
                self.cart_items.remove(i)
                return
        print("Item not found in cart. Nothing removed.")

    def modify_item(self, new_item):
        for i in self.cart_items:
            if i.item_name == new_item.item_name:
                i.item_quantity = new_item.item_quantity
                return
        print("Item not found in cart. Nothing modified.")

    def get_num_items_in_cart(self):
        return sum(item.item_quantity for item in self.cart_items)

    def get_cost_of_cart(self):
        return sum(item.item_price * item.item_quantity for item in self.cart_items)

    def print_total(self):
        total_cost = self.get_cost_of_cart()
        print(f"{self.customer_name}'s Shopping Cart - {self.current_date}")
        print(f"Number of Items: {self.get_num_items_in_cart()}\n")
        for item in self.cart_items:
            print(f"{item.item_name} @ ${item.item_price} = ${item.item_price * item.item_quantity}")
        print(f"\nTotal: ${total_cost}")

    def print_descriptions(self):
        print(f"{self.customer_name}'s Shopping Cart - {self.current_date}\n")
        print("Item Descriptions")
        for item in self.cart_items:
            print(f"{item.item_name}: {item.item_description}")

def print_menu():
    print("MENU")
    print("a - Add item to cart")
    print("r - Remove item from cart")
    print("c - Change item quantity")
    print("i - Output items' descriptions")
    print("o - Output shopping cart")
    print("q - Quit")

def execute_menu(choice, cart):
    if choice == 'a':
        # Add item to cart
        item_name = input("Enter the item name: ")
        item_description = input("Enter the item description: ")
        item_price = float(input("Enter the item price: "))
        item_quantity = int(input("Enter the item quantity: "))
        new_item = ItemToPurchase(item_name, item_price, item_quantity, item_description)
        cart.add_item(new_item)
    elif choice == 'r':
        # Remove item from cart
        item_name = input("Enter name of item to remove: ")
        cart.remove_item(item_name)
    elif choice == 'c':
        # Change item quantity
        item_name = input("Enter the item name: ")
        new_quantity = int(input("Enter the new quantity: "))
        new_item = ItemToPurchase(item_name, 0, new_quantity)
        cart.modify_item(new_item)
    elif choice == 'i':
        # Output items' descriptions
        cart.print_descriptions()
    elif choice == 'o':
        # Output shopping cart
        cart.print_total()
    elif choice == 'q':
        print("Exiting program.")
    else:
        print("Invalid choice. Please try again.")

# Main section
customer_name = input("Enter customer's name: ")
current_date = input("Enter today's date: ")
print(f"\nCustomer name: {customer_name}")
print(f"Today's date: {current_date}\n")

shopping_cart = ShoppingCart(customer_name, current_date)

while True:
    print_menu()
    user_choice = input("Choose an option: ")
    execute_menu(user_choice, shopping_cart)
    if user_choice == 'q':
        break