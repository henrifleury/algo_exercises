#шаги инвертированы i - номер строки, координата y, j - номер столбца-  соотв x
d_left, d_right, d_bot, d_top = (0, -1), (0, 1), (-1, 0),  (1, 0)
def get_out_step_nbr(N, M, entry_c, exit_c, lab_map):
    path_dots = set()
    new_dots = set([entry_c])
    path_len=-1
    while len(new_dots) != 0:
        #print('***path_dots***', path_dots, "new_dots", new_dots)
        path_len += 1
        new_steps = set()
        for dot in new_dots:
            if dot in path_dots:
                continue
            #print('*dot*', dot, 'new_dots', new_dots)
            if dot[1] < M:
                new_steps.add(map(sum, zip(dot, d_right)))
                #print("right", new_steps)
            if dot[1] > 0:
                new_steps.add(map(sum, zip(dot, d_left)))
                #print("left ", new_steps)
            if dot[0] < N:
                new_steps.add(map(sum, zip(dot, d_top)))
                #print("top", *new_steps)
            if dot[0] > 0:
                new_steps.add(map(sum, zip(dot, d_bot)))
                #print("bot", *new_steps)
            #print('new_steps', [list(step) for step in new_steps])
            #print([(i, j) for i, j in new_steps if lab_map[i][j] == 0])
            '''
            tmp_l=[]
            for i, j in new_steps:
                #print(i, j, lab_map[i][j])
                if lab_map[i][j]==1:
                    print(i, j, 1)
                    continue
                else:
                    print(i, j, 0)
                    tmp_l.append((i,j))
            print("tmp_l", tmp_l)
            '''
            new_steps = set([(i, j) for i, j in new_steps if lab_map[i][j] == 0])
            #print('new_steps', new_steps)
            #return

        if exit_c in new_steps:
            #print("exit_c", exit_c, new_steps)
            path_len += 1
            return path_len
        path_dots = path_dots | new_dots
        new_dots = new_steps

    return 0

#def bfs(known_dots, exit_p)


N, M = map(int, input().split())
entry_c = map(int, input().split())
exit_c = map(int, input().split())
lab_map = []
for i in range(N):
    lab_map.append(tuple(map(int, input().split())))
res = get_out_step_nbr(N-1, M-1, tuple(entry_c)[::-1], tuple(exit_c)[::-1], lab_map)
print(res)


N, M = (2, 3)
entry_c, exit_c = (0, 0), (2, 1)
lab_map = ((0,0,0), (0,0,0))
[print(s) for s in lab_map]

res = get_out_step_nbr(N-1, M-1, entry_c[::-1], exit_c[::-1], lab_map)
assert res == 3

N, M = (3, 3)
entry_c, exit_c = (0, 0), (2, 0)
lab_map = ((0,1,0), (0,1,0), (0,0,0))
[print(s) for s in lab_map]

res = get_out_step_nbr(N-1, M-1, entry_c[::-1], exit_c[::-1], lab_map)
assert res == 6

N, M = (3, 3)
entry_c, exit_c = (0, 0), (2, 0)
lab_map = ((0,1,0), (0,1,0), (0,1,0))
[print(s) for s in lab_map]

res = get_out_step_nbr(N-1, M-1, entry_c[::-1], exit_c[::-1], lab_map)
print(res)
assert res == 0



'''
N, M = (3, 4)
entry_c, exit_c = (0, 0), (2, 0)
lab_map = ((0,1,0,0), (0,1,0,0), (0,0,0,0))
[print(s) for s in lab_map]

res = get_out_step_nbr(N-1, M-1, entry_c[::-1], exit_c[::-1], lab_map)
print(res)'''