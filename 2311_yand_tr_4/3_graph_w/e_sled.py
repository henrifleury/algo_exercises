import heapq

f = open('input.txt', 'r')
n = int(f.readline().strip())
# в первой строке всегда будем считать 1 1, отбросим, n поправим чтоб старому
# city_time_to_ready, city_velosity = map(int, f.readline().split())
# ttready_d, vel_d = {0: city_time_to_ready}, {0: city_velosity}
ttready_d, vel_d = dict(), dict()
for i in range(1, n + 1):
    ttready_d[i], vel_d[i] = map(int, f.readline().split())
# некоторые манипуляции с n
dist_d = dict()
for i in range(n - 1):
    a, b, l = map(int, f.readline().split())
    if a in dist_d:
        dist_d[a].append((l, b))
    else:
        dist_d[a] = [(l, b)]
    if b in dist_d:
        dist_d[b].append((l, a))
    else:
        dist_d[b] = [(l, a)]

# тащить среднюю скорость и пересчитывает только если превышает
visited = [False for i in range(n + 1)]
max_dist, max_time = 3333333333, 5555555555
# max_time = 5555555555
distance = [max_dist for i in range(n + 1)]
path_time = [max_time for i in range(n + 1)]
road_map = [-1 for i in range(n + 1)]
#road_map_rev = [-1 for i in range(n + 1)]
path_time_hpq = []
heapq.heapify(path_time_hpq)

city_id = 1
distance[city_id], path_time[city_id] = 0, 0
# path_time[city_id] = 0
cur_id, prev_change_id = city_id, 1
# max_path_time
while cur_id > 0:
    # не должно такого быть
    # if cur_id not in dist_d:
    # cur_id = -1
    # break
    for l, next_id in dist_d[cur_id]:
        # print(next_id, l, ttready_d[next_id], l/vel_d[next_id], l/vel_d[next_id]+ttready_d[next_id])
        # print(cur_id, next_id, l, vel_d[next_id], "ttready_d", ttready_d[next_id], l/vel_d[next_id]+ttready_d[next_id], path_time[next_id])
        new_time_old_vel = l / vel_d[next_id] + ttready_d[next_id] + path_time[cur_id]
        new_time_new_vel = l / vel_d[next_id] + ttready_d[next_id] + distance[cur_id] / vel_d[next_id]
        new_time = min(new_time_old_vel, new_time_new_vel)
        # print("cur_id", cur_id, next_id, "new_time", new_time, "new_time_new_vel", new_time_new_vel, "new_time_old_vel", new_time_old_vel)
        if new_time < path_time[next_id]:
            # path_time[next_id] = path_time[cur_id]+new_time
            path_time[next_id] = new_time
            distance[next_id] = distance[cur_id] + l
            road_map[next_id] = cur_id
            # road_map[next_id] = prev_change_id
            # print("cur_id, next_id, prev_change_id", cur_id, next_id, prev_change_id, road_map)
            """
            if new_time_new_vel > new_time_old_vel:
                # prev_change_id = next_id
                prev_change_id = cur_id
                # print(prev_change_id, "prev_change_id, cur_id, next_id ", cur_id, next_id,  road_map, path_time, distance)
            """
            heapq.heappush(path_time_hpq, (path_time[next_id], next_id))
            print(cur_id, next_id, road_map)
    if len(path_time_hpq):
        next_id = heapq.heappop(path_time_hpq)[1]
    else:
        next_id = 0
        break
    while visited[next_id]:
        if len(path_time_hpq):
            next_id = heapq.heappop(path_time_hpq)[1]
        else:
            next_id = 0
            break

    if path_time[next_id] >= max_time:  # next_dist >= max_dist
        next_id = -1
        break
    else:
        cur_id = next_id

    # break # break
print("path_time", path_time)
print("distance", distance)
print("road_map", road_map)
print(cur_id)
"""
far_id = path_time.index(max(path_time[1:]))
print(path_time[far_id])
print(far_id, end=" ")
cur_id = far_id
# i=0
# while i<n+1:
while cur_id != city_id:
    print(cur_id, end=" ")
    cur_id = road_map[cur_id]
    # i+=1
"""