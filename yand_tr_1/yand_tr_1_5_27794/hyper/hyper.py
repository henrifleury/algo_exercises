## неправильно прочитал условие, бросил

with open("input.txt", "r") as f:
    n, k = list(map(int, f.readline().strip().split()))
    card_lst = list(map(int, f.readline().strip().split()))
#print(n, k, card_lst)
    card_a_lst = sorted(card_lst)
    comb_counter = 0
    for card_a_id, card_a in enumerate(card_a_lst[:len(card_a_lst)-3+1]):
        card_b_lst = card_a_lst.copy()
        card_b_lst.pop(card_a_id)
        for card_b_id, card_b in enumerate(card_b_lst[:len(card_a_lst)-3+2]):
            (big, small) = (card_a, card_b) if card_a >= card_b else (card_b, card_a)
            if big % small==0:
                if big // small <= k:
                    card_c_lst = card_b_lst.copy()
                    card_c_lst.pop(card_b_id)
                    for card_c_id, card_c in enumerate(card_c_lst[:len(card_b_lst)-3+3]):
                        (biggest, smallest) = (big, card_c) if big >= card_c else (card_c, big)
                        if (biggest % smallest == 0) & (biggest % small == 0):
                            if (biggest // smallest <= k) & (biggest % small == 0):
                                print(card_a, card_b, card_c)
                                comb_counter += 1
                            else:
                                break

                else:
                    break
print(comb_counter)