# Lists of items and categories for slicing
items = "Bubblegum, Chocolate, Pasta"
categories = "Candy Aisle, Pasta Aisle"

candy1 = items[0:9]
candy2 = items[11:20]
dry_goods = items[22:]

category1 = categories[0:11]
category2 = categories[13:]
bubblegum_price = 1.50
chocolate_price = 2.00
pasta_price = 5.40

print(candy1,candy2,dry_goods)
print(category1, category2)

message1 = f"We have {candy1} for ${bubblegum_price:.2f} in the {category1}"
message2 = f"We have {candy2} for ${chocolate_price:.2f} in the {category1}"
message3 = f"We have {dry_goods} for ${pasta_price:.2f} in the {category2}"

print(message1)
print(message2)
print(message3)


