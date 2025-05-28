temperature = float(input("Enter the temperature in Celsius: "))
if temperature < 0:
    print("It's freezing! Wear a coat.")
elif temperature < 15:
    print("It's cold! Wear a warm jacket.")
elif temperature < 25:
    print("It's cool! A light sweater is recommended.")
elif temperature < 35:
    print("It's warm! Wear a t-shirt and shorts.")