test_f_name = 'input.txt'
f = open(test_f_name, 'r')

n, k = list(map(int, f.readline().split()))
price_l = list(map(int, f.readline().split()))


def max_profit(price_l):
    if n <= 1: #or k <= 1:
        return 0
    res = 0

    dif_l = [price_l[0]] + price_l# + k * [price_l[-1]]
    dif_l = [dif_l[i]-dif_l[i-1] for i in range(1,len(dif_l))]
    #print(dif_l, len(dif_l))

    for i in range(1, n-k+1):
        start_sum = dif_l[i]
        if start_sum > res:
            res = start_sum
        #print(i, 'start_sum', start_sum)
        for j in range(i+1, i+k):
            #print(j, dif_l[j])
            start_sum += dif_l[j]
            if start_sum > res:
                res = start_sum
        #print('res', res)


    for i in range(n-k+1, n):
        start_sum = dif_l[i]
        if start_sum > res:
            res = start_sum
        for j in range(i + 1, n):
            # print(j, dif_l[j])
            start_sum += dif_l[j]
            if start_sum > res:
                res = start_sum
        #print('res', res)

    return res

print(max_profit(price_l))