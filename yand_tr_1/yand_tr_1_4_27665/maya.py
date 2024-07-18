'''g, s = map(int, input())
w = input()
seq = input()
'''

g,s = 4,11
w = "cAda"
seq = "AbrAcadAbRa"

maya_w_counter = 0
if (g<1) | (g>s):
    pass
else:
    w_dict = dict()
    for sym in w:
        w_dict[sym] = w_dict.get(sym, 0) + 1
    #print(w_dict)

    maybe_w = seq[:g-1] # для старта 3 символа, четвертый в цикле
    maybe_w_dict = dict()
    for sym in maybe_w:
        maybe_w_dict[sym] = maybe_w_dict.get(sym, 0) + 1


    st = 0
    len_w_dict = len(w_dict)

    win_counter = 0
    for k in w_dict.keys():
        if w_dict[k] == maybe_w_dict.get(k, None):
            win_counter += 1

    while st <= s-g:
        sym_in = seq[st + g - 1]
        maybe_w_dict[sym_in] = maybe_w_dict.get(sym_in, 0) + 1

        #if sym in w_dict &  maybe_w_dict[sym]==w_dict[sym]:
            #win_counter += 1
        w_in_sym_nbr = w_dict.get(sym_in, 0)
        if w_in_sym_nbr>0:
            if w_in_sym_nbr == maybe_w_dict[sym_in]:
                win_counter += 1

        #if w_dict == maybe_w_dict:
        if win_counter == len_w_dict:
            maya_w_counter += 1

        '''if maybe_w_dict[seq[st]] == 1:
            del maybe_w_dict[seq[st]]
        else:
            maybe_w_dict[seq[st]] -= 1'''
        sym_out = seq[st]
        maybe_w_dict[sym_out] = maybe_w_dict.get(sym_in, 0) - 1
        w_out_sym_nbr = w_dict.get(sym_out, 0)
        if w_out_sym_nbr>0:
            if w_out_sym_nbr != maybe_w_dict[sym_out]:
                win_counter -= 1

        st += 1

print(maya_w_counter)