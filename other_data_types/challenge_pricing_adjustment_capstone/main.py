#1.
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

#2. Update Eggs price 
if grocery_inventory["Eggs"][1] > 5:
    print("Eggs are too expensive, reducing the price by $1.")
    #reduce the egg price by $1.
    grocery_inventory["Eggs"] = (
        grocery_inventory["Eggs"][0],
        grocery_inventory["Eggs"][1] - 1,
        grocery_inventory["Eggs"][2])
    #print(grocery_inventory)
else:
    #otherwise print 
    print("The price of Eggs is reasonable.")
# *********************************

#3. Update inventory with Tomatoes
grocery_inventory.update({"Tomatoes": ("Produce", 1.20, 30)})
print(f"Inventory after adding Tomatoes: {grocery_inventory}")


#4. check and restock Milk
if grocery_inventory["Milk"][2] < 10:
    # restock milk add 20 units, but you have to recreate this entire item in the dictionary 
    # as this value is a tuple and tuples are immutable
    print("Milk needs to be restocked. Increasing stock by 20 units.")
    grocery_inventory["Milk"] = (grocery_inventory["Milk"][0],
                                 grocery_inventory["Milk"][1],
                                 grocery_inventory["Milk"][2]+20)
else:
    print("Milk has sufficient stock.")

#5. Checks the price of Apples and if it exceeds $2.00 then remove it using pop
if grocery_inventory["Apples"][1]>2:
    grocery_inventory.pop("Apples")
    print("Apples removed from inventory due to high price.")

#6. Final inventory
print(f"Updated inventory: {grocery_inventory}")    


