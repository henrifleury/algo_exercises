test_f_name = 'input.txt'
f = open(test_f_name, 'r')


voc = f.readline().strip().split()
text = f.readline().strip().split()


def translate():
    voc_fast = dict()
    for voc_w in voc:
        first_sym = voc_w[0]
        if first_sym not in voc_fast:
            voc_fast[first_sym] = set()
        voc_fast[first_sym].add(voc_w)
    #voc_fast = {k: sorted(v) for k,v in voc_fast.items()}

    res = []
    for w in text:
        first_sym = w[0]
        if first_sym in voc_fast:
            for i in range(1, len((w))):
                if w[0:i] in voc_fast[first_sym]:
                    res.append(w[0:i])
                    break
            else:
                res.append(w)
        else:
            res.append(w)

    return res

print(*translate())
