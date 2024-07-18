import heapq

f = open('input.txt', 'r')
n, k = map(int, f.readline().split())
dist_d = dict()

max_dist = 10000000000001
for i in range(k):
    a, b, l = map(int, f.readline().split())
    if a in dist_d:
        dist_d[a].append((b, l))
    else:
        dist_d[a] = [(b, l)]
    if b in dist_d:
        dist_d[b].append((a, l))
    else:
        dist_d[b] = [(a, l)]

#dist_d = sorted(dist_d)
#print(dist_d)
st, fin = map(int, f.readline().split())
visited = [False for i in range(n+1)]
distance = [max_dist for i in range(n+1)]
"""dist_hpq = [(max_dist, i) for i in range(st)]
dist_hpq += [(0, st)]
dist_hpq += [(max_dist, i) for i in range(st, n+1)]
"""
dist_hpq=[]
heapq.heapify(dist_hpq)
#print(len(dist_hpq), dist_hpq[0], dist_hpq[1], dist_hpq[-1])
cur_id = st
distance[cur_id] = 0
while cur_id != fin:
    visited[cur_id] = True
    if cur_id == fin:
        break
    if cur_id not in dist_d:
        next_id = 0
        break
    #print(cur_id)
    #print("dist_d[cur_id]", dist_d[cur_id])
    for next_id, l in dist_d[cur_id]:
        if l > 0:
            #print(next_id, l, distance[cur_id] + l, len(distance))
            if distance[cur_id]+l < distance[next_id]:
                distance[next_id] = distance[cur_id]+l
                heapq.heappush(dist_hpq, (distance[next_id], next_id))
                #print("cur_id, l, distance[next_id]", cur_id, l, distance[next_id])
    #print(len(dist_hpq), visited)
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
