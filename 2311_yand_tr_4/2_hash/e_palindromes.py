f = open('input.txt', 'r')
arr = f.readline().strip()

s0 = len(arr)
arr = "$".join(arr)

p = 10**9+7
x_ = 10
#x_ = 10
len_s = len(arr)
len_corr = len_s+2
h = [0]*(len_corr)
x = [0]*(len_corr)
x[0] = 1
arr = " " + arr + " "

for i in range(1, len_corr):
    #h[i] = (h[i - 1] * x_ + ord(s[i])) % p
    h[i] = (h[i-1] * x_ + ord(arr[i])) % p
    x[i] = (x[i-1] * x_) % p

#arr = arr[1:]

#arr_rev = arr[1:]
arr_rev = arr[::-1]
#print("arr_rev", arr_rev, len(arr_rev))
h_rev = [0]*(len_corr)
for i in range(1, len_corr):
    h_rev[i] = (h_rev[i - 1] * x_ + ord(arr_rev[i])) % p
#arr_rev = arr_rev[1:]


def get_hash(h_arr, slen, from1):
    #print(from1, from1 + slen)
    return (h_arr[from1 + slen-1] - h_arr[from1-1] * x[slen]) % p
"""
print("len(h_rev)", len(h_rev))
for i in range(1, len_corr-2):
    print(i, arr[i:i+2], get_hash(h, 2, i))
"""
"""
for i in range(2, len_corr-2,2):
    print(i, arr[i])
"""
for i in range(2, len_corr-2,2):
    l, r = 0, min(i, len_corr - i -1)
    while l<r:
        cur = (l+r)//2+1
        #print("str", i, cur, arr[i:i+cur], arr)
        #print(get_hash(h, cur, i))
        #print("rev", i, len_corr - i, l, cur, arr_rev[len_corr - i-1:len_corr-i-1+cur], arr_rev)
        #print(get_hash(h_rev, cur, len_corr - i-1))
        if get_hash(h, cur, i) == get_hash(h_rev, cur, len_corr - i-1):
            #print("l", i, cur, arr[i:i + cur], arr)
            #print("rev", i, len_corr - i-1, l, cur, arr_rev[len_corr - i-1:len_corr-i-1+cur], arr_rev)
            l = cur
        else:
            r = cur-1
    #print(l)
    s0 += l//2
#print("arr", arr, len_corr)
for i in range(3, len_corr-3,2):
    #print(i, arr[i])
    l, r = 0, min(i, len_corr - i -1)
    while l<r:
        cur = (l+r)//2+1
        #print("str", i, cur, arr[i:i+cur], arr)
        #print(get_hash(h, cur, i))
        #print("rev", i, len_corr - i, l, cur, arr_rev[len_corr - i-1:len_corr-i-1+cur], arr_rev)
        #print(get_hash(h_rev, cur, len_corr - i-1))
        if get_hash(h, cur, i) == get_hash(h_rev, cur, len_corr - i-1):
            #print("l", i, cur, arr[i:i + cur], arr)
            #print("rev", i, len_corr - i-1, l, cur, arr_rev[len_corr - i-1:len_corr-i-1+cur], arr_rev)
            l = cur
        else:
            r = cur-1
    #print(l)
    s0 += (l-1) // 2
print(s0)
"""
    while l<r:
        pal_len = (l+r)//2+1
        print(i, "pal_len", pal_len, arr[i], "arr", arr[i:i+pal_len+1], "arr_rev", arr_rev[len_s-i-1:len_s-i-1+pal_len+1])
        print(get_hash(h, pal_len, i))
        print(get_hash(h_rev, pal_len, len_s-i-1))
        break"""