products = ["apple", "banana", "cherry"]
prices = [0.99, 0.59, 2.99]
stock = [50, 100, 25]

# `zip()` combines the 3 lists into a series of tuples
# `list()` converts the zip object into a list
product_info = list(zip(products, prices, stock))

print("Product information:", product_info)