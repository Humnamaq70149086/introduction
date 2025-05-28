marks = float(input("Enter marks: "))
if marks < 0 or marks > 100:
    print("Invalid marks! Please enter a value between 0 and 100.")
elif marks >= 95:
    print("Grade: A")
elif marks >= 85:
    print("Grade: B")
elif marks >= 75:
    print("Grade: C")
elif marks >= 65:
    print("Grade: D")
else:
    print("Grade: F")
   