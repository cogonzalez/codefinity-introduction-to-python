# Dictionary of products with price and quantity sold as strings
products = {
    "Apple": ["1.20", "50"],   # "Item": [price, quantity sold]
    "Banana": ["0.50", "100"],
    "Cherry": ["2.50", "25"],
    "Mango": ["1.75", "40"]
}
total_sales_list = []
for product, data in products.items():
    price, quantity_sold = data
#    print(f"Processing {product} ...")
#    print(f"{product}: {data}")
    total_sales = float(price)*int(quantity_sold)
    total_sales_list.append(total_sales)
    print(f"Total sales for {product}: ${total_sales:0.2f} ")

total_sum = sum(total_sales_list)
min_sales = min(total_sales_list)
max_sales = max(total_sales_list)

print(f"Total sum of all sales: ${total_sum:0.2f} ")
print(f"Minimum sales: ${min_sales:0.2f} ")
print(f"Maximum sales: ${max_sales:0.2f} ")