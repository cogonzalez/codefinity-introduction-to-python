# List of product prices
product_prices = [1.50, 2.50, 3.00, 0.99, 2.30]

def apply_discount(any_price_list):
    prices_copy = any_price_list.copy()
    # print(prices_copy)
    # Use a for loop with index iteration (range(len(prices_copy))) to go through the copied list.
    # 'price' arbituary variable to iterate from 0 to length of list (5), which is 0 to 4
    for index in range(len(prices_copy)):
        # If a price is greater than 2.00, apply a 10% discount
        # print(f"{index}")
        if prices_copy[index] > 2.00:
            prices_copy[index] = prices_copy[index]*0.9
    return prices_copy

# Call the function and store the updated prices
updated_prices = apply_discount(product_prices)
print(f"Updated product prices: ${updated_prices}")
