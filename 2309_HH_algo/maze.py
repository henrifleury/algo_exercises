from collections import deque

def get_out_step_nbr():
    d_left, d_right, d_bot, d_top = (0, -1), (0, 1), (-1, 0), (1, 0)
    lab_dist = [[-1]*M for _ in range(N)]
    steps = deque()
    steps.append((x1, y1))
    lab_dist[x1][y1] = 0
    while steps:
        x, y = steps.popleft()
        if (x, y) == (x2, y2):
            #print("next_x, next_y", x, y, lab_dist[x][y])
            return lab_dist[x][y]
        for dx, dy in [d_left, d_right, d_bot, d_top]:
            next_x, next_y = x + dx, y + dy
            if (0 <= next_x < N) and (0<= next_y<M) and (lab_map[next_x][next_y])==0 and (lab_dist[next_x][next_y]==-1):
                lab_dist[next_x][next_y] = lab_dist[x][y] + 1
                steps.append((next_x, next_y))
                #print(next_x, next_y)
                #print(lab_dist)
    return 0

N, M = map(int, input().split())
y1, x1 = map(int, input().split())
y2, x2 = map(int, input().split())
lab_map = []
for i in range(N):
    lab_map.append(tuple(map(int, input().split())))
res = get_out_step_nbr()
print(res)    

N, M = (2, 3)
(y1, x1), (y2, x2) = (0, 0), (2, 1)
lab_map = ((0, 0, 0), (0, 0, 0))
res = get_out_step_nbr()
#print(res)
assert res == 3

N, M = (3, 3)
(y1, x1), (y2, x2) = (0, 0), (2, 0)
lab_map = ((0,1,0), (0,1,0), (0,0,0))

res = get_out_step_nbr()
assert res == 6


N, M = (3, 3)
(y1, x1), (y2, x2) = (0, 0), (2, 0)
lab_map = ((0,1,0), (0,1,0), (0,1,0))
#[print(s) for s in lab_map]

res = get_out_step_nbr()
print(res)
assert res == 0

N, M = (3, 4)
(y1, x1), (y2, x2) = (0, 0), (2, 0)
lab_map = ((0,1,0,0), (0,1,0,0), (0,0,0,0))
[print(s) for s in lab_map]

res = get_out_step_nbr()
print(res)