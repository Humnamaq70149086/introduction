student_marks = [90, 80, 65, 50, 85, 72, 95, 58]
for marks in student_marks:
        if marks >= 85:
            category = "Excellent"
        elif marks >= 75:
            category = "Good"
        elif marks >= 60:
            category = "Satisfactory"
        else:
            category = "Needs Improvement"

        # Print the classification for each student inside the loop
        print(f"Student with marks {marks}: {category}")

