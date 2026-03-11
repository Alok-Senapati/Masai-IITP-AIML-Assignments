def main():
    print("=" * 40)
    print((" " * 9) + "SIMPLE BILL CALCULATOR" + (" " * 9))
    print("=" * 40)
    print()
    item_name = input("Enter item name: ")
    unit_price = float(input("Enter unit price: "))
    quantity = int(input("Enter quantity: "))
    subtotal = unit_price * quantity
    gst = subtotal * 18 / 100
    total = subtotal + gst
    print()
    print("=" * 40)
    print((" " * 16) + "RECEIPT" + (" " * 17))
    print("=" * 40)
    print(f"Item:\t\t\t{item_name}")
    print(f"Unit Price:\t\t₹ {unit_price:.2f}")
    print(f"Quantity:\t\t\t{quantity}")
    print("-" * 40)
    print(f"Subtotal:\t\t₹ {subtotal:.2f}")
    print(f"GST (18%):\t\t₹ {gst:.2f}")
    print("-" * 40)
    print(f"TOTAL::\t\t\t₹ {total:.2f}")
    print("=" * 40)
    print()
    print("Thank you for your purchase!")

if __name__ == '__main__':
    main()
