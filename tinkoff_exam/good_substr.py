#len_s, s = int(input()), input()
good_syms = set(["a", "b", "c", "d"])
len_good_syms = len(good_syms)


def is_good(s):
    return len(set(s)) == len_good_syms

def get_max_ss_len(s):
    if not is_good(s):
        return -1

    freqs = []
    for sym in good_syms:
        freqs.append((s.count(sym), sym))
    rare_sym_n, rare_sym = sorted(freqs)[0]
    other_syms = good_syms-set([rare_sym])
    #print(sorted(freqs), rare_sym_n, rare_sym, other_syms)
    start_ind=0
    max_sym_distances=[]
    for ind in range(rare_sym_n):
        next_rare_ind = s.find(rare_sym, start_ind)
        #print(s[next_rare_ind:])
        seek_right = True if next_rare_ind+1 < len(s) else False
        seek_left = True if next_rare_ind > 0 else False
        min_s_dist = []
        for other_s in other_syms:
            if seek_right:
                # ищем вправо
                next_other_s = s.find(other_s, next_rare_ind)
                if next_other_s > 0:
                    min_s_dist.append(next_other_s-next_rare_ind)
                else:
                    seek_right = False
            if seek_left:
                prev_other_s = s.rfind(other_s, 0, next_rare_ind)
                if prev_other_s >= 0:
                    min_s_dist.append(next_rare_ind - prev_other_s)
                else:
                    seek_left = False

            #print(other_s, seek_right, seek_left, min_s_dist)
        start_ind = next_rare_ind+1
        max_sym_distances.append(max(min_s_dist))
    #print('max_sym_distances', min(max_sym_distances), max_sym_distances)
    return min(max_sym_distances)+1

#print(get_max_ss_len(s))

len_s, s  = 12, "aabbccddbadd"
#print(s)
assert get_max_ss_len(s) == 5

s = "aaaabbbbccccdddd"
assert get_max_ss_len(s) == 10

s = "dbbccca"
#print(s)
#get_max_ss_len(s)
assert get_max_ss_len(s) == 7

s = "abcabac"
assert get_max_ss_len(s) == -1
