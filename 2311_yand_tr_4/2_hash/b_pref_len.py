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

def isequal(slen, from1, from2):
    #print(slen, from1, from2)
    #print(s[from1:from1+slen], s[from2:from2+slen])
    return ((h[from1+slen-1] + h[from2 - 1]*x[slen]) % p ==
            (h[from2+slen-1] + h[from1 - 1]*x[slen]) % p)

#len_s длина исходной строки без пробела в начале
len_corr = len_s+1

min_pref_len = len_s
for len_pref in range(1, len_s):
    if isequal(len_pref, 1, len_corr-len_pref):
        #print("isequal", len_pref)
        min_pref_len = len_s-len_pref
print(min_pref_len)
