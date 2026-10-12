# Student Grade Tracker 
 
students = [] 
 
n = int(input("Enter number of students: ")) 
 
if n <= 0: 
    print("Number of students must be greater than 0") 
else: 
    for i in range(n): 
        name = input("Enter student name: ") 
         
        while True: 
            try: 
                marks = float(input("Enter marks: ")) 
                if 0 <= marks <= 100: 
                    break 
                else: 
                    print("Marks should be between 0 and 100") 
            except ValueError: 
                print("Please enter valid numeric marks.") 
         
 
  
        students.append((name, marks))   # storing as tuple 
 
    # Display all students 
    print("\n----- Student Details -----") 
    for name, marks in students: 
        print(f"Name: {name}  |  Marks: {marks}") 
 
    # Calculate average 
    total = sum(marks for name, marks in students) 
    average = total / n 
    print("\nAverage Marks:", round(average, 2)) 
 
    # Find topper 
    topper = max(students, key=lambda x: x[1]) 
    print("Topper:", topper[0], "with marks", topper[1]) 