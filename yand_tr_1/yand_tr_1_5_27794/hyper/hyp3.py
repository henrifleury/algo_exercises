import gc

with open("input.txt", "r") as f:
    n, k = list(map(int, f.readline().strip().split()))
    card_lst = list(map(int, f.readline().strip().split()))
#print(n, k, card_lst)

card_dict = dict()
for card in card_lst:
    #card_dict[card] = card_dict.get(card, 0) + 1
    if card not in card_dict:
        card_dict[card] = 1
    else:
        card_dict[card] += 1

del card_lst
gc.collect()
uniq_cards = sorted(card_dict.keys())
double_card = [1 if card_dict[nbr] > 1 else 0 for nbr in uniq_cards]
double_card.append(0)

fin = 0
res = 0

#cur_doubles = -1 if double_card[0] else 0
cur_doubles = 0
for start in range(len(uniq_cards)):
    while fin < len(uniq_cards) and uniq_cards[start]*k >= uniq_cards[fin]:
        fin += 1
        cur_doubles += double_card[fin]

    cur_card_set = uniq_cards[start:fin] #len(cur_card_set) = fin - start
    #cur_double_card = double_card[start+1:fin] #дубли первого значения отдельно
    # считаем все возможные вторые карточки не равные uniq_cards[start]
    cards_b_not_a_nbr = fin-start-1
    # считаем все возможные третьи карточки не равные uniq_cards[start] и uniq_cards[start+1]
    cards_c_not_b_not_a_nbr = cards_b_not_a_nbr - 1 #len(cur_card_set[2:]) #  len(cur_card_set[2:]) = fin - start -2
    # если
    #res += cards_b_not_a_nbr * cards_c_not_b_not_a_nbr * 3

    #print(cur_card_set)
    # если вторых карточек больше одной то добавляется три варианта для каждого дубля

    #for j in range(1, len(cur_card_set)):
        #if card_dict[cur_card_set[j]] > 1:
            #print('+3')
            #res += 3

    #print(start,fin, "cur_double_card, sum(cur_double_card), cur_doubles", cur_double_card, sum(cur_double_card), cur_doubles)
    #res += (((card_dict[cur_card_set[0]]>1)+cards_c_not_b_not_a_nbr) * cards_b_not_a_nbr + sum(cur_double_card)) * 3

    res += (((card_dict[cur_card_set[0]] > 1) + cards_c_not_b_not_a_nbr) * cards_b_not_a_nbr + cur_doubles - double_card[fin]) * 3

    # если первых карточек больше одной то добавляется 3*len(cur_card_set[1:] варианта для каждого дубля
    #if card_dict[cur_card_set[0]]>1:
        #res += 3 * cards_b_not_a_nbr # len(cur_card_set[1:])
    #res += (card_dict[cur_card_set[0]]>1)*3 * cards_b_not_a_nbr  # len(cur_card_set[1:])

    # если первых карточек больше двух добавляется еще один вариант
    if card_dict[cur_card_set[0]] > 2:
        res += 1

    cur_doubles -= double_card[start+1]
    #print('cur_doubles', cur_doubles, 'double_card[start+1]', double_card[start+1])

    #print(res, cur_card_set, double_card)
    #if fin == len(uniq_cards):
        #break
    #del card_dict[uniq_cards[start]]
    #gc.collect()
print(res)
