
# Prompt the user for a number
choice = int(input("Enter a number (1, 2, 3, or 4): "))

# Determine and print the corresponding suit
if choice == 1:
    print("diamonds")
elif choice == 2:
    print("hearts")
elif choice == 3:
    print("clubs")
elif choice == 4:
    print("spades")
else:
    print("Invalid input")
