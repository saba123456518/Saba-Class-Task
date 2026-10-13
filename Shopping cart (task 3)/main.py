
class ShoppingCart:
    def __init__(self):
         # Each cart has its own item collection
        self.items = []

    def add_item(self, name, price, quantity):
         # Add a product with price and quantity
        item = {
            "name": name,
            "price": price,
            "quantity": quantity
        }
        self.items.append(item)

    def calculate_total(self):
        # Calculate total price of all items
        total = 0

        for item in self.items:
            total += item["price"] * item["quantity"]

        return total

    def display_cart(self):
        print("\nShopping Cart Items:")

        if not self.items:
            print("Cart is empty.")
            return

        for item in self.items:
            subtotal = item["price"] * item["quantity"]

            print(
                f'{item["name"]} - '
                f'Price: Rs. {item["price"]:.2f}, '
                f'Quantity: {item["quantity"]}, '
                f'Subtotal: Rs. {subtotal:.2f}'
            )

        print(f"Cart Total: Rs. {self.calculate_total():.2f}")


cart1 = ShoppingCart()
cart2 = ShoppingCart()

cart1.add_item("Laptop", 80000, 1)
cart1.add_item("Mouse", 1500, 2)

cart2.add_item("Keyboard", 2500, 1)
cart2.add_item("Headphones", 3000, 2)

print("===== CART 1 =====")
cart1.display_cart()

print("\n===== CART 2 =====")
cart2.display_cart()

print("\n===== FINAL TOTALS =====")
print(f"Cart 1 Total: Rs. {cart1.calculate_total():.2f}")
print(f"Cart 2 Total: Rs. {cart2.calculate_total():.2f}")
