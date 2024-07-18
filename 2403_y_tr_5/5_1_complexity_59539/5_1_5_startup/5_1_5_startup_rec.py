import sys
sys.setrecursionlimit(10000000)
sys.set_int_max_str_digits(100000)

test_f_name = 'input.txt'
f = open(test_f_name, 'r')
n, k, d = map(int, f.readline().split())

def dfs(cur_profit):
    if cur_profit >= over_profit:
        return -1
    for next_dig in range(10):
        next_prof = cur_profit + next_dig
        if next_prof % k == 0:
            if next_prof < profit_goal:
                return dfs(next_prof * 10)
            else:
                return next_prof
    return -1


if k == 0:
    print(-1)
else:
    profit_goal = n*10**d
    over_profit = profit_goal*10
    res = dfs(n*10)
    print(res)