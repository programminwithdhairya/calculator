# Calculator program in Python 

print("Enter 1 for +")
print("Enter 2 for -")
print("Enter 3 for *")
print("Enter 4 for /")
print("Enter 5 for **")

try:
    operator = int(input("Enter a Number"))
    num_1 = int(input("Enter the First Number"))
    num_2 = int(input("Enter the Second Number"))

    if operator == 1:
        print(f"{num_1} + {num_2} is {num_1 + num_2}")

    elif operator == 2:
        print(f"{num_1} - {num_2} is {num_1 - num_2}")

    elif operator == 3:
        print(f"{num_1} * {num_2} is {num_1 * num_2}")

    elif operator == 4:
        print(f"{num_1} / {num_2} is {num_1 / num_2}")

    elif operator == 5:
        print(f'{num_1} ** {num_2} is {num_1 ** num_2}')

except Exception as e:
    print("Enter a correct Value")
