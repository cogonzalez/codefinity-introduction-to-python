# List of products, their prices, and the quantities sold
products = ["Bread", "Apples", "Oranges", "Bananas"] # product names
prices = [0.50, 1.20, 2.50, 2.00]  # price per item
quantities_sold = [150, 200, 100, 50]  # number of items sold


# Define calculate revenue function and returns revenue
def calculate_revenue(price, qty_sold):
    revenue = []
    for i in range(len(price)):
        revenue.append(price[i]*qty_sold[i])
    return revenue

# Define formatted output
def formatted_output(revenues):
    for name, rev in sorted(revenues):
        print(f"{name} has total revenue of ${rev}")


# CALL functions
calcuated_rev = calculate_revenue(prices,quantities_sold)

# Use the zip() function to combine the products list and the 
# revenue list into a list of tuples named revenue_per_product
revenue_per_product = list(zip(products, calcuated_rev))
#**************
print(revenue_per_product)

# CALL function
formatted_output(revenue_per_product)
