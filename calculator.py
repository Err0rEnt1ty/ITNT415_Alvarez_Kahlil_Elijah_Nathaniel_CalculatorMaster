# calculator.py

def display_menu():
    print("\n===== Calculator Master =====")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exit")
    print("==============================")


def get_numbers():
    while True:
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            return num1, num2
        except ValueError:
            print("Invalid input. Please enter numeric values only.")


def main():
    while True:
        display_menu()
        choice = input("Select an option (1-5): ").strip()

        if choice == "5":
            print("Exiting Calculator Master. Goodbye!")
            break
        elif choice not in ("1", "2", "3", "4"):
            print("Invalid choice. Please select a number between 1 and 5.")
            continue

        num1, num2 = get_numbers()

        if choice == "1":
            pass  # addition will be added on the addition branch
        elif choice == "2":
            pass  # subtraction will be added on the subtraction branch
        elif choice == "3":
            pass  # multiplication will be added on the multiplication branch
        elif choice == "4":
            pass  # division will be added on the division branch


if __name__ == "__main__":
    main()