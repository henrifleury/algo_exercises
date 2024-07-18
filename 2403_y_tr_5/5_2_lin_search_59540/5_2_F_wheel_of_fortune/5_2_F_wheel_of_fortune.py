#работает для k==1
test_f_name = 'input.txt'
f = open(test_f_name, 'r')

#txt_file = f.readlines()
n = int(f.readline())
score = list(map(int, f.readline().split()))
a, b, k = list(map(int, f.readline().split()))

def calc_max_res_k_1():
    min_sect_p = a//k -1
    max_sect_p = min(b//k, n + min_sect_p)
    #print(min_sect_p, max_sect_p, max_sect_p%n)
    base, rest = divmod(max_sect_p, n)
    #print(base, rest)
    if base>0 and rest >= min_sect_p:
        return(max(score))
    else:
        if base > 0:
            if rest <= 0:
                l = min(min_sect_p, n-max_sect_p)
                r = max(max_sect_p, n-min_sect_p)
                #print('rest <= 0', l, r)
                return max(score[l:r])
            else:
                l = max(rest, n - min_sect_p)
                r = max(l, min(min_sect_p, n-rest))
                #print('rest >', l, r)
                return max(score[:l]+score[r:])
        else:
            if rest >= n+k-1//k:
                return max(score[min_sect_p:n-min_sect_p])
            else:
                return max(score[min_sect_p:max_sect_p] + score[n-max_sect_p:n-min_sect_p])

def calc_max_res():
    res = score[a // k % n]
    for i in range(a, b+1, k):
        idx = (i-1) // k % n
        if score[idx] > res: res = score[idx]
        idx = -((i-1)//k % n)
        if score[idx] > res: res = score[idx]

    return res

if k==1:
    print(calc_max_res_k_1())
else:
    print(calc_max_res())
