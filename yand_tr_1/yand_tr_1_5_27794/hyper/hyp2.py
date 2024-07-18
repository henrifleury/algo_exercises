with open("input.txt", "r") as f:
    n, k = list(map(int, f.readline().strip().split()))
    card_lst = list(map(int, f.readline().strip().split()))
#print(n, k, card_lst)

card_sorted = sorted(card_lst)
card_dict_a = dict()
for card in card_sorted:
    card_dict_a[card] = card_dict_a.get(card, 0) + 1

mark_set = set()
for card_a in card_dict_a.keys():
    card_dict_b = card_dict_a.copy()
    card_dict_b[card_a] -= 1
    if card_dict_b[card_a]==0:
        del card_dict_b[card_a]
    for card_b in card_dict_b.keys():
        (big, small) = (card_a, card_b) if card_a > card_b else (card_b, card_a)
        if small * k < big:
            continue
        card_dict_c = card_dict_b.copy()
        card_dict_c[card_b] -= 1
        if card_dict_c[card_b]==0:
            del card_dict_c[card_a]
        for card_c in card_dict_c.keys():
            biggest = big if big > card_c else card_c
            smallest = small if small < card_c else card_c
            if smallest * k < biggest:
                continue
            mark_set.add((card_a, card_b, card_c))
#print(sorted(mark_set))
print(len(mark_set))
# сортируем карточки
# считаем количества карточек в словарь
# перебеираем ключи словаря
# забираем одну из карточек - минусуем количество карт в словаре (копии)
# перебираем оставшиемя карточки пока отношение не превысит k
# забираем одну из оставшихся карточек - минусуем количество карт в словаре (копии)
