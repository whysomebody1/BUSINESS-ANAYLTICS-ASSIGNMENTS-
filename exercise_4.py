
# Input salary
salary = float(input("Enter your salary: €"))

# Determine tax
if salary <= 10000:
    tax = 0
elif 10000 < salary <= 50000:
    tax = (salary - 10000) * 0.2
else:  # salary > 50000
    tax = 8000 + (salary - 50000) * 0.4

print(f"Your tax is: €{tax}")
