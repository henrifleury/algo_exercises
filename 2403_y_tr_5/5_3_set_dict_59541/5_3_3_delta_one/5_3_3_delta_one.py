#работает для k==1
test_f_name = 'input.txt'
f = open(test_f_name, 'r')

#txt_file = f.readlines()
n = int(f.readline())
nbrs = list(map(int, f.readline().split()))

from collections import Counter

nbr_counter = Counter(nbrs)
k_sorted = sorted(nbr_counter.keys())
nbr_counter = {k: nbr_counter[k] for k in k_sorted}
#print(nbr_counter, len(nbr_counter))
prev_k = k_sorted[0]
max_delta = nbr_counter[prev_k]
if len(nbr_counter)>1:

    #for k,v in nbr_counter.items():
    for k in k_sorted[1:]:
        if abs(k - prev_k)<=1:
            if nbr_counter[k] + nbr_counter[prev_k] > max_delta:
                #print(k, prev_k, v, nbr_counter[prev_k], max_delta)
                max_delta = nbr_counter[k] + nbr_counter[prev_k]
        prev_k = k

#else:
    #print(0)
print(n-max_delta)
