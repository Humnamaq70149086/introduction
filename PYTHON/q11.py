limit= int(input("Enter the upper limit to check for prime numbers:"))
for num in range(2,limit + 1):
    is_prime = True
    for i in range(2, num):
        if num % i == 0:
            is_prime = False
            break
        if is_prime:
            print(f"{num}is Prime")
        else:
            print(f"{num}is not Prime")
