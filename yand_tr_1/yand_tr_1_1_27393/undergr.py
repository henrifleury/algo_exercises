#t1, t2, n1, n2 = map(int, input().split())
inp_lst = []
for i in range(4):
    inp_lst.append(int(input()))
t1, t2, n1, n2 = inp_lst

verbose = False

def my_print(*args):
    if verbose:
        print(*args)

def get_time(t1, t2, n1, n2):

    def get_min_max_t(t, n, st_time=1):
        return t*(n-1) + st_time*n, t * (n + 1) + st_time * n

    min_time1, max_time1 = get_min_max_t(t1, n1)
    min_time2, max_time2 = get_min_max_t(t2, n2)

    my_print(min_time1, max_time1, min_time2, max_time2)
    if (min_time1 > max_time2) or (min_time2 > max_time1):
        #return -1
        print("-1")
        return

    #return max(min_time1, min_time2), min(max_time1, max_time2)
    print(max(min_time1, min_time2), min(max_time1, max_time2))

get_time(t1, t2, n1, n2)

assert get_time(1, 3, 3, 2) == (5, 7)
assert get_time(1, 5, 1, 2) == -1
#assert get_time(1, 3, 3, 2) == (5, 7)