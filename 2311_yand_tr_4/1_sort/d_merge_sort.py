f = open('input.txt', 'r')
n = int(f.readline())
arr_a = list(map(int, f.readline().split()))


def merge(arr_1, arr_2):
    len_1, len_2 = len(arr_1), len(arr_2)
    #if len_1 == 0:
        #return arr_2
    #if len_2 == 0:
        #]return arr_1

    #print("merge", len_1, arr_1, len_2, arr_2)
    idx_1, idx_2 = 0, 0
    res = []
    while True:
        if arr_1[idx_1] > arr_2[idx_2]:
            res.append(arr_2[idx_2])
            idx_2 += 1
            if idx_2 >= len_2:
                return res+arr_1[idx_1:]
        else:
            res.append(arr_1[idx_1])
            idx_1 += 1
            if idx_1 >= len_1:
                return res+arr_2[idx_2:]


def merge_sort(arr):
    arr_len = len(arr)
    #print(arr, arr_len)
    if arr_len >= 2:
        split_idx = arr_len//2
        #print("merge_sort", arr[:split_idx], arr[split_idx:])
        return merge(merge_sort(arr[:split_idx]), merge_sort(arr[split_idx:]))
    else:
        return arr


#print(merge_sort(arr_a))
print(" ".join(str(v) for v in merge_sort(arr_a)))