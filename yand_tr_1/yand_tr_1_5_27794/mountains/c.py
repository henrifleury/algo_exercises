inp_list = []
with open("input.txt", "r") as f:
    for line in f.readlines():
        inp_list.append(line.strip())
pick_nbr = int(inp_list[0])
map_l = []
for m in inp_list[1:pick_nbr+1]:
    #map_l.append(list(map(int, inp_list[idx].split())))
    _, y = map(int, m.split())
    map_l.append(y)

n_path = int(inp_list[pick_nbr+1])
path_l = []
for path in inp_list[pick_nbr+2:]:
    path_l.append(list(map(int, path.split())))

#print(map_l)
#print(path_l)

def get_rising(map_l, path_l):
    if not map_l:
        return
    if len(map_l) == 1:
        return 0
    inc_h_l = [0, map_l[0]]
    dec_h_l = [0, map_l[0]]
    #for idx in range(1, len(map_l)):
    for idx in range(1, len(map_l)):
        delta_h = map_l[idx] - map_l[idx-1]
        if delta_h>0:
            inc_h, dec_h = delta_h, 0
        else:
            inc_h, dec_h = 0, -1*delta_h
        inc_h_l.append(inc_h_l[-1] + inc_h)
        dec_h_l.append(dec_h_l[-1] + dec_h)
    #print(inc_h_l)
    #print(dec_h_l)

    for st, fin in path_l:
        #cur_map = inc_h_l if fin > st else dec_h_l
        #print(abs(cur_map[fin-1] - cur_map[st-1]))
        if fin > st:
            print(inc_h_l[fin]-inc_h_l[st])
        else:
            print(dec_h_l[st] - dec_h_l[fin])
get_rising(map_l, path_l)