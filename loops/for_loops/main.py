prices = [12.99, 8.50, 15.75, 23.00, 7.25]

# Write your code here
# total is a variable initially set to zero then its value gets add to each iteration
total = 0

# item_price is an arbitrary variable prices is our list
for item_price in prices:
    total = total + item_price
# final grand total
print(f"Final Total: {total:0.2f}")