

def check_price(price, mini_price, maxi_price):
    if price < mini_price:
        return mini_price
    elif price > maxi_price:
        return maxi_price
    else:
        return price