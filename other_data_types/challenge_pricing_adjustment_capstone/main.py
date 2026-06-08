# Create the grocery_inventory dictionary
# Each value is a tuple of (category, price, stock).
# {"str",  ("str",      float, int  ) }
# {"Item_Name", ("category", price, stock) }

grocery_inventory = {
"Milk"  : ("Dairy", 3.50, 8),
"Eggs"  : ("Dairy", 5.50, 30),
"Bread" : ("Bakery", 2.99, 15),
"Apples": ("Produce", 1.50, 50),   
}

#print(grocery_inventory)
egg_details = grocery_inventory.get("Eggs")

# Update Eggs price — 
if egg_details[1] > 5:
    print("Eggs are too expensive, reducing the price by $1.")
    #reduce the egg price by $1.
    grocery_inventory["Eggs"] = (egg_details[0], egg_details[1] - 1, egg_details[2])
    #print(grocery_inventory)
else:
    #otherwise print 
    print("The price of Eggs is reasonable.")

