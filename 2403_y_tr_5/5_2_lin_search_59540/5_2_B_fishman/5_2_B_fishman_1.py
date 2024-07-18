test_f_name = 'input.txt'
f = open(test_f_name, 'r')

n, k = list(map(int, f.readline().split()))
price_l = list(map(int, f.readline().split()))

def max_profit():
    if n <= 1 or k <= 1:
        return 0
    res = 0
    for j in range(1, min(k + 1, n)):
        prof = price_l[j] - price_l[0]
        if prof > res:
            res = prof
    #print('start_res', res)
    for i in range(1, n-1):
        prof_i = res - price_l[i-1] + price_l[i]
        #print('prof_i', prof_i)
        prof_k = price_l[min(i+k, n-1)] - price_l[i]
        #@print('prof_k', prof_k)
        print(res, prof_i, prof_k)
        res = max(res, prof_i, prof_k)

    return res
print(max_profit())