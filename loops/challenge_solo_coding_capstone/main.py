# Inventory dictionary with stock, price, and discount price
inventory = {
    "Bread": [42, 1.20, 0.99],  # "Item": [current stock, regular price, discounted price]
    "Eggs": [225, 2.12, 1.99],  # Eggs should be sold at a discount
    "Apples": [9, 1.50, 1.35]   # Apples need to be restocked
}

restocking_threshold = 30 #If stock is below 30, print that it needs restocking and that it should be sold at the regular price.
                          # If stock is 30 to 100, print that it should be sold at the regular price.
discount_threshold = 100  #If stock is above 100, print that it should be sold at the discounted price.

for item, data in inventory.items():
    current_stock, regular_price, discounted_price = data
    print(f"Processing {item} ...")
    print(f"{item}: {data}")
    if current_stock < restocking_threshold:
        print(f"{item} need restocking.")
    elif current_stock > discount_threshold:
        print(f"{item} should be sold at the discounted price of {discounted_price}.")
    elif current_stock >= restocking_threshold and current_stock <= discount_threshold:
        print(f"{item} should be sold at the regular price of {regular_price}.")




        
    


