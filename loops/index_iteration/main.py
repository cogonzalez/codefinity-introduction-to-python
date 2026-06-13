prices = [29.99, 45.50, 12.75, 38.20]
disc_factor = [0.10, 0.20, 0.15, 0.05]

for i in range(len(prices)):
    disc = prices[i]*disc_factor[i]
    #print(f"Discount: {disc:0.2f}")
    prices[i] -= prices[i]*disc_factor[i] 
    #print(f"New Price: {prices[i]:0.2f}")

for i in range(len(prices)):
    print(f"Updated price for item {i+1}: ${prices[i]:0.2f}")


