# https://coderun.yandex.ru/seasons/2024-summer/tracks/backend/problem/tiles?currentPage=1&pageSize=50&search=

INPUT_F = 'input_500000.txt'
INPUT_F = 'input.txt'
#ASSERTION_F = False
ASSERTION_F = True

def get_res(sku_arr):
    dig_d = dict()
    pair_nbr = 0
    if len(dig_d) < len(sku_arr):
        for sku in sku_arr:
            sku_digs = {int(s) for s in sku}
            sku_dig_arr = 0
            for dig in sku_digs:
                sku_dig_arr += 2 ** dig
            if sku_dig_arr in dig_d:
                pair_nbr += dig_d[sku_dig_arr]
                dig_d[sku_dig_arr] += 1
            else:
                dig_d[sku_dig_arr] = 1
            #print(sku, sku_dig_arr)
    if len(dig_d) == 1:
        return sum(i for i in range(len(sku_arr)))
    dig_keys = list(dig_d.keys())
    for k in dig_keys:
        cur = dig_d[k]
        del dig_d[k]
        for sku_digs in dig_d:
            if k&sku_digs:
                pair_nbr += cur * dig_d[sku_digs]
    return pair_nbr

def main(f_name = INPUT_F):
    f = open(f_name, 'r')
    sku_nbr = int(f.readline())
    sku_arr = f.readline().split()

    return get_res(sku_arr)

if __name__ == '__main__':
    res = main()
    print(res)

'''
import time
start_time = time.time()  # время начала выполнения
if __name__ == '__main__':
    res = main()
    print(res)
end_time = time.time()  # время окончания выполнения
execution_time = end_time - start_time  # вычисляем время выполнения
print(f"Время выполнения программы: {execution_time} секунд")

def generate_test_data(n=500000, f_name='input_500000.txt'):
    import random
    f = open(f_name, 'w')
    f.write(str(n)+'\n')
    for i in range(n):
        f.write(str(random.randint(1, 1000000000)) + ' ')
    f.write('\n')
    return
generate_test_data()
'''
if ASSERTION_F:
    assert get_res('123 321'.split()) == 1
    assert get_res('123 321 223'.split()) == 3
    assert get_res('123 321 213'.split()) == 3
    assert get_res('103 123 20 4567'.split()) == 3
