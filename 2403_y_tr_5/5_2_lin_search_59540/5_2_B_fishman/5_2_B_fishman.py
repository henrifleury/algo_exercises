test_f_name = 'input.txt'
f = open(test_f_name, 'r')

n, k = list(map(int, f.readline().split()))
price_l = list(map(int, f.readline().split()))

def max_profit():
    if n==1 or k == 1:
        return 0
    res = 0
    for i in range(n):
        for j in range(i+1, min(i+k+1, n)):
            prof = price_l[j]-price_l[i]
            print(i, j, prof)
            if prof > res:
                res = prof
    return res
print(max_profit())