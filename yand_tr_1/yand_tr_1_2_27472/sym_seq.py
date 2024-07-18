def get_sym_seq(arr):
    def is_sym(arr, id_dec, id_inc):
        while id_inc<len(arr):
            if arr[id_dec]!=arr[id_inc]:
                return False
            id_dec -= 1
            id_inc += 1
        return True

    if len(arr)<1:
        return []
    if len(arr) < 2:
        return arr*2
    even_len = len(arr)%2
    half_idx = len(arr)//2 + even_len-1 # -1 тк индекс начинается с 0
    for center in range(half_idx, len(arr)-1):
        if not even_len:
            if is_sym(arr, center, center+1):
                even_len = 0
                break
            if is_sym(arr, center, center+2):
                even_len = 1
                center += 1
                break
        else:
            if is_sym(arr, center-1, center+1):
                even_len = 1
                break
            if is_sym(arr, center, center+1):
                even_len = 0
                break
        even_len = (even_len + 1) % 2
    else:
        even_len = (even_len + 1) % 2
        center+=1
        # print(odd_len)
    #even_len = (even_len + 1) % 2
    center = center + 1-even_len # смещение для правильного среза
    #print(arr, "center", center, arr[:center], even_len)
    len_sym_seq = center*2 + even_len
    tail_len = len_sym_seq - len(arr)
    tail = arr[:tail_len][::-1]
    #print(len_sym_seq, tail_len, tail)
    return tail

'''len_arr = int(input())
arr = list(map(int, input().split()))


tail = get_sym_seq(arr)
if not tail:
    print(0)
else:
    print(len(tail))
    print(" ".join(tail))
'''
arr = list(map(int, "1 2 1 2 2".split()))
#print(get_sym_seq(arr))
assert get_sym_seq(arr) == list(map(int, "1 2 1".split()))
arr = list(map(int, "1 2 3 4 5 4 3 2 1".split()))
assert get_sym_seq(arr) == []
arr = list(map(int, "1 2 3 4 5".split()))
assert get_sym_seq(arr) == list(map(int, "4 3 2 1".split()))
arr = list(map(int, "1 2 3 4 5 6 7 6 5".split()))
assert get_sym_seq(arr) == list(map(int, "4 3 2 1".split()))
arr = list(map(int, "1 2 3 3 2 1".split()))
assert get_sym_seq(arr) == []
arr = list(map(int, "1 2".split()))
assert get_sym_seq(arr) == [1]
arr = list(map(int, "1 2 2 2 2".split()))
assert get_sym_seq(arr) == [1]
arr = list(map(int, "1 2 2 2".split()))
assert get_sym_seq(arr) == [1]
arr = list(map(int, "1 2 2".split()))
assert get_sym_seq(arr) == [1]
arr = list(map(int, "1 2 2 3".split()))
assert get_sym_seq(arr) == [2, 2, 1]
arr = list(map(int, "2 2 2 2 2".split()))
assert get_sym_seq(arr) == []
arr = list(map(int, "2".split()))
print(get_sym_seq(arr))
