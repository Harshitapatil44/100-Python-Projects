stocks = {}

def buy_stock():
    name = input("Enter stock name: ").upper()
    quantity = int(input("Enter quantity: "))
    price = float(input("Enter price per stock: "))

    if name in stocks:
        stocks[name]["quantity"] += quantity
        stocks[name]["price"] = price
    else:
        stocks[name] = {
            "quantity": quantity,
            "price": price
        }

    print(f"{name} added successfully.\n")


def view_portfolio():
    if not stocks:
        print("Portfolio is empty.\n")
        return

    total_value = 0

    print("\n--- Portfolio ---")
    for name, data in stocks.items():
        value = data["quantity"] * data["price"]
        total_value += value
        print(
            f"Stock: {name} | "
            f"Quantity: {data['quantity']} | "
            f"Price: ₹{data['price']} | "
            f"Value: ₹{value}"
        )

    print(f"\nTotal Portfolio Value: ₹{total_value}\n")


def sell_stock():
    name = input("Enter stock name to sell: ").upper()

    if name not in stocks:
        print("Stock not found.\n")
        return
    quantity = int(input("Enter quantity to sell: "))

    if quantity >= stocks[name]["quantity"]:
        del stocks[name]
        print(f"{name} removed from portfolio.\n")
    else:
        stocks[name]["quantity"] -= quantity
        print(f"Sold {quantity} shares of {name}.\n")


while True:
    print("===== Stock Market Tracker =====")
    print("1. Buy Stock")
    print("2. View Portfolio")
    print("3. Sell Stock")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        buy_stock()
    elif choice == "2":
        view_portfolio()
    elif choice == "3":
        sell_stock()
    elif choice == "4":
        print("Exiting Program...")
        break
    else:
        print("Invalid choice. Try again.\n")

