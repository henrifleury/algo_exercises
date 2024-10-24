# https://coderun.yandex.ru/seasons/2024-summer/tracks/backend/problem/tiles?currentPage=1&pageSize=50&search=

INPUT_F = 'input.txt'

def main(f_name = INPUT_F):
    f = open(f_name, 'r')
    sku_nbr = int(f.readline())
    prices = ['_'] + list(map(int, f.readline().split()))
    combo_pr = int(f.readline())
    combo = set(map(int, f.readline().split()))
    order_len = int(f.readline())
    order_d = dict()
    for sku in map(int, f.readline().split()):
        if sku in order_d:
            order_d[sku] += 1
        else:
            order_d[sku] = 1
    combo_sku_nbr_max = 0
    order_combo_s = set()
    for sku in order_d:
        if sku in combo:
            order_combo_s.add(sku)
            if order_d[sku] > combo_sku_nbr_max:
                combo_sku_nbr_max = order_d[sku]

    #print(combo_sku_nbr_max, order_d, order_combo)
    cur_order_price = 0
    for sku, q in order_d.items():
        cur_order_price += q*prices[sku]
    min_price = cur_order_price
    for i in range(1, combo_sku_nbr_max+1):
        for sku in order_combo_s:
            if order_d[sku] > 0:
                order_d[sku] -= 1
                cur_order_price -= prices[sku]
        cur_order_price += combo_pr
        if cur_order_price < min_price:
            if cur_order_price >0:
                min_price = cur_order_price

    return min_price



if __name__ == '__main__':
    res = main()
    print(res)