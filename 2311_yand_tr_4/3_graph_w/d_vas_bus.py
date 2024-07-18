import heapq

f = open('input.txt', 'r')
n = int(f.readline().strip())
st, fin = map(int, f.readline().split())
r = int(f.readline().strip())
"""
dep_arr, dep_t_arr, ar_arr, ar_t_arr = [0]*(r+1), [0]*(r+1), [0]*(r+1), [0]*(r+1)
for i in range(r):
    dep_arr[i+1], dep_t_arr[i+1], ar_arr[i+1], ar_t_arr[i+1] = map(int, f.readline().split())
print(dep_arr, dep_t_arr, ar_arr, ar_t_arr)
"""
dist_d = dict()

max_dist = 1111111111

for i in range(r):
    dep, td, arvl, ta = map(int, f.readline().split())
    if dep in dist_d:
        dist_d[dep].append((arvl, td, ta))
    else:
        dist_d[dep] = [(arvl, td, ta)]

visited = [False for i in range(n+1)]
distance = [max_dist for i in range(n+1)]
#dep_time = [0 for i in range(n+1)]

dist_hpq = []
heapq.heapify(dist_hpq)

cur_id = st
distance[cur_id] = 0
while cur_id != fin:
    visited[cur_id] = True
    if cur_id == fin:
        break
    if cur_id not in dist_d:
        next_id = -1
        break

    for next_id, td, ta in dist_d[cur_id]:
        #print(next_id, td, ta, distance[cur_id])
        if td >= distance[cur_id]:
            #print(next_id, td, ta, distance[cur_id], distance[next_id])
            if ta < distance[next_id]:
                distance[next_id] = ta
                heapq.heappush(dist_hpq, (distance[next_id], next_id))
                #print("cur_id, l, distance[next_id]", cur_id, l, distance[next_id])


    if len(dist_hpq):
        next_id = heapq.heappop(dist_hpq)[1]
    else:
        next_id = 0
        break
    while visited[next_id]:
        if len(dist_hpq):
            next_id = heapq.heappop(dist_hpq)[1]
        else:
            next_id = 0
            break
    #print(next_id, len(dist_hpq))
    if distance[next_id] >= max_dist:  # next_dist >= max_dist
        next_id = 0
        # print("next_id == fin", next_id == fin, next_id)
        # cur_id = next_id
        break
    else:
        # gr_path[next_id] = cur_id
        # print( cur_id, next_id, "cur_id, gr_path", gr_path)
        cur_id = next_id

#print(len(dist_hpq), dist_hpq[0], dist_hpq[1], dist_hpq[-1])
#print(distance)

if cur_id == fin:
    print(distance[fin])
else:
    print(-1)

#print(len(dist_hpq), dist_hpq)#, dist_hpq[0], dist_hpq[1], dist_hpq[-1])
#print(distance)
