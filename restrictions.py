
def limit_price(price, old_price, min_price, max_price):
    if (float(price) >= old_price * 0.4) and (float(price) <= old_price * 1.6) and (min_price < price < max_price):
        return price
    else:
        return old_price
    

