with open("mountains/input.txt", "r") as f:
    #for line in f.readlines():
        #inp_list.append(line.strip())
    n, k = map(int, f.readline().split())
    inp_list = list(map(int, f.readline().split()))

def get_shortes_seq(seq):
    if n == 1:
        return 1, 1
    res = (n, 1, n) #длина, старт, финиш
    for start in range(n-k+1):
        color_s = set()
        fin = start
        while fin < n:
            color_s.add(seq[fin])
            #print(start, fin, color_s, res)
            if len(color_s) == k:
                if fin-start+1 <= res[0]:
                    #print("fin-start, start, fin", fin-start, start, fin)
                    res = (fin-start+1, start, fin)
                    break
            fin += 1
        if res[0] == k:
            break
    #return res
    return res[1]+1, res[2]+1

def get_shortes_seq_best(seq):
    if n == 1 or k==1:
        return 1, 1
    if len(seq) == k:
        return 1, k
    res = (n, 0, n-1) #длина, старт, финиш
    #color_counter_d = {color: 0 for color in range(1,k+1)}
    color_counter_d = dict()
    start = fin = 0
    color_counter_d[seq[start]] = 1
    while fin < n-1:#  and res[0] != k
        fin += 1
        color_counter_d[seq[fin]] = color_counter_d.get(seq[fin], 0)
        color_counter_d[seq[fin]] += 1
        while len(color_counter_d) == k:
            #assert(set(seq[start:fin+1])==color_counter_d.keys())
            if fin-start < res[0]:
                res = (fin-start, start, fin)
                #print(fin-start, "res, start, fin", res, start, fin, seq[start:fin+1])
                if fin+1-start == k:
                    break
            color_counter_d[seq[start]] -= 1
            if color_counter_d[seq[start]] == 0:
                del color_counter_d[seq[start]]
            start += 1

    return res[1]+1, res[2]+1



#print(*get_shortes_seq(inp_list))

#print(*get_shortes_seq_best(inp_list))

file_lst = ["input.txt", "input1.txt", "input3.txt", "input4.txt"]
#file_lst = ["input.txt"]
for f_name in file_lst:
    with open(f_name, "r") as f:
        n, k = map(int, f.readline().split())
        inp_list = list(map(int, f.readline().split()))
    print(*get_shortes_seq(inp_list))
    print(*get_shortes_seq_best(inp_list))
