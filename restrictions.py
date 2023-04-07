
def limit_price(price, min_price, max_price):
    if price < min_price:
        return min_price
    elif price > max_price:
        return max_price
    else:
        return price