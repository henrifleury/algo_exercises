#g1 = input()
#g2 = input()

g1 = "ABBACAB"
g2 = "BCABB"

def get_pairs(g):
    res = dict()
    if len(g)>=2:
        for i in range(len(g)-1):
            pair = g[i]+g[i+1]
            res[pair] = res.get(pair, 0)+1
    return res

def get_degree(g1, g2):
    pair_d1 = get_pairs(g1)
    pair_d2 = get_pairs(g2)
    common_keys = set(pair_d1.keys()) & set(pair_d2.keys())
    res=0
    for k in common_keys:
        res += pair_d1[k]
    return res

print(get_degree(g1, g2))