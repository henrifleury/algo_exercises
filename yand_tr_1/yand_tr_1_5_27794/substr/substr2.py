with open("input.txt", "r") as f:
    n, k = list(map(int, f.readline().strip().split()))
    # card_lst = list(map(int, f.readline().strip().split()))
    inp_str = f.readline().strip()

sym_dict = dict()
right_idx = 0
most_freq_sym = inp_str[0]
most_freq = 1
sym_dict[most_freq_sym] = 1
max_good_str_len = 1
max_good_str_start = 0

for left_idx, left_sym in enumerate(inp_str):
    # длина строки  = n, max индекс питон  = n-1
    while (right_idx < n-1) and (most_freq <= k):
        right_idx += 1
        cur_sym = inp_str[right_idx]
        sym_dict[cur_sym] = sym_dict.get(cur_sym, 0) + 1
        if sym_dict[cur_sym] > most_freq:
            most_freq_sym = cur_sym
            most_freq = sym_dict[cur_sym]
    #print(right_idx, left_idx, right_idx - left_idx > max_good_str_len)
    if right_idx-left_idx+1 > max_good_str_len:
        max_good_str_len = right_idx-left_idx+1
        max_good_str_start = left_idx
    if right_idx == n-1:
        break
    cur_sym = inp_str[left_idx]
    sym_dict[cur_sym] -= 1
    if cur_sym == most_freq_sym:
        most_freq -= 1

if most_freq > k: #случай когда последний символ в строке стал лишним
    max_good_str_len -= 1
print(max_good_str_len, max_good_str_start+1)