def get_max_len(inp_s:str):
    #print(len(inp_s))
    if len(inp_s) <= 1:
        return len(inp_s)
    max_len = 1
    cur_len = 1
    sym = inp_s[0]
    for s in inp_s[1:]:
        if s == sym:
            cur_len += 1
        else:
            max_len = max(max_len, cur_len)
            cur_len = 1
            sym = s
    return max(max_len, cur_len)

inp_s = input()
res = get_max_len(inp_s)
print(res)

assert get_max_len("a")==1
assert get_max_len("abbc")==2
assert get_max_len("aabbb")==3
assert get_max_len("adddaabaa")==3
assert get_max_len("ddddaabaa")==4
