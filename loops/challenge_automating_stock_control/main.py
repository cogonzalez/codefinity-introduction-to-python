# Initialize the inventory dictionary with stock details
inventory = {
    "Bread": [30, 50, 10, False],   # "Item": [current stock, minimum stock, restock quantity, on sale (True/False)]
    "Eggs": [120, 200, 40, False],
    "Milk": [60, 100, 20, False],
    "Apples": [15, 50, 15, False]
}

discount_threshold = 100
print("Processing started...")
for item, data in inventory.items():
    print(f"Processing {item}")
    current, minimum, restock_amount, on_sale = data
    # This while Loop updates the current stock with restock quantity until minimum is met.
    while current < minimum:
        current += restock_amount
        # print(current)
    # write the updated stock back into the dict
    # on 1st go round item = "Bread" and [0] references current stock
    inventory[item][0] = current
    if current > discount_threshold and not(inventory[item][3]):
        inventory[item][3] = True
print("Processing completed")