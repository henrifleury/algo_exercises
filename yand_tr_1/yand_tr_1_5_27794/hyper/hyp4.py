with open("input.txt", "r") as f:
    n, k = list(map(int, f.readline().strip().split()))
    card_lst = list(map(int, f.readline().strip().split()))
#print(n, k, card_lst)

card_sorted = sorted(card_lst)
card_dict_a = dict()
for card in card_sorted:
    card_dict_a[card] = card_dict_a.get(card, 0) + 1

mark_set = set()
uniq_cards = sorted(card_dict_a.keys())
fin = 0
res = 0

for start in range(len(uniq_cards)):
    card_a = uniq_cards[start]
    while fin < len(uniq_cards) and uniq_cards[start]*k >= uniq_cards[fin]:
        #print(n, fin)
        fin += 1


