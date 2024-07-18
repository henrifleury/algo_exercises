'''n = int(input())
arr = list(map(int, input().split()))
x = int(input())'''

def get_nearest(arr, x):
    nearest = arr[0]
    min_delta = abs(x - nearest)
    for el in arr:
        cur_delta = abs(x - el)
        if cur_delta < min_delta:
            min_delta = cur_delta
            nearest = el
        if min_delta==0:
            break
    return nearest

print(get_nearest(arr, x))

assert get_nearest([1, 2, 3, 4, 5], 6) == 5
assert get_nearest([1, 2, 3, 4, 5], 3) == 3