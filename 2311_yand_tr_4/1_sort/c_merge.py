from random import randint

f = open('input.txt', 'r')
n = int(f.readline())
arr_a = list(map(int, f.readline().split()))
#print(n, arr_a)
m = int(f.readline())
arr_b = list(map(int, f.readline().split()))


def merge_sort(arr_1, arr_2):
    if n==0: return arr_2
    if m==0: return arr_1
    idx_1, idx_2 = 0, 0
    res = []
    while True:
        if arr_1[idx_1] > arr_2[idx_2]:
            res.append(arr_2[idx_2])
            idx_2 += 1
            if idx_2 >= m:
                return res+arr_1[idx_1:]
        else:
            res.append(arr_1[idx_1])
            idx_1 += 1
            if idx_1 >= n:
                return res+arr_2[idx_2:]


#res =
print(" ".join(str(v) for v in merge_sort(arr_a, arr_b)))