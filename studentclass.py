# Student Score Card Program 
 
class Student: 
     
    # Constructor 
    def __init__(self, name, usn): 
        self.name = name 
        self.usn = usn 
        self.marks = [] 
        self.total = 0 
        self.percentage = 0 
        self.grade = "" 
 
    # Method to get marks 
    def getMarks(self): 
        for i in range(3): 
            while True: 
                mark = float(input(f"Enter marks for subject {i+1}: ")) 
                if 0 <= mark <= 100: 
                    self.marks.append(mark) 
                    break 
                else: 
                    print("Marks should be between 0 and 100.") 
         
        self.total = sum(self.marks) 
        self.percentage = self.total / 3 
        self.calculateGrade() 
 
    # Method to calculate grade 
    def calculateGrade(self): 
        if self.percentage >= 90: 
            self.grade = "A+" 
        elif self.percentage >= 80: 
 
  
            self.grade = "A" 
        elif self.percentage >= 70: 
            self.grade = "B" 
        elif self.percentage >= 60: 
            self.grade = "C" 
        elif self.percentage >= 50: 
            self.grade = "D" 
        else: 
            self.grade = "F" 
 
    # Method to display score card 
    def display(self): 
        print("\n------ SCORE CARD ------") 
        print("Name       :", self.name) 
        print("USN        :", self.usn) 
        print("Marks      :", self.marks) 
        print("Total      :", self.total) 
        print("Percentage :", round(self.percentage, 2), "%") 
        print("Grade      :", self.grade) 
 
        if self.grade == "F": 
            print("Result     : FAIL") 
        else: 
            print("Result     : PASS") 
 
# Main Program 
name = input("Enter Student Name: ") 
usn = input("Enter USN: ") 
 
s1 = Student(name, usn) 
s1.getMarks() 
s1.display() 
 