age = int(input("Enter your age: "))
if age < 0:
    print("Invalid age! Please enter a valid number.")
elif age <= 10:
    print("Ticket price: $8")
elif age <= 20:
    print("Ticket price: $10")
elif age <= 55:
    print("Ticket price: $12")
else:
    print("Ticket price: $7")
