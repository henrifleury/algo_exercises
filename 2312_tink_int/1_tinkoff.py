"f = open('input.txt', 'r')
#n = int(f.readline())
#arr_a = list(map(int, f.readline().split()))

n = int(input())

slogan = "TINKOFF"
slogan_len = len(slogan)
slogan_d = {}
for s in slogan:
    slogan_d[s] = slogan_d.get(s, 0)+1

for i in range(n):
    cur_slogan_d = slogan_d.copy()
    #sym_str = f.readline().strip()
    sym_str = input().strip()
    #print("i", i, sym_str, len(sym_str))
    if len(sym_str) != slogan_len:
        print("No")
        continue
    res = "Yes"
    for s in sym_str:
        rest = cur_slogan_d.get(s, 0)
        if rest>0:
            cur_slogan_d[s] = rest - 1
        else:
            res = "No"
            break
    print(res)

