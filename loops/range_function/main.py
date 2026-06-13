# List of products on promotion for each weekday
daily_promotions = ["Milk", "Eggs", "Bread", "Apples", "Oranges"]

# List of weekdays corresponding to the promotions
weekdays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]

# for day arbritrary variable in range(0,5,1) 
# there are 5 elements in these list at positions 0, 1, 2, 3, 4
# remember five days in list chose 5
for day in range(5):
    # Access the corresponding weekday
    weekday = weekdays[day]
    # Access the corresponding daily promotion
    promotion = daily_promotions[day]
    print(f"{weekday}: Promotion on {promotion}")
    