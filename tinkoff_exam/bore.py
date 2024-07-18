#len_arr = int(input())
#arr = list(map(int, input().split()))


verbose = False

def my_print(*args):
    if verbose:
        print(*args)

def get_max_boring_l(arr):
    my_print(arr)
    freq_d = {el: arr.count(el) for el in set(arr)}
    my_print(freq_d)


    '''
    freq_sym_nbr_d = dict()
    for freq in freq_d:
        freq_sym_nbr_d[freq] = freq_sym_nbr_d.get(freq, 0)+1
    my_print('freq_sym_nbr_d', freq_sym_nbr_d)
    '''
    freq_uniq_l = (sorted(set(freq_d.values())))
    my_print(freq_uniq_l)

    max_l=[]
    for _, l in enumerate(freq_uniq_l[:-1]):
    #for l in freq_uniq_l:
        good_freq_flags = [1 for v in freq_d.values() if v >= l]
        n_fr = sum(good_freq_flags)
        my_print('l', l, "n_fr",n_fr)
        #max_l.append((n_fr+1)*l+1)
        max_l.append(n_fr * l + 1) if l>1 else max_l.append(n_fr * l)
    l = freq_uniq_l[-1]
    n_fr = sum(v for v in freq_d.values() if v == l)
    if l == 1:
        max_l.append(n_fr)
    else:
        max_l.append(n_fr - 1)
    my_print("max(max_l), max_l", max(max_l), max_l)
    return max(max_l)



arr = list(map(int, "1 2 3 1 2 2 3 3 3 1 4 4 5 1 2 1 2 1 2 1 2 1 2".split()))
#print(arr)
assert get_max_boring_l(arr) == 15

arr = list(map(int, "1 2 3 1 2 2 3 3 3 1 4 4 5".split()))
#print(arr)
assert get_max_boring_l(arr) == 10

arr = list(map(int, "1 2 4 2 3 1 3 9 15 23".split()))
#print(arr)
assert get_max_boring_l(arr) == 7

arr = list(map(int, "1 2 3 4 5".split()))
assert get_max_boring_l(arr)== 5

arr = list(map(int, "1 2 3 4 5 1 2 3 4 5".split()))
assert get_max_boring_l(arr) == 9
