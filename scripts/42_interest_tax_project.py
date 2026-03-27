def calculate_interest(principal, rate, time):
    simple = (principal * rate * time) / 100
    compound = principal * ((1 + rate/100) ** time - 1)
    return simple, compound


def calculate_tax(income):
    if income < 50000:
        return income * 0.05
    elif income < 100000:
        return income * 0.1
    else:
        return income * 0.2


def main():
    print("=== Finance Calculator ===")

    principal = float(input("Enter principal: "))
    rate = float(input("Enter rate: "))
    time = float(input("Enter time: "))
    income = float(input("Enter income: "))

    simple, compound = calculate_interest(principal, rate, time)
    tax = calculate_tax(income)

    print("\n--- Results ---")
    print("Simple Interest:", simple)
    print("Compound Interest:", compound)
    print("Tax:", tax)


main()
