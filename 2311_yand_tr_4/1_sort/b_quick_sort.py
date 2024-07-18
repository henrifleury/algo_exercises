from random import randint

f = open('input1.txt', 'r')
n = int(f.readline())
arr = list(map(int, f.readline().split()))
# eq = int(f.readline())


def get_part(l_id, r_id):
    eq_id = l_id + randint(0, r_id-l_id-1)
    eq = arr[eq_id]
    # eq = 1
    # print("eq", eq, eq_id, l, r)
    eq_c, big_c = l_id, l_id
    for idx in range(l_id, r_id):
        el = arr[idx]
        # print(el)
        if el < eq:
            arr[idx] = arr[big_c]
            arr[big_c] = arr[eq_c]
            big_c += 1
            arr[eq_c] = el
            eq_c += 1
        elif arr[idx] == eq:
            arr[idx] = arr[big_c]
            arr[big_c] = eq
            big_c += 1
        # print(id, eq_c, arr, big_c)
    # return eq_c, big_c#, arr
    # if eq_c - 1 > 1: get_part(0, eq_c - 1)
    # print("eq", eq, eq_id, l, r)
    # return
    #print(eq_c)
    if eq_c - l_id > 1:
        #print("left", 0, eq_c)
        get_part(l_id, eq_c)
    if r_id-big_c > 1:
        #print("right", big_c, r_id)
        get_part(big_c, r_id)
    # if big_c<n: get_attr(0, eq_c - 1)
    return   # , arr
    # return get_part(arr, l, eq_c-1)+arr[eq_c:big_c]+get_part(arr, big_c, r)


if n > 1:
    get_part(0, n)
# [print(i, end=" ") for i in arr]
res = " ".join(str(v) for v in arr)
print("res")
print(res)
