def calculator():
    print("=== Advanced Calculator ===")

    while True:
        print("\n1.Add 2.Sub 3.Mul 4.Div 5.Power 6.Exit")

        choice = input("Choose: ")

        if choice == "6":
            print("Exiting...")
            break

        if choice not in ["1","2","3","4","5"]:
            print("Invalid choice")
            continue

        try:
            a = float(input("Enter first number: "))
            b = float(input("Enter second number: "))
        except:
            print("Invalid input")
            continue

        if choice == "1":
            print("Result:", a + b)
        elif choice == "2":
            print("Result:", a - b)
        elif choice == "3":
            print("Result:", a * b)
        elif choice == "4":
            if b == 0:
                print("Cannot divide by zero")
            else:
                print("Result:", a / b)
        elif choice == "5":
            print("Result:", a ** b)

calculator()
