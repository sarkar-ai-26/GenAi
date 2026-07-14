#Method that returns discounted price
def apply_discount(price,percent):
    return price - (price*(percent/100))

#return flat discount price
def flat_discount(price):
    return price - 50

