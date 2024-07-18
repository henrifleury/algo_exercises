test_f_name = 'input.txt'

import sys
from math import log10
sys.setrecursionlimit(10000000)
sys.set_int_max_str_digits(1000000)

f = open(test_f_name, 'r')
n, k, d = map(int, f.readline().split())

def dfs(cur_profit):
    if int(log10(cur_profit)) >= profit_len:
        return -1
    for next_dig in range(10):
        next_prof = cur_profit + next_dig
        if next_prof % k == 0:
            return next_prof
    return -1


if k == 0:
    print(-1)
else:
    profit_len = int(log10(n))+1 + d
    #over_profit_len = profit_len + 1
    res = dfs(n*10)
    if res>0:
        res_len = int(log10(res))+1
        res = res * 10 ** (profit_len-res_len)
    print(res)
