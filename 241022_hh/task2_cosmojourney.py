'''
Отдыхая в деревне Пётр мысленно вернулся в детство и вспомнил одну из своих любимых
 компьютерных игр. В мире этой игры произошёл катаклизм, разорвавший его на множество
  островов летающих в космическом пространстве. Со временем острова расположились в
   пространстве ровным рядом, один за другим.

После катаклизма, осталось всего два способа путешествовать по миру:

1. магические паромы, перемещающиеся между соседними островами (естественно, паром может
 двигаться в обе стороны), таким образом с острова, который стоит на i-ом месте
  в космическом ряду, можно попасть на i-1 и i+1 острова;

2. порталы, через которые можно телепортироваться между островами независимо от расстояния,
 но только если до катаклизма эти острова составляли один материк (любопытно, что материки в
  этом мире имели не названия, а номера).

Петру стало интересно, за какое минимальное количество перемещений можно добраться от
первого острова до последнего. Помогите ему это выяснить (сам он всё ещё отдыхает).
'''
import heapq

inf = 1000000
def get_time(islands):
    tr_d = dict()
    start, fin = islands[0], islands[-1]
    if start == fin:
        return 0
    prev = start
    tr_d[prev] = set()
    inf = 100000
    cur_dist = [[0, start]]
    for i in range(1, len(islands)):
        cur = islands[i]
        if cur == prev:
            continue
        tr_d[prev].add(cur)
        if cur in tr_d:
            tr_d[cur].add(prev)
        else:
            tr_d[cur] = set([prev])
            cur_dist.append([inf, cur]) # all vertex except start
        prev = cur

    dist_d = {k: v for (v, k) in cur_dist}
    heapq.heapify(cur_dist)

    visited = set()
    prev_d = dict()
    #print(cur_dist, 'dist_d', dist_d)
    print(islands, tr_d)
    while cur_dist:
        cur_distance, cur = heapq.heappop(cur_dist)
        if cur == fin:
            break
            #return cur_distance
        cur_distance += 1
        #print('cur', cur, tr_d[cur], 'cur_distance', cur_distance, visited)
        if cur in visited:
            continue
        visited.add(cur)
        for isl in tr_d[cur]:
            if dist_d[isl] > cur_distance:
                #print(isl, cur_distance)
                dist_d[isl] = cur_distance
                prev_d[isl] = cur
                heapq.heappush(cur_dist, [cur_distance, isl])

    # Восстанавливаем порталы
    tmp = fin
    continent_path = [tmp]
    while tmp != start:
        tmp = prev_d[tmp]
        continent_path += [tmp]
    print(continent_path)

    #1 2 2 2 2 2 3 # 2/3
    #1 2 2 1 2 2 3 # 2/3


    return

# Прямой проход - порталы не рассчитываются


#islands = map(int, input.split())
islands = list(map(int, '11 -86 -86 201 11 86 86 86 3 201'.split()))
print(get_time(islands))
'''
assert (get_time([2,3,4,2])) == 0

continents = [1, 1, 2, 2, 2, 3, 3]  # принадлежность островов к материкам
print(get_time(continents))
'''