produce = ["Tomatoes", "Lettuce"]
dairy = ["Milk", "Cheese"]

# categories are called sections: produce, dairy
# items are each item in each section
groceries = [ produce, dairy]
#print(groceries)

for category in groceries:
    for item in category:
        print(f"Item name: {item}")

