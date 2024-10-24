# https://coderun.yandex.ru/seasons/2024-summer/tracks/backend/problem/tiles?currentPage=1&pageSize=50&search=

INPUT_F = 'input.txt'

def get_res(sku_arr):
    dig_d = dict()
    pair_nbr = 0
    if len(dig_d) < len(sku_arr):
        for sku in sku_arr:
            sku = ''.join(sorted(sku))
            #sku = {s for s in sku}
            if sku in dig_d:
                pair_nbr += dig_d[sku]
                dig_d[sku] += 1
            else:
                dig_d[sku] = 1
    #if pair_nbr == 1: pair_nbr = 0
    if len(dig_d) == 1:
        return sum(i for i in range(len(sku_arr)))
    dig_keys = list(dig_d.keys())
    #print(dig_d)
    for k in dig_keys:
        cur = dig_d[k]
        del dig_d[k]
        #print(k, )
        # плохой нейминг это не sku
        for sku in dig_d:
            for s in sku:
                if s in k:
                    pair_nbr += cur * dig_d[sku]
                    #print(k, sku, s, 'pair_nbr', pair_nbr)
                    break
            print(k, 'sku, pair_nbr',sku, pair_nbr)
    #if pair_nbr >= len(sku_arr):
        #return len(sku_arr)-1

    return pair_nbr

def main(f_name = INPUT_F):
    f = open(f_name, 'r')
    sku_nbr = int(f.readline())
    #sku_arr = map(int, f.readline().split())
    #sku_arr = set(f.readline().split())
    sku_arr = f.readline().split()

    return get_res(sku_arr)



if __name__ == '__main__':
    res = main()
    print(res)

'''
def get_res_dumb(sku_arr):
    pass
    return
    return pair_nbr
'''
assert get_res('123 321'.split()) == 1
assert get_res('123 321 223'.split()) == 3
assert get_res('123 321 213'.split()) == 3
assert get_res('103 123 20 4567'.split()) == 3
