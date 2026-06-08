# grocery_inventory to store information:
grocery_inventory = {
"Milk": (113, "Dairy"),
"Eggs": (116, "Dairy"),
"Bread": (117, "Bakery"),
"Apples": (141, "Produce") }

#milk_details = grocery_inventory.get("Milk")
#eggs_details = grocery_inventory.get("Eggs")
bread_details = grocery_inventory.get("Bread")
#apples_details = grocery_inventory.get("Apples")


#print(f"Milk Details: {milk_details}")
#print(f"Eggs Details: {eggs_details}")
print(f"Details of Bread: {bread_details}")
#print(f"Apples Details: {apples_details}")

grocery_inventory.update({"Cookies": (143, "Bakery")})
cookies_details = grocery_inventory.get("Cookies")

print("Inventory after adding Cookies:", grocery_inventory)

# Remove Eggs from the inventory
removed_item = grocery_inventory.pop("Eggs")
print("Inventory after removing Eggs:", grocery_inventory)
