# create a simple calculator

num_one: float = float(input("Enter first number: "))
num_two: float = float(input("Enter second number: "))

print("Operations:")
print("1. +")
print("2. -")
print("3. *")
print("4. /")
operator: str = input("Enter operation to use: ")

match operator:
    case "1":
        print(f"{num_one} + {num_two} = {num_one + num_two}")
    case "2":
        print(f"{num_one} - {num_two} = {num_one - num_two}")
    case "3":
        print(f"{num_one} * {num_two} = {num_one * num_two}")
    case "4":
        print(f"{num_one} / {num_two} = {num_one / num_two}")
    case _:
        print("Invalid operator")


# if operator == "1":
#     print(f"{num_one} + {num_two} = {num_one + num_two}")
# elif operator == "2":
#     print(f"{num_one} - {num_two} = {num_one - num_two}")
# elif operator == "3":
#     print(f"{num_one} * {num_two} = {num_one * num_two}")
# elif operator == "4":
#     print(f"{num_one} / {num_two} = {num_one / num_two}")
# else:
#     print("Invalid operator")
