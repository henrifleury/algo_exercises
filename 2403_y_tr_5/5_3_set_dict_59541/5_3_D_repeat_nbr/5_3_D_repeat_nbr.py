#работает для k==1
test_f_name = 'input.txt'
f = open(test_f_name, 'r')

#txt_file = f.readlines()
#n = int(f.readline())
n, k = list(map(int, f.readline().split()))
nbrs = list(map(int, f.readline().split()))

def check_repeats():
    init_id = min(n, k+1)
    k_set = set(nbrs[:init_id])
    if len(k_set)<init_id:
        return "YES"
    for r_idx in range(k+1, n):
        l_idx = r_idx - k -1
        l = nbrs[l_idx]
        #k_set = k_set -set([l])
        k_set.remove(l)
        #k_set = \
        k_set.add(nbrs[r_idx])
        #print(l_idx, r_idx, k_set, len(k_set))
        if len(k_set) < k+1:
            return "YES"
    return "NO"

def check_repeats1():
    init_id = min(n, k+1)
    k_set = set(nbrs[:init_id])
    if len(k_set)<init_id:
        return "YES"
    for r_idx in range(k+1, n):
        l_idx = r_idx - k -1
        l = nbrs[l_idx]
        k_set = k_set -set([l])
        #k_set = \
        k_set.add(nbrs[r_idx])
        #print(l_idx, r_idx, k_set, len(k_set))
        if len(k_set) < k+1:
            return "YES"
    return "NO"


#import datetime
#start = datetime.datetime.now()
print(check_repeats())
#fin = datetime.datetime.now()
#print(fin-start)

'''
for i in range(n-k):
    print(i, i+k, len(set(nbrs[i:i+k])))
    #print()

i1,i2 = 12,22
print(nbrs[i1:i2])
print(set(nbrs[i1:i2]))
print(len(set(nbrs[i1:i2])))
'''