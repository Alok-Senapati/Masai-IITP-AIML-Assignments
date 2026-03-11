def create_inventory():
    return dict()


def add_product(inventory, name, price, quantity):
    if name in inventory.keys():
        inventory[name]["price"] = price
        inventory[name]["quantity"] += quantity
    else:
        inventory[name] = {
            "price": price,
            "quantity": quantity
        }


def remove_product(inventory, name):
    if inventory.pop(name, None) is None:
        return False
    return True


def get_product_info(inventory, name):
    return inventory.get(name, None)


def calculate_total_value(inventory):
    total_value = 0
    for name, info in inventory.items():
        quantity = info["quantity"]
        price = info["price"]
        total_value += (quantity * price)
    return total_value


def get_low_stock(inventory, threshold=5):
    return [name for name, info in inventory.items() if info["quantity"] <= threshold]


def main():
    # Create inventory
    inv = create_inventory()

    # Add products
    add_product(inv, "laptop", 999.99, 10)
    add_product(inv, "mouse", 29.99, 50)
    add_product(inv, "keyboard", 79.99, 3)
    add_product(inv, "monitor", 299.99, 8)

    # Get product info
    print(get_product_info(inv, "laptop"))
    # Output: {"price": 999.99, "quantity": 10}

    # Calculate total value
    print(calculate_total_value(inv))
    # Output: 14099.32 (999.99*10 + 29.99*50 + 79.99*3 + 299.99*8)

    # Get low stock items
    print(get_low_stock(inv, threshold=5))
    # Output: ["keyboard"]

    # Remove product
    print(remove_product(inv, "mouse"))  # Output: True
    print(remove_product(inv, "tablet"))  # Output: False


if __name__ == '__main__':
    main()
