# CoffeeKutira Restaurant Bill Calculator 
# Using Functions and Loop 
 
def add_bill(): 
    food_cost = float(input("Enter food cost: ")) 
    tax = float(input("Enter tax amount: ")) 
    total = food_cost + tax 
    print("Total Bill Amount =", round(total, 2)) 
 
def subtract_discount(): 
    original_bill = float(input("Enter original bill amount: ")) 
    discounted_bill = float(input("Enter discounted bill amount: ")) 
    discount = original_bill - discounted_bill 
    print("Discount Amount =", round(discount, 2)) 
 
def multiply_orders(): 
    price_per_item = float(input("Enter price of one item: ")) 
    quantity = int(input("Enter quantity: ")) 
    total = price_per_item * quantity 
    print("Total Cost for Multiple Orders =", round(total, 2)) 
 
def divide_bill(): 
    total_bill = float(input("Enter total bill amount: ")) 
    customers = int(input("Enter number of customers: ")) 
     
    if customers > 0: 
        split_amount = total_bill / customers 
        print("Each Customer Should Pay =", round(split_amount, 2)) 
 
  
    else: 
        print("Number of customers must be greater than zero!") 
 
# Main Loop 
while True: 
    print("\n☕ Welcome to CoffeeKutira Restaurant Bill Calculator") 
    print("Choose an operation:") 
    print("a) Add - Calculate total bill (food cost + tax)") 
    print("b) Subtract - Calculate discount amount") 
    print("c) Multiply - Calculate total for multiple identical orders") 
    print("d) Divide - Split bill among customers") 
    print("e) Exit") 
 
    choice = input("Enter your choice (a/b/c/d/e): ") 
 
    if choice == 'a': 
        add_bill() 
    elif choice == 'b': 
        subtract_discount() 
    elif choice == 'c': 
        multiply_orders() 
    elif choice == 'd': 
        divide_bill() 
    elif choice == 'e': 
        print("Thank you for using CoffeeKutira Bill Calculator!") 
        break 
    else: 
        print("Invalid choice! Please select a, b, c, d, or e.") 