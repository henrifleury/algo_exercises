with open("input.txt", "r") as f:
    n, k = list(map(int, f.readline().strip().split()))
    #card_lst = list(map(int, f.readline().strip().split()))
    inp_str = f.readline().strip()

str_len = len(inp_str)
sym_dict = dict()
right_idx = -1
breaker_nbr = 0
max_good_str_len = 0
max_good_str_start = 0
for left_idx, left_sym in enumerate(inp_str):
    while (right_idx < str_len-1) & (breaker_nbr <= k):
        right_idx += 1
        cur_sym = inp_str[right_idx]
        sym_dict[cur_sym] = sym_dict.get(cur_sym, 0) + 1
        if sym_dict[cur_sym] > breaker_nbr:
            #print(sym_dict, sym_dict[cur_sym])
            breaker_nbr = sym_dict[cur_sym]
            breaker = cur_sym

        print(left_idx, right_idx, right_idx - left_idx)
        if right_idx - left_idx + 1 > max_good_str_len:
            max_good_str_len = right_idx - left_idx
            max_good_str_start = left_idx
            print(left_idx, left_sym, right_idx, max_good_str_len)
        #if breaker_nbr == k:
    sym_dict[left_sym] -= 1

print(max_good_str_len, max_good_str_start+1)