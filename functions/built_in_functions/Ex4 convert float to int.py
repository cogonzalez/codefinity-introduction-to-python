price = 3.99
quantity = "4"

# Calculate the total cost
total_cost = int(quantity) * price
# which is 15.96
print(f"The total cost for {quantity} items is ${total_cost}")
print(f"Converting the total cost to an integer results in ${int(total_cost)}")
# converting to int results in 15, after converting to int() type (it essentially truncates)
