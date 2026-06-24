# User defined functions that returns a value 'total'
def calculate_total_cost(price, quantity):
    total = price*quantity
    return total
    


# Call the function and print the result
apples_total_cost = calculate_total_cost(1.50, 10)
# the userdefined function returns the value 'total' and assigns
# the variable apples_total_cost

print(f"The total cost for apples is ${apples_total_cost}")