
shopping_cart = []

def add_item(item, quantity):
    shopping_cart.append({'item': item, 'quantity': quantity})
    print(f"Added {quantity} of {item} to the cart.")
    print_cart()


def remove_item(item):
    for i in range(len(shopping_cart)):
        if shopping_cart[i]['item'] == item:
            shopping_cart.pop(i)
            print(f"Removed {item} from the cart.")
            break
    else:
        print(f"{item} not found in the cart.")
    print_cart()

def update_quantity(item, quantity):
    for i in range(len(shopping_cart)):
        if shopping_cart[i]['item'] == item:
            shopping_cart[i]['quantity'] = quantity
            print(f"Updated {item} quantity to {quantity}.")
            break
    else:
        print(f"{item} not found in the cart.")
    print_cart()


def print_cart():
    print("Shopping Cart Contents:")
    if len(shopping_cart) == 0:
        print("Your cart is empty.")
    else:
        for entry in shopping_cart:
            print(f"{entry['item']} - {entry['quantity']}")
    print("-" * 30)


add_item("Apple", 5)
add_item("Banana", 2)
update_quantity("Apple", 10)
remove_item("Banana")
