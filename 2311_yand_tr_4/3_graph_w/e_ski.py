import heapq

f = open('input.txt', 'r')
n = int(f.readline().strip())-1
f.readline()

time_d, vel_d = dict(), dict()
for i in range(n):
    time_d[i], vel_d[i] = map(int, f.readline().split())

dist_d = dict()
max_dist = 333333333
for i in range(n-1):
    a, b, l = map(int, f.readline().split())
    if a in dist_d:
        dist_d[a].append((b, l))
    else:
        dist_d[a] = [(b, l)]
    if b in dist_d:
        dist_d[b].append((a, l))
    else:
        dist_d[b] = [(a, l)]

fin = 0
for st in range(1, n):
    visited = [False for i in range(n + 1)]
    distance = [max_dist for i in range(n + 1)]
    gr_path = [-1 for i in range(n + 1)]

    dist_hpq = []
    heapq.heapify(dist_hpq)
    cur_id = st
    distance[cur_id] = time_d[cur_id]
    cur_v = vel_d[cur_id]

    while cur_id != fin:
        print("cur_id", cur_id, distance[cur_id], time_d[cur_id], vel_d[cur_id])
        visited[cur_id] = True
        if cur_id == fin:
            break
        if cur_id not in dist_d:
            next_id = -1
            break
        for next_id, l in dist_d[cur_id]:
            print("next_id", next_id, l, l/cur_v)
            if distance[cur_id]+l/cur_v < distance[next_id]:
                distance[next_id] = distance[cur_id]+l/cur_v
                heapq.heappush(dist_hpq, (distance[next_id], next_id))
                #print("cur_id, l, distance[next_id]", cur_id, l, distance[next_id])
            """
        break
    break