with open("input.txt", "r") as f:
    cl_nbr = f.readline().split()
    power_l = list(map(int, f.readline().split()))
    mod_nbr = f.readline().split()
    price_d = dict()
    for line in f.readlines():
        power, price = map(int, line.split())
        price_d[power] = price_d.get(power,price)
        if price_d[power]>price:
            price_d[power] = price
#print(price_d)

def get_best_price_noob(powers: list, pow_prices: dict):
    if len(price_d)==1:
        return len(power_l)*list(pow_prices.values())[0]

    powers = sorted(power_l)
    pow_prices = dict(sorted(pow_prices.items()))

    sorted_pow = list(pow_prices.keys())
    prev_price = pow_prices[sorted_pow[-1]]

    for idx in range(len(sorted_pow)-2, -1,-1):
        checked_price = pow_prices[sorted_pow[idx]]
        if checked_price >= prev_price:
            del pow_prices[sorted_pow[idx]]
        else:
            prev_price = checked_price

    sorted_pow = list(pow_prices.keys())
    last_price_id = 0
    order_sum = 0
    for pow in powers:
        while sorted_pow[last_price_id] < pow:
            last_price_id+=1
        order_sum += pow_prices[sorted_pow[last_price_id]]
    #print(order_sum)
    return order_sum

print(get_best_price_noob(power_l, price_d))