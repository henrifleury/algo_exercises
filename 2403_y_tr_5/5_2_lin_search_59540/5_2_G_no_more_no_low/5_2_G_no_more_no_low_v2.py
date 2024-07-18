from collections import Counter

#работает для k==1
test_f_name = 'input.txt'
f = open(test_f_name, 'r')

#txt_file = f.readlines()
t = int(f.readline())
def get_best_cut(arr):#, min_el):
    #counter = Counter(arr)
    #counter = {k :counter[k] for k in sorted(counter.keys())}
    #print(arr, counter)

    rest = len(arr)
    min_seg_nbr=0

    while rest>0:
        for k, v in pos_counter.items():
            #print(k,v)
            if k*v > rest:
                rest -= (rest+k-1)//k * v
                min_seg_nbr += (rest+k-1)//k

            else:
                min_seg_nbr += v
                rest -= k * v


    print('min_seg_nbr', min_seg_nbr)


def cut_by_min(arr, l_p, r_p):
    #print('enter arr, l_p, r_p', arr[l_p:r_p], l_p, r_p, r_p-l_p)

    if l_p>=r_p:
        #print('l_p, r_p', l_p, r_p)
        return [(l_p, r_p)]
    min_el = min(arr[l_p:r_p])
    #cur_len = r_p-l_p
    if r_p-l_p <= min_el:
        #print('l_p, r_p, cur_len <= min_el', l_p, r_p)
        return [(l_p, r_p)]
    res = []
    idx_prev = l_p
    for idx in range(l_p, r_p):
        el = arr[idx]
        if el == min_el:
            if idx - idx_prev+1 <= min_el:
                #print(idx, 'idx - idx_prev+1 <= min_el')
                res.append((idx_prev, idx_prev + min_el))
                #res += cut_by_min(arr, idx_prev + min_el, cur_len)
                res += cut_by_min(arr, idx_prev + min_el, r_p)
                break
            else:
                if idx+el >= r_p:
                    #print(idx, 'idx+el >= cur_len')
                    res += cut_by_min(arr, idx_prev, r_p - el)
                    res.append((r_p - el, r_p))
                else:
                    #print(idx, 'idx+el < cur_len')
                    #должен быть перебор. пока так
                    res += cut_by_min(arr, idx_prev, idx)
                    res.append((idx, idx+el))
                    res += cut_by_min(arr, idx+el, r_p)
                break
    #print('l_p, r_p, res', l_p, r_p, res)
    return res

def cut_by_one(arr):
    #if min(arr) > 1:
        #return
    res=[]
    for idx, el in enumerate(arr):
        if el == 1:
            res.append((idx, idx+1))
    return res



def cut():
    res_l = []
    for i in range(t):
        res = []
        n = int(f.readline())
        arr = list(map(int, f.readline().split()))
        counter = Counter(arr)
        counter = {k :counter[k] for k in sorted(counter.keys())}
        #min_seg_nbr = 0
        seg = []
        for k in counter.keys():
            if k == 1:
                seg = cut_by_one(arr)
            break
        if seg:
            prev_id = seg[0][0]
            for ones in seg:
                res += cut_by_min(arr, prev_id, ones[0])
                res += [ones]
                prev_id = ones[1]
            if prev_id < n:
                res += cut_by_min(arr, prev_id, n)
        else:
            res += cut_by_min(arr, 0, len(arr))
        #print('res', res)
        res_l.append(res)
        #break
    return res_l

res_l = cut()
for res in res_l:
    res = [(l, r) for (l,r) in res if r-l>0]
    print(len(res))
    for (l, r) in res:
        print(r-l, end = " ")
    print()