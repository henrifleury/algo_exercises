f = open('input.txt', 'r')
s = f.readline().strip()

p = 10**9+7
x_ = 257
len_s = len(s)
h = [0]*(len_s+1)
x = [0]*(len_s+1)
x[0] = 1
s = " " + s

for i in range(1, len_s+1):
    h[i] = (h[i-1] * x_ + ord(s[i])) % p
    x[i] = (x[i-1] * x_) % p

#s, h, x = s[1:], h[1:], x[1:]

def isequal(slen, from1, from2):
    #print(slen, from1, from2)
    #print(s[from1:from1+slen], s[from2:from2+slen])
    return ((h[from1 + slen] + h[from2] * x[slen]) % p ==
            (h[from2 + slen] + h[from1] * x[slen]) % p)
    #return ((h[from1+slen-1] + h[from2 - 1]*x[slen]) % p ==
    #            (h[from2+slen-1] + h[from1 - 1]*x[slen]) % p)

s=s[1:]
#11 print(len_s)
z_arr = [0]
for suff_start_idx in range(1, len_s):
    l, r, len_pref = 0, len_s-suff_start_idx, 0
    #print(s[i:], len(s[i:]), len_s-i)
    while l<r:
        len_pref = (l+r)//2+1
        if isequal(len_pref, 0, suff_start_idx):
            l = len_pref
        else:
            r = len_pref -1
    z_arr.append(l)
#print(z_arr)
print(" ".join(str(i) for i in z_arr))
#j,[jlbv


"""
# len_s длина исходной строки без пробела в начале
len_corr = len_s+1
#print(len_s, len_corr)
#z_arr = [0]
z_arr = []
for i in range(1, len_s):
    #suff = s[i:]
    #max_pref_len = 0
    #for len_pref in range(i, 0, -1):
    l, r, len_pref = 1, i, 0
    while l < r :
        len_pref = (l+r) // 2
        #print(i, len_pref, len_corr - i)
        #print(s[1:1+len_pref], s[len_corr - i:len_corr - i + len_pref] )
        pref = s[1:1+len_pref]
        suff = s[len_corr - i+1:len_corr - i+1+len_pref]
        if isequal(len_pref, 1, len_corr - i+1):
            #print("isequal", s, len_pref, len_corr - len_pref)
            l = len_pref+1
        else:
            r = len_pref-1
    #max_pref_len = len_pref
    z_arr.append(l-1)
    #z_arr = [max_pref_len] + z_arr
    #break
print(" ".join(str(i) for i in [0]+z_arr[::-1]))"""