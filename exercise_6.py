
# Display menu
print("Welcome to the SimpleCalc")
print("Press 1 to add two numbers")
print("Press 2 to subtract two numbers")
print("Press 3 to divide two numbers")
print("Press 4 to multiply two numbers")

# Read the user's selection
selection = int(input("Enter your choice: "))

# Ask the user for two numbers
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

# Perform the selected operation
if selection == 1:
    result = num1 + num2
elif selection == 2:
    result = num1 - num2
elif selection == 3:
    result = num1 / num2
elif selection == 4:
    result = num1 * num2
else:
    print("Invalid selection")
    result = None

# Print the result
if result is not None:
    print(f"The result is: {result}")
