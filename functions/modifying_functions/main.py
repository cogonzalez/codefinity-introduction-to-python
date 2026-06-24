# Function where `discount` and `tax` has a default value
def calculate_total(price, discount=0.05, tax=0.07):
    total_tax = apply_tax(price, tax)
    total = apply_discount(total_tax,discount)
    return total

def apply_tax(price, tax=0.07):
    total_tax = price*(1+tax)
    return total_tax

def apply_discount(price, discount=0.05):
    total_disc = price*(1-discount)
    return total_disc

total_price_default = calculate_total(120)
total_price_custom = calculate_total(100,discount=0.10,tax=0.08)
print(f"Total cost with default discount and tax: ${total_price_default}")
print(f"Total cost with custom discount and tax: ${total_price_custom}")
    