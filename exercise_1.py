
# Read two integer values
first_number = int(input("Enter the first number: "))
second_number = int(input("Enter the second number: "))

# Compare and print the appropriate message
if first_number < second_number:
    print("First number is less than the second")
elif second_number < first_number:
    print("Second number is less than the first")
else:
    print("The numbers are equal")
