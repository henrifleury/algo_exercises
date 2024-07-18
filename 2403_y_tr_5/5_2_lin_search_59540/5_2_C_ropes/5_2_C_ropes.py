test_f_name = 'input.txt'
f = open(test_f_name, 'r')

#txt_file = f.readlines()
n = int(f.readline())
rest_ropes = list(map(int, f.readline().split()))

def get_min_rope(rest_ropes):
    max_len = rest_ropes[0]
    sum_len = max_len
    for rope in rest_ropes[1:]:
        sum_len += rope
        if rope > max_len:
            max_len = rope
    sum_len_no_max = sum_len - max_len
    #print(sum_len_no_max, max_len)
    if max_len > sum_len_no_max:
        return max_len - sum_len_no_max
    else:
        return sum_len

print(get_min_rope(rest_ropes))
