#len_arr = int(input())
#arr = list(map(int, input().split()))

len_arr = 3
arr = [[2, 0], [0, 2], [2, 2]]

def get_back_tort(arr):
    #back_t_nbr = dict()
    total_t = len(arr)
    true_answ = set()
    for t_n, (t_back, t_fwd) in enumerate(arr):
        if t_back >= 0 & t_fwd >= 0:
            if t_back < total_t:
                if t_back+t_fwd == total_t-1:
                    true_answ.add((t_back, t_fwd))
    return len(true_answ)

print(get_back_tort(arr))