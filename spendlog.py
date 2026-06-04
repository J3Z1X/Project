def multiply_price(quantity, price):
    return quantity * price


def show_purchases():
    print("\n===== Your Purchases =====")

    try:
        with open("spendlog.csv", "r") as file:
            for line in file:
                data = line.strip().split(",")

                if len(data) == 4:
                    product_name, qty, prod_price, total_price = data

                    print(
                        f"- {product_name} | Qty: {qty} | Price: ₱{float(prod_price):.2f} | Total: ₱{float(total_price):.2f}"
                    )

    except FileNotFoundError:
        print("No purchases found.")


def main():
    print("===== Welcome to Spending Tracker =====")

    while True:
        product = input("\nEnter the product name: ")

        try:
            quantity = int(input("Enter the quantity: "))
            price = float(input("Enter the price of the product: "))
        except ValueError:
            print("Please enter valid numbers!")
            continue

        total = multiply_price(quantity, price)

        # Save purchase
        with open("spendlog.csv", "a") as file:
            file.write(f"{product},{quantity},{price},{total}\n")

        print(f"Purchase saved! Total Cost: ₱{total:.2f}")

        while True:
            user_input = input(
                "\n0 = Exit\n1 = Add Another Product\n2 = Show Purchases\nq = Quit\nChoice: "
            )

            if user_input == "0":
                print("Thank you for using Spending Tracker!")
                return

            elif user_input == "1":
                break

            elif user_input == "2":
                show_purchases()

            elif user_input.lower() == "q":
                quit()

            else:
                print("Invalid choice!")


main()
