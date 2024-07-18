inp_list=[]
with open("input.txt", "r") as f:
    for line in f.readlines():
        inp_list.append(line.strip())
len_voc, reg_sense_f, first_dig_en_f = (inp_list[0].split())
len_voc = int(len_voc)
reg_sense_f = reg_sense_f == "yes"
first_dig_en_f = first_dig_en_f == "yes"


def is_number(w):
    res = True
    return res

kword_s = set()
for idx in range(1, len_voc+1):
    voc_word = inp_list[idx]
    if reg_sense_f:
        kword_s.add(voc_word)
    else:
        kword_s.add(voc_word.lower())

id_counter_d = dict()
most_freq_w = ""
max_freq = 0
for code_str in inp_list[len_voc+1:]:
    code_str_mod = ""
    for sym in code_str:
        if (sym.isalpha()) or (sym.isdigit()) or (sym == "_"):
            code_str_mod = code_str_mod + sym
        else:
            code_str_mod = code_str_mod + " "
    word_l = code_str_mod.strip().split()
    for w in word_l:
        if not w:
            continue
        if not reg_sense_f:
            w=w.lower()
        if w in kword_s:
            continue
        else:
            if not first_dig_en_f:
                if w[0].isdigit():
                    continue
            if w.isdigit():
                continue
            id_counter_d[w] = id_counter_d.get(w, 0) + 1
            if id_counter_d[w] > max_freq:
                max_freq = id_counter_d[w]
                most_freq_w = w
print(most_freq_w)



