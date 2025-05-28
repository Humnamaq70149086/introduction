import time
def countdown_timer():
    number = int(input("Enter the starting number for countdown: "))
    if number < 0:
        print("Please enter a non-negative number.")
        return
    while number >= 0:
        print(number)
        time.sleep(1)
        number -= 1
        print("Time's up!")

countdown_timer()