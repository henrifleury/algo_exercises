from math import atan2, pi
f = open('input.txt', 'r')
#x1, y1, x2, y2 = map(int, f.readline().split())
n = int(f.readline())
#for i in range(n)
rate_l = list(map(int, f.readline().split()))
#rate_l_sum = sum(rate_l)
#print(rate_l_sum)
res = sum(rate_l)
prev = 0
for id, rate in enumerate(rate_l):
    #res_l.append(rate_l_sum-n*rate)
    delta = rate - prev
    res = res + id*delta - (n-id)*delta
    print(res, end=" ")
    prev = rate
