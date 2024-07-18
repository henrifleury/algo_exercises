#word_l = input().split()

word_l = "apple orange banana banana orange".split()
def get_min_word(word_l):
    if not word_l:
        return
    counter_d = dict()
    min_max_word = word_l[0]
    max_counter = 0
    for w in word_l:
        counter_d[w] = counter_d.get(w, 0) + 1
        if counter_d[w] >= max_counter:
            if counter_d[w] == max_counter:
                if w < min_max_word:
                    min_max_word = w
            else:
                max_counter = counter_d[w]
                min_max_word = w

    return min_max_word

def get_min_word_fast(word_l):
    if not word_l:
        return
    counter_d = dict()
    min_max_word = word_l[0]
    max_counter = 0
    for w in word_l:
        counter_d[w] = counter_d.get(w, 0) + 1
        if counter_d[w] >= max_counter:
            if counter_d[w] == max_counter:
                if w < min_max_word:
                    min_max_word = w
            else:
                max_counter = counter_d[w]
                min_max_word = w

    return min_max_word

def get_min_word_extra_fast(word_l):
    if not word_l:
        return
    counter_d = dict()
    counter_k = dict()
    min_max_word = word_l[0]
    max_counter = 0
    [counter_d[w] = counter_d.get(w, 0) + 1 for w in word_l]
        #if counter_d[w]>max_counter:
            #max_counter=counter_d[w]
        counter_k[counter_d[w]] = counter_k.get(counter_d[w], [])
        counter_k[counter_d[w]].append(w)
        '''
        if counter_d[w] >= max_counter:
            if counter_d[w] == max_counter:
                if w < min_max_word:
                    min_max_word = w
            else:
                max_counter = counter_d[w]
                min_max_word = w
        '''
    max_counter = max(counter_k.keys())
    min_max_word = min(counter_k[max_counter])
    return min_max_word


print(get_min_word_extra_fast(word_l))

word_l = "oh you touch my tralala mmm my ding ding dong".split()
print(get_min_word_extra_fast(word_l))
word_l = """q w e r t y u i o p
a s d f g h j k l
z x c v b n m
""".split()
print(get_min_word_extra_fast(word_l))