def add_item(inventory, item, quantity):
    if item in inventory:
        inventory[item] += quantity
    else:
        inventory[item] = quantity
    return inventory


def remove_item(inventory, item, quantity):
    if item not in inventory:
        print(f"item: {item} not present in inventory")
        return inventory

    if inventory[item] > quantity:
        inventory[item] -= quantity
    else:
        inventory.pop(item)
    return inventory


def display_inventory(inventory):
    for item, quantity in inventory.items():
        print(f"{item}: {quantity}")


def manage_inventory():
    inventory = {"apple": 10, "banana": 5, "orange": 8}
    inventory_after_adding = add_item(inventory=inventory, item="mango", quantity=12)
    print("After adding items:")
    print(inventory_after_adding)
    print()

    inventory_after_removing = remove_item(inventory=inventory_after_adding, item="banana", quantity=2)
    print("After removing items:")
    print(inventory_after_removing)
    print()

    print("Final Inventory:")
    display_inventory(inventory_after_removing)


if __name__ == '__main__':
    manage_inventory()

