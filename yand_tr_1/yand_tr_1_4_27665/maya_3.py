'''len_w, len_seq = map(int, input())
w = input()
seq = input()
'''
w = "cAda"
#seq = "AbrAcadAbRa"
seq = "Acad"
len_w, len_seq = len(w), len(seq)
maya_w_counter = 0
if (len_w < 1) or (len_w > len_seq):
    pass
else:
    w_dict = dict()
    for sym in w:
        w_dict[sym] = w_dict.get(sym, 0) + 1

    sub_seq_d = dict()
    for sym in seq[:len_w]:
        sub_seq_d[sym] = sub_seq_d.get(sym, 0) + 1

    win_count=0
    for k in w_dict.keys():
        if w_dict[k] == sub_seq_d.get(k,0):
            win_count +=1
    if win_count==len_w:
        maya_w_counter+=1

    for idx_out, sym_out in enumerate(seq[:len_seq-len_w]):
        sym_in = seq[idx_out+len_w]
        sub_seq_d[sym_in] = sub_seq_d.get(sym_in, 0) + 1

        sym_in_w_count = w_dict.get(sym_in, 0)
        if sym_in_w_count:
            if sym_in_w_count==sub_seq_d[sym_in]:
                win_count += 1
            else:
                win_count -= 1


        sym_out_before_nbr = sub_seq_d[sym_out]
        sub_seq_d[sym_out] = sym_out_before_nbr-1
        sym_out_w_count = w_dict.get(sym_out, 0)
        if sym_out_w_count:
            if sym_out_w_count == sym_out_before_nbr:
                win_count -= 1
            if sym_out_w_count == sub_seq_d[sym_out]:
                win_count += 1

        if win_count==len_w:
            maya_w_counter+=1

    #print(win_count, sym_out, sym_in)
print(maya_w_counter)


