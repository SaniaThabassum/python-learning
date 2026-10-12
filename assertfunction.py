# Function definition 
def DivExp(a, b): 
    # Assertion for a > 0 
    assert a > 0, "Value of 'a' must be greater than 0" 
     
    # Raise exception if b = 0 
    if b == 0: 
        raise ZeroDivisionError("Division by zero is not allowed") 
     
    return a / b 
 
# Main program 
 
  
try: 
    a = float(input("Enter value of a: ")) 
    b = float(input("Enter value of b: ")) 
     
    result = DivExp(a, b) 
    print("Result (a/b) =", result) 
 
except ValueError: 
    print("Invalid input! Please enter numeric values.") 
 
except AssertionError as e: 
    print("Assertion Error:", e) 
 
except ZeroDivisionError as e: 
    print("Error:", e) 
 
except Exception as e: 
    print("Unexpected Error:", e) 