import csv 
def find_topper(filename): 
    try: 
        with open(filename, mode='r') as file: 
            reader = csv.DictReader(file) 
            topper = None 
            highest_cgpa = -1.0 
            for row in reader: 
                try: 
                    cgpa = float(row['CGPA']) 
                    if cgpa > highest_cgpa: 
                        highest_cgpa = cgpa 
                        topper = row 
                except ValueError: 
                    print(f"Invalid CGPA value found: {row['CGPA']}") 
            if topper: 
                print("Topper of the class:") 
                print("USN : {topper['USN']}") 
                print("Name : {topper['Name']}") 
                print("CGPA : {topper['CGPA']}") 
            else: 
                print("No valid data found") 
    except FileNotFoundError: 
        print(f"File'{filename}'; not found") 
    except KeyError as e: 
        print(f"Missing expected column: {e}") 
# Call the function 
find_topper(r"D:\BMSIT&M\AIML_Dept\2025-26\Python\studData.csv") 