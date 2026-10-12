# Shopping Mall Billing Program 
 
print("Welcome to Shopping Mall") 
 
num_items = int(input("Enter number of items you want to buy: ")) 
 
prices = [] 
total = 0 
 
# Input prices using loop 
for i in range(num_items): 
    price = float(input(f"Enter price of item {i+1}: Rs. ")) 
    prices.append(price) 
    total += price 
 
# Calculate discount 
discount = 0 
if total > 100: 
    discount = total * 0.10   # 10% discount 
 
final_total = total - discount 
 
# Display Itemized Receipt 
print("\n----------- RECEIPT -----------") 
for i in range(num_items): 
    print(f"Item {i+1}: Rs. {prices[i]:.2f}") 
 
print("--------------------------------") 
print(f"Total Amount      : Rs. {total:.2f}") 
print(f"Discount (10%)    : Rs. {discount:.2f}") 
print(f"Final Amount Payable: Rs. {final_total:.2f}") 
print("--------------------------------") 
print("Thank you for shopping with us!") 