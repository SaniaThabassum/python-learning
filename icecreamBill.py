# Ice Cream Parlour Billing System 
 
# Menu 
menu = { 
    "Vanilla": 50, 
    "Chocolate": 60, 
    "Strawberry": 55, 
    "Butterscotch": 65 
} 
 
total = 0 
orders = [] 
 
print("----- Ice Cream Menu -----") 
for item, price in menu.items(): 
    print(f"{item} : Rs. {price}") 
 
# Ordering loop 
while True: 
    order = input("\nEnter ice cream name: ").title() 
 
    if order in menu: 
        total += menu[order] 
        orders.append(order) 
        print(order, "added to bill.") 
    else: 
        print("Item not available.") 
 
    more = input("Do you want to order more? (yes/no): ").lower() 
    if more != "yes": 
        break 
 
# Calculate tax (8%) 
tax = total * 0.08 
final_bill = total + tax 
 
# Print Receipt 
print("\n------ RECEIPT ------") 
for item in orders: 
    print(f"{item} : Rs. {menu[item]:.2f}") 
 
print("---------------------") 
print(f"Subtotal : Rs. {total:.2f}") 
 
  
print(f"Tax (8%) : Rs. {tax:.2f}") 
print(f"Final Bill : Rs. {final_bill:.2f}") 
print("---------------------") 
print("Thank you! Visit Again ")