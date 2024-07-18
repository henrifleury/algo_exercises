#word_l = input().split()
'''word_l = "one two one tho three".split()

word_l = """She sells sea shells on the sea shore;
The shells that she sells are sea shells I'm sure.
So if she sells sea shells on the sea shore,
I'm sure that the shells are sea shore shells.
""".split()
'''
word_l = "aba aba; aba @?".split()


word_count_d = dict()
list_counters = []
for w in word_l:
    w_count = word_count_d.get(w, 0)
    list_counters.append(w_count)
    word_count_d[w] = w_count + 1


print(*list_counters)

#print(word_l)
#print(len(list_counters), len(word_l))
#print(list_counters)
#assert " ".join([str(i) for i in list_counters]) == "0 0 0 0 0 0 1 0 0 1 0 0 1 0 2 2 0 0 0 0 1 2 3 3 1 1 4 0 1 0 1 2 4 1 5 0 0"
assert " ".join([str(i) for i in list_counters]) == "0 0 1 0"

#print(*[word_count_d[w] for w in word_l])
#print(*word_count_d.values())

