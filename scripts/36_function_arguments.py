def introduce(name, age=18):
    print(f"Name: {name}")
    print(f"Age: {age}")

introduce("John")
introduce("Emma", 22)

def add_numbers(*args):
    total = 0
    for num in args:
        total += num
    print("Total:", total)

add_numbers(1, 2, 3, 4)
