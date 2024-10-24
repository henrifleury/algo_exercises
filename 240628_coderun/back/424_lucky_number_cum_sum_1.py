# https://coderun.yandex.ru/seasons/2024-summer/tracks/backend/problem/lucky-number
#import sys
#sys.set_int_max_str_digits(10**100000)
import time


INPUT_F = 'input.txt'

'''
def get_dig_list(n_int_or_str: [int, str], dig_len):
    half_len = dig_len // 2
    digits = []
    if type(n_int_or_str)==str:
        digits = [int(s) for s in n_int_or_str]
    else:
        while n_int_or_str>0:
            n_int_or_str, reminder = divmod(n_int_or_str, 10)
            digits = [reminder] + digits
    digits = [0] * (dig_len - len(digits)) + digits
    start_half_l = digits[:half_len]
    end_half_l = digits[half_len:]
    return start_half_l, end_half_l
'''
def get_int_from_list(dig_l):
    len_l = len(dig_l)
    res = 0
    for i in range(len_l):
        res += dig_l[i]*10**(len_l-1-i)
    return res
def get_halfs_from_str(x_str: str):
    dig_len = len(x_str)
    half_len = dig_len // 2
    high_str = x_str[:half_len]
    low_str = x_str[half_len:]
    high_l = [int(s) for s in high_str]
    low_l = [int(s) for s in low_str]

    high_n = get_int_from_list(high_l)
    low_n = get_int_from_list(low_l)

    max_half = 10**half_len-1
    max_hi = max_half * 10 ** half_len
    max_full = max_hi + max_half
    full_n = high_n * 10 ** half_len + low_n
    return dig_len, half_len, high_str, low_str, full_n, high_n, low_n, high_l, low_l, max_half, max_hi, max_full

def get_str_from_list(dig_list, half_len):
    return ''.join([str(i) for i in dig_list]).zfill(half_len)

# def check_borders(start_half, end_half):
def is_borders(half_len, x, max_half, max_hi, max_full):
    if x <= max_half:
        return (True, str(1).zfill(half_len) + str(1).zfill(half_len))
    if x >= max_hi:
        if x == max_full:
            return (True, str(1).zfill(half_len) + str(1).zfill(half_len))
        else:
            return (True, str(max_full))
    return (False,)

def is_998(half_len, high_x, low_x, max_half):
    # 998 можно проверить отдельно так как ищем след число и след будет 999
    # тогда можно не делать второй раз is_border
    if low_x >= max_half-1:
        if high_x <= low_x:
            return (True, '9'*half_len*2)
    return (False,)

def get_cum_sums(x: int, half_len):
    cum_sums = [0]
    #for s in str(x):
        #cum_sums.append(cum_sums[-1]+int(s))
    #while x>0:
        #x, reminder = divmod(x, 10)
    #cum_sums.append(cum_sums[-1] + reminder)
    x_l = get_list_from_int(x, half_len)
    for i in x_l:
        cum_sums.append(cum_sums[-1] + i)

    cum_sums = cum_sums[1:]
    #return cum_sums+[cum_sums[-1]]*(half_len-len(cum_sums))
    return [0]*(half_len-len(cum_sums)) + cum_sums

def get_list_from_int(x: int, half_len):
    #res = [int(s) for s in str(x)]
    res = []
    while x>0:
        x, reminder = divmod(x, 10)
        res = [reminder] + res
    return [0]*(half_len-len(res)) + res


def get_halfs_from_int(x, half_len, max_half, max_hi, max_full):
    high_n = x // (max_half+1)
    low_n = x - high_n*10**half_len
    return high_n, low_n, get_list_from_int(high_n, half_len), get_list_from_int(low_n, half_len), get_cum_sums(high_n, half_len), get_cum_sums(low_n, half_len)

def calck_with_min_eq_str(x_hi, half_len):
    hi_str = str(x_hi)
    '''
    dig_dict = {k: 0 for k in '0123456789'}
    for k in hi_str:
        dig_dict[k] = dig_dict[k]+1
    lo_str = ''
    for k in '123456789':
        lo_str += k*dig_dict[k]
    '''
    cum_sum = 0
    for i in hi_str:
        cum_sum += int(i)
    n_9, reminder = divmod(cum_sum, 9)
    lo_str = str(reminder)+'9'*n_9
    return hi_str.zfill(half_len)+lo_str.zfill(half_len)

def main(x_str: str) -> str:
    stamp_len, half_len, high_str, low_str, x, high_n, low_n, high_l, low_l, max_half, max_hi, max_full = get_halfs_from_str(x_str)
    # проверка что текущее число не на грнаицах - все девятки или все нули в одной из половин
    res_check = is_borders(half_len, x, max_half, max_hi, max_full)
    if res_check[0]:
        return res_check[1]
    #if (high_n == max_half - 1) and (low_n == max_half - 1):
        #return str(max_full)
    res_check = is_998(half_len, high_n, low_n, max_half)
    if res_check[0]:
        return res_check[1]

    # нас интересует СЛЕДУЮЩЕЕ счастливое число, добавляем 1 и снова проверяем границы
    x_1 = x + 1
    # снова проверка для нового числа, кажется можно оптимизировать
    # res_check = is_borders(half_len, x_1, max_half, max_hi, max_full)
    if res_check[0]:
        return res_check[1]

    #high_str, low_str, high_n, low_n, high_l, low_l
    high_n, low_n, high_l, low_l, high_cum_sums, lo_cum_sums = get_halfs_from_int(x_1, half_len, max_half, max_hi, max_full)

    # если суммы чисел равны то на этом можно закончить
    if high_cum_sums == lo_cum_sums:
        return get_str_from_list(high_l, half_len)+get_str_from_list(low_l, half_len)

    # если сумма чисел в левой половине больше чем в правой то это нормальный вариант
    # а если не больше то нужно привести к номальному
    lo_best_sum_dig = lo_cum_sums[-1]
    if high_cum_sums[-1] < lo_cum_sums[-1]:
        best_i = -1
        for best_i in range(half_len-1)[::-1]:
            dig = low_l[best_i]
            if dig < 9:
                lo_best_sum_dig = lo_cum_sums[best_i]+1
                if high_cum_sums[-1] >= lo_best_sum_dig:
                    break
        if best_i == 0:
            if high_cum_sums[-1] < lo_best_sum_dig:
                best_i = -1
        if best_i == -1:
            high_n +=1
            return calck_with_min_eq_str(high_n, half_len)
        else:
            low_l[best_i] += 1
            # снова нужно проверить
            if lo_best_sum_dig == high_cum_sums[-1]:
                low_l = low_l[:best_i+1]
                low_l += (half_len-len(low_l))*[0]
                return get_str_from_list(high_l, half_len) + get_str_from_list(low_l, half_len)
            else:
                low_l = low_l[:best_i+1]
                low_l += (half_len-len(low_l))*[0]
                # здесь можно нужное количество ра

    last_dig_reserved = 9 - low_l[-1]
    rest = high_cum_sums[-1] - lo_best_sum_dig
    if rest <= last_dig_reserved:
        low_l[-1] += rest
        return get_str_from_list(high_l, half_len) + get_str_from_list(low_l, half_len)
    cur_id = -2
    cur_adds = 9 - low_l[cur_id]
    while rest > last_dig_reserved + cur_adds:
        rest -= cur_adds
        low_l[cur_id] = 9
        cur_id -= 1
        cur_adds = 9 - low_l[cur_id]
    if last_dig_reserved >= rest:
        low_l[-1] += rest
    else:
        low_l[-1] += last_dig_reserved
        low_l[cur_id] += rest - last_dig_reserved

    return get_str_from_list(high_l, half_len) + get_str_from_list(low_l, half_len)


start_time = time.time()  # время начала выполнения

if __name__ == '__main__':
    f = open(INPUT_F, 'r')
    x_str: str = f.readline().strip()
    #res = main(x_str)

    half_len = len(x_str) // 2
    x=0
    #for i in range(half_len):
        #x += int(x_str[i]) *10 ** (half_len-i-1)

    #_ = get_cum_sums(int(x_str), half_len)
    end_time = time.time()  # время окончания выполнения
    #print(res)


execution_time = end_time - start_time  # вычисляем время выполнения

print(f"Время выполнения программы: {execution_time} секунд")

# 99998
# 998998

assert main('00') == '11'
assert main('0000') == '0101'
assert main('9999') == '0101'
assert main('9997') == '9999'
assert main('0001') == '0101'
assert main('003001') == '003003'
assert main('90300001') == '90300039'
assert main('00300033') == '00300102'
assert main('47059694') == '47059700'
assert main('08357857') == '08357900'
assert main('08357857') == '08357900'
assert main('20013063') == '20020004'

# 4349393
#

def main_dumb(s: str):
    #s = str(x)
    dig_nbr = len(s)
    half_dig_nbr = dig_nbr // 2

    num_9 = 9
    for i in range(1, half_dig_nbr):
        num_9 = num_9*10+9

    start_dig = int(s[:half_dig_nbr])
    end_dig = int(s[half_dig_nbr:])

    if start_dig == 0:
        return str(1).zfill(half_dig_nbr)+str(1).zfill(half_dig_nbr)

    # если задано число из девяток то след будет 0
    if start_dig == num_9:
        if end_dig < num_9:
            return str(num_9)+str(num_9)

        #return ''.jo0101in('0'*dig_nbr)
        return str(1).zfill(half_dig_nbr) + str(1).zfill(half_dig_nbr)

    while True:
        start_dig_sum = sum([int(sym) for sym in str(start_dig)])
        end_sum = 0
        for i in range(end_dig+1, num_9+1):
            end_sum = sum([int(s) for s in str(i)])
            if start_dig_sum == end_sum:
                break
        if start_dig_sum == end_sum:
            if start_dig_sum == 0:
                return str(1).zfill(half_dig_nbr) + str(1).zfill(half_dig_nbr)
            break
        start_dig += 1
        # такого быть не может по всем 9 должен выскочить if start_dig > num_9:
        end_dig = 0




    return str(start_dig).zfill(half_dig_nbr)+str(i).zfill(half_dig_nbr)

# 02130123 02128398 02130006

'''
import random
N_DIG = 8
for x in range(10**N_DIG):
    if x%100000 == 0:
        print(x)
    x_str = str(x).zfill(N_DIG)
    main_str = main(x_str)
    main_dumb_str = main_dumb(x_str)
    if  main_str != main_dumb_str:
        print('error', main_str, x, main_dumb_str)
        #break


while True:
    x = random.randint(3, 10**N_DIG)
    x_str = str(x).zfill(N_DIG)
    main_str = main(x_str)
    main_dumb_str = main_dumb(x_str)
    if  main_str != main_dumb_str:
        print(main_str, x, main_dumb_str)
        break
'''