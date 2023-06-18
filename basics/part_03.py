# taking user input

# input return input as a string
name: str = input("Enter your name: ")
# f string can directly interpolate values into the string by providing
# the values in curly brace inside string.
print(f"Hello {name}")
print(type(name))

# age: int = int(input("Enter your age: "))
# print(age)
# print(type(age))

num_one: int = int(input("Enter first number: "))
num_two: int = int(input("Enter second number: "))
print(f"{num_one} + {num_two} = {num_one + num_two}")
