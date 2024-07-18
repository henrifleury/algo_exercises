f = open('input.txt', 'r')
n = int(f.readline().strip())
# в первой строке всегда будем считать 1 1, отбросим, n поправим чтоб старому
#city_time_to_ready, city_velosity = map(int, f.readline().split())
#ttready_d, vel_d = {0: city_time_to_ready}, {0: city_velosity}
ttready_d, vel_d = dict(), dict()
for i in range(1, n+1):
    ttready_d[i], vel_d[i] = map(int, f.readline().split())
ttready_d[1], vel_d[1] = 0, 1
#print(len(ttready_d), ttready_d)

city_id, max_dist, max_t = 1, 3333333333, 5555555555
#ttready_d[i], vel_d[i] = max_t, 1

dist_d = dict()
#for i in range(1, n):
dist_arr = [[max_dist ]*(n+1) for i in range(n+1) ]
t_arr = [[max_t ]*(n+1) for i in range(n+1) ]

dist_arr[0][0]=0
for i in range(1, n):
    a, b, l = map(int, f.readline().split())
    #(a,b) = (a,b) if a<=b else (b,a)
    if a in dist_d:
        dist_d[a].append(b)
    else:
        dist_d[a] = [b]
    if b in dist_d:
        dist_d[b].append(a)
    else:
        dist_d[b] = [a]

    dist_arr[a][b] = l
    dist_arr[b][a] = l
    dist_arr[i][i] = 0
    t_arr[i][i] = ttready_d[i]


for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n + 1):
            dist_arr[i][j] = min(dist_arr[i][j], dist_arr[i][k]+dist_arr[k][j])
            dist_arr[j][i] = dist_arr[i][j]

t_arr[1] = [max_t for j in range(n+1)]
#for i in range(2, n+1):
for i in range(1, n + 1):
    for j in range(1, n+1):
        #print(i, j, ttready_d[i], dist_arr[i][j], vel_d[i], dist_arr[i][j] / vel_d[i], ttready_d[i] + dist_arr[i][j] / vel_d[i])
        t_arr[i][j] = ttready_d[i] + dist_arr[i][j] / vel_d[i]
    #break

"""
z=2
print(dist_arr[z])
print(z, "t_arr", t_arr[2])
print(ttready_d[z])
print(vel_d[z])
"""
visited = [False for i in range(n+1)]
unknown_idx = [i for i in range(1, n+1)]
best_time_arr = [max_t for i in range(n+1)]
gr_path = [-1 for i in range(n+1)]

cur_id = city_id
best_time_arr[cur_id] = 0

while cur_id >0:
    visited[cur_id] = True
    unknown_idx.remove(cur_id)

    #for next_id, t in enumerate(t_arr[cur_id]):
    for next_id in range(1, n+1):
        new_time = best_time_arr[cur_id] + t_arr[next_id][cur_id]
        if new_time < best_time_arr[next_id]:
            best_time_arr[next_id] = new_time
            gr_path[next_id] = cur_id

    next_id, next_t = cur_id, max_t
    for i in unknown_idx:
        if best_time_arr[i] < next_t:
            next_id, next_t = i, best_time_arr[i]
    if next_id == cur_id:
        break
    else:
        cur_id = next_id


#print("path_time", best_time_arr)
#print("gr_path", gr_path)



far_id = best_time_arr.index(max(best_time_arr[1:]))
print(best_time_arr[far_id])
#print(far_id)
print(far_id, end=" ")
cur_id = gr_path[far_id]
# i=0
# while i<n+1:
#prev_id = city_id
while cur_id > city_id:
    print(cur_id, end=" ")
    cur_id = gr_path[cur_id]
    # i+=1
print(cur_id)