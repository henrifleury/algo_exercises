'''t, d, n = map(int, input().split())
# t - период навигатора, d - точность навигатора, n*t - длительность пробежки n - количество сообщений
coord_l = []
for i in range(n):
    coord_l.append(tuple(map(int, input().split())))
'''

#t, d, n = 2, 2, 1
#coord_l = [[2,2]]
t,d,n = 2, 1, 5
coord_l = [[0, 1], [-2, 1], [-2, 3], [0, 3], [2, 5]]



START_COORD = (0, 0)

def get_manh_dist(coord_1, coord_2):
    return abs(coord_2[0]-coord_1[0])+abs(coord_2[1]-coord_1[1])

def get_coord_enabled(cur_coord , cur_t):
    cur_step_set = set([tuple(cur_coord)])
    cur_x, cur_y = cur_coord
    dx = [1, -1, 0, 0] #  0]
    dy = [0, 0, 1, -1] #  0]

    for i in range(4):
        next_x, next_y = cur_x+dx[i], cur_y+dy[i]
        cur_step_set.add((next_x, next_y))
    if cur_t==1:
        return cur_step_set
    else:
        res_step = cur_step_set.copy()
        for coord in cur_step_set:
            res_step |= get_coord_enabled(coord, cur_t-1)
        return res_step

def get_points(coord_l):
    prev_coord_set = set([START_COORD])
    navy_coord_enabled = set()
    for navy_coord in coord_l:
        cur_coord_set = prev_coord_set.copy()
        for path_coord in prev_coord_set:
            cur_coord_set |= get_coord_enabled(path_coord, t)
        #print('path_coord', len(cur_coord_set) ,cur_coord_set)
        #navy_coord_enabled.add(navy_coord)
        navy_coord_enabled = get_coord_enabled(navy_coord, d)
        #print('navy_coord_enabled', navy_coord_enabled)
        cur_coord_set = cur_coord_set & navy_coord_enabled
        #print('cur_coord_set', cur_coord_set)
        prev_coord_set = cur_coord_set
    return cur_coord_set

res = get_points(coord_l)
print(len(res))
for coord in res:
    print(*coord)

t,d,n = 2, 1, 5
coord_l = [[0, 1], [-2, 1], [-2, 3], [0, 3], [2, 5]]
assert get_points(coord_l) == {(2, 4), (1, 5)}

t,d,n = 1, 1, 1
coord_l = [[0, 0]]
assert get_points(coord_l) == {(0, 0), (1, 0), (-1, 0), (0, -1), (0, 1)}

t,d,n = 1, 10, 1
coord_l = [[0, 0]]
assert get_points(coord_l) == {(0, 0), (1, 0), (-1, 0), (0, -1), (0, 1)}

