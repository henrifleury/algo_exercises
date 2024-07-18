# n,m,k = list(map(int, input().split()))
verbose = False

def my_print(*args):
    if verbose:
        print(*args)


def get_check_time(n, m, k):
    need_check = {jun_num:k for jun_num in range(n)}
    my_print(need_check)
    min_nbr=0
    cur_jun = 0
    while True:
        if max(need_check.values()) == 0:
            break
        for ind in range(m):
            if need_check[cur_jun] > 0:
                need_check[cur_jun] -= 1
            cur_jun += 1
            if cur_jun == n:
                cur_jun = 0
        min_nbr += 1
        my_print(min_nbr, need_check)
    return min_nbr
#print(get_check_time(n, m, k))

#print(get_check_time(3, 2, 2))
assert get_check_time(3, 2, 2) == 3
assert get_check_time(7, 3, 2) == 5