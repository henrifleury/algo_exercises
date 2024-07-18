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
    print(arr, l_p, r_p)
    if l_p>=r_p:
        return (l_p, r_p)
    res = []
    min_el = min(arr[l_p:r_p])
    cur_len = r_p-l_p
    if cur_len <= min_el:
        return ((0, cur_len))

    idx_prev = l_p
    for idx in range(l_p, r_p):
        el = arr[idx]
        if el == min_el:
            if idx - idx_prev < min_el:
                res.append((idx_prev, idx_prev + min_el))
                #res.append(cut_by_min(arr[idx_prev:idx_prev + min_el]))
                res.append(cut_by_min(arr, idx_prev, idx_prev + min_el))
            else:
                if idx+el >= cur_len:
                    res.append((cur_len-el, cur_len))
                    res.append(cut_by_min(arr, idx_prev, cur_len-el))
                else:
                    #должен быть перебор. пока так
                    res.append((idx, idx+el))
                    res.append(cut_by_min(arr, idx_prev,idx))
                    res.append(cut_by_min(arr,idx+el,cur_len))
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
    res = []
    for i in range(t):
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
            #print('seg', seg, len(arr))
            prev_id = seg[0][0]
            for ones in seg:
                #print('ones', ones, arr[ones])
                res.append(cut_by_min(arr, prev_id, ones[0]))
                res.append(ones)
                #res.append(cut_by_min(arr, ones[0], ones[1]))
                prev_id = ones[1]
            print(arr[prev_id: -1])
        else:
            res += [ cut_by_min(arr, 0, len(arr))]
        print('res', res)
        break

        '''
        rest = len(arr)

        while rest > 0:
            for k, v in counter.items():
                if k * v > rest:
                    rest -= (rest + k - 1) // k * v
                    min_seg_nbr += (rest + k - 1) // k

                else:
                    min_seg_nbr += v
                    rest -= k * v

        #res.append(get_best_cut(arr))#, min_el))
        # break
        '''

print(cut())
