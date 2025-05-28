balance = 6000
amount = float(input("Enter withdrawal amount: "))
if amount <= 0:
    print("Invalid amount! Please enter a positive value.")
elif amount > balance:
    print("Insufficient funds! Your balance is $", balance)
else:
    balance -= amount
    print(f"Withdrawal successful! Remaining balance: ${balance:.2f}")
    