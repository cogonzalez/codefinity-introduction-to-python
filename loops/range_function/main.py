# List of products on promotion for each weekday
daily_promotions = ["Milk", "Eggs", "Bread", "Apples", "Oranges"]

# List of weekdays corresponding to the promotions
weekdays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]

# for day arbritrary variable in range(0,7,1)
for day in range(7)
    # Access the corresponding weekday
    weekday = weekdays[day]
    # Access teh corresponding daily promotion
    promotion = daily_promotions[day]
    print(f"{weekday}: Promotion on {promotion}")