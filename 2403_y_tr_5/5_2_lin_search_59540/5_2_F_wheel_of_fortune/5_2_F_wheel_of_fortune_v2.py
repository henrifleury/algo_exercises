#работает для k==1
test_f_name = 'input.txt'
f = open(test_f_name, 'r')

#txt_file = f.readlines()
n = int(f.readline())
score = list(map(int, f.readline().split()))
a, b, k = list(map(int, f.readline().split()))

def calc_max_res():
    res = score[a // k % n]
    for i in range(a, b+1, k):
        idx = (i-1) // k % n
        if score[idx] > res: res = score[idx]
        idx = -((i-1)//k % n)
        if score[idx] > res: res = score[idx]

    return res

print(calc_max_res())
