meat = ["Ham", 3.99, 50, "Sliced"]
cheese = ["Cheddar", 5.49, 100, "Sharp"]
condiment = ["Mustard", 1.99, 75, "Spicy"]
deli_dept = [meat, cheese, condiment]

print(f"Initial Deli List: {deli_dept}")

#Restock Item: change meat quantity to 100
if "Ham" in meat and meat[2] < 100:
    # update its quantity to 100.
    meat[2]=100
else:
    print("meat not in list or is in list and more than 100")

#Add Seasonal Meat to meat:
seasonal_meat = ["Turkey", 4.50, 100, "Sliced"]
deli_dept.append(seasonal_meat)

#Remove Condiment from deli_dept:
deli_dept.remove(condiment)

#Sort List:
deli_dept.sort()

print(f"Updated Deli List: {deli_dept}")