# List of products, their prices, and the quantities sold
products = ["Bread", "Apples", "Oranges", "Bananas"] # product names
prices = [0.50, 1.20, 2.50, 2.00]  # price per item
quantities_sold = [150, 200, 100, 50]  # number of items sold
revenue = [0,0,0,0]

# Define calculate revenue function and returns revenue
def calculate_revenue(price, qty_sold,rev):
    for i in range(len(price)):
        rev[i] = price[i]*qty_sold[i]
    return rev

# CALL functions
calcuated_rev = calculate_revenue(prices,quantities_sold,revenue)

# Use the zip() function to combine the products list and the 
# revenue list into a list of tuples named revenue_per_product
revenue_per_product = list(zip(products, calcuated_rev))
#print(revenue_per_product)

def formatted_output(revenues):
    revenues = sorted(revenues)
    for i in range(len(revenues)):
        print(f"{products[i]} has total revenue of ${revenues[i]}")
    return revenues

# CALL function
formatted_output(revenue_per_product)
