# Create a program that takes in user weight in KGs and
# prints it out in Pounds on the screen

weight_in_kilogram: float = float(input("Enter you weight in kg: "))
weight_in_pounds: float = weight_in_kilogram * 2.204623
print(f"Your weight in pounds is: {weight_in_pounds} lbs")
