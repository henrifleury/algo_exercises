#работает для k==1
test_f_name = 'input.txt'
f = open(test_f_name, 'r')

#txt_file = f.readlines()
n = int(f.readline())
score = list(map(int, f.readline().split()))
a, b, k = list(map(int, f.readline().split()))

def calc_max_res_k_1():
    if b<=1:
        return score[0]

    min_p = a % n - 1
    max_p = min(b, n + min_p)
    #print(min_sect_p, max_sect_p, max_sect_p%n)
    base, rest = divmod(max_p, n)
    #print(base, rest)
    if base>0 and rest >= min_p:
        return(max(score))
    else:
        if b <=n:
            l = min(min_p, n-max_p)
            r = max(max_p, n-min_p)
            return max(score[l:r])
        else:
            l = max(max_p-n-1, n-min_p)
            r = min(min_p, 2*n-max_p)
            if l>=r:
                return (max(score))
            else:
                return (max(score[:l]+score[r:]))

def calc_max_res():
    res = score[a // k % n]
    res_set = set()
    #res_l = list()
    for i in range(a, b+1, k):
        idx = (i-1) // k % n
        if score[idx] > res: res = score[idx]
        res_set.add(idx)
        #res_l.append(idx)
        #print(i, idx, score[idx])
        idx = -((i-1)//k % n)
        #print(i, idx, score[idx])
        if score[idx] > res: res = score[idx]
        if len(res_set) == n:
            #print(i, 'len(res_set)', len(res_set), len(res_l))
            return res
    return res

if k==1:
    print(calc_max_res_k_1())
else:
    print(calc_max_res())
