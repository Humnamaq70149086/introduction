def atm_system():
    correct_pin = "6969"
    attempts = 4
    while attempts > 0:
        entered_pin = input("Enter your PIN: ")
        if entered_pin == correct_pin:
            print("Access granted. Welcome!")
            return
        else:
            attempts -= 1
            print(f"Incorrect PIN. You have {attempts} attempts left.")
            print("Too many incorrect attempts. Your account is locked.")

atm_system()