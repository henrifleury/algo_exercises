inp_list = []
f = open('input.txt', 'r')
n, m = map(int, f.readline().split())

rec_d = dict()
#for idx in range(m):
    #rec_d[idx] = []

for idx in range(n):
    rec_type = int(f.readline())
    rec_d[rec_type] = rec_d.get(rec_type,[])
    rec_d[rec_type].append(idx)

def mod_rec_list(rec_d):
    if len(rec_d) < 1:
        return []
    res = []
    prev_rec_type = list(rec_d.keys())[0]
    res.append(rec_d[prev_rec_type][0])
    rec_d[prev_rec_type] = rec_d[prev_rec_type][1:]
    while len(rec_d) > 1:
        print(res, prev_rec_type)
        print(rec_d)
        add_rec_d = dict() # словарь - ключ - номер рекомендации, значение - тип
        rec_types = list(rec_d.keys())
        for k in rec_types:
            if k!= prev_rec_type:
                add_rec_d[rec_d[k][0]] = k
        print(add_rec_d)
        next_rec = min(list(add_rec_d.keys()))
        res += [next_rec]
        prev_rec_type = add_rec_d[next_rec]
        rec_d[prev_rec_type] = rec_d[prev_rec_type][1:]
        if len(rec_d[k]) == 0:
            del rec_d[k]
    if len(rec_d) == 1:
        last_rec_type  = list(rec_d.keys())[0]
        if last_rec_type != prev_rec_type:
            last_recs = rec_d[last_rec_type]
            if last_recs:
                res.append(last_recs[0])

    return res


print(*mod_rec_list(rec_d))
