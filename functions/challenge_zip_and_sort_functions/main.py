# List of product names
products = ["Banana", "Apple", "Mango", "Cherry"]

# List of product prices
prices = [1.20, 0.50, 2.50, 1.75]

# List of quantity sold
quantities_sold = [50, 100, 25, 40]

# Zip 3 Lists in the 1 List of 3 tuples
# [(products),(prices),(quantities_sold)]

combined_list = list(zip(products, prices, quantities_sold))
sorted_products = sorted(combined_list)
print(sorted_products)