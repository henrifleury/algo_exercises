f = open('input.txt', 'r')
n, s, fin = map(int, f.readline().split())

"""if s==fin:
    print(0)
else:
"""
matr = [[0 for i in range(n+1)]]
for i in range(n):
    matr.append([0]+list(map(int, f.readline().split())))

visited = [False for i in range(n+1)]
unknown_idx = [i for i in range(1, n+1)]
max_dist = 999
dist = [max_dist for i in range(n+1)]
gr_path = [-1 for i in range(n+1)]

dist[s] = 0
gr_path[s] = s

cur_id = s
while sum(visited) <= n:
    if visited[cur_id]:
        continue
    else:
        visited[cur_id] = True
        unknown_idx.remove(cur_id)
        if cur_id == fin:
            break
        for idx, cur_dist in enumerate(matr[cur_id]):
            if cur_dist > 0:
                if cur_dist+dist[cur_id] < dist[idx]:
                    dist[idx] = cur_dist+dist[cur_id]
                    gr_path[idx] = cur_id
                    #print("idx, dist", idx, dist, unknown_idx)
        next_id, next_dist = cur_id, max_dist
        for idx in unknown_idx:
            if dist[idx] < next_dist:
                next_id, next_dist = idx, dist[idx]

        if next_id == cur_id: # next_dist >= max_dist
            #print("next_id == fin", next_id == fin, next_id)
            #cur_id = next_id
            break
        else:
            #gr_path[next_id] = cur_id
            #print( cur_id, next_id, "cur_id, gr_path", gr_path)
            cur_id = next_id


if cur_id == fin:
    prev = fin
    path_rev = [prev]
    #print(prev, end=" ")
    while prev !=s:
        path_rev.append(gr_path[prev])
        #print(gr_path[prev], end=" ")
        prev = gr_path[prev]
    #print(gr_path[prev])
    [print(i, end=" ") for i in path_rev[::-1]]
else:
    print(-1)
#print(visited)
#print(dist)