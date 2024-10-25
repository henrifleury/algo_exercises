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
#import heapq
from collections import deque, defaultdict

def get_best_path(continents: list):
    start_cont, fin_cont = continents[0], continents[-1]
    if start_cont == fin_cont:
        return 0 if len(continents) == 1 else 1

    # можно сократить подряд идущие несколько островов одного континента до 2

    n = len(continents)

    continent_map = defaultdict(list)
    for i in range(n):
        continent_map[continents[i]].append(i)

    visited = [False] * n
    distance = [0] * n
    q = deque()
    q.append(0)
    visited[0] = True

    visited_continent = defaultdict(bool)

    while q:
        cur_idx = q.popleft()
        if cur_idx == n-1:
            return distance[cur_idx]

        if cur_idx > 0 and not visited[cur_idx-1]:
            visited[cur_idx-1] = True
            distance[cur_idx-1] = distance[cur_idx] + 1
            q.append(cur_idx-1)

        if cur_idx < n-1 and not visited[cur_idx+1]:
            visited[cur_idx+1] = True
            distance[cur_idx+1] = distance[cur_idx] + 1
            q.append(cur_idx+1)

        cont = continents[cur_idx]
        if not visited_continent[cont]:
            for island in continent_map[cont]:
                if not visited[island]:
                    visited[island] = True
                    distance[island] = distance[cur_idx] + 1
                    q.append(island)
            visited_continent[cont] = True

#conts = map(int, input.split())
conts = list(map(int, '11 -86 -86 201 11 86 86 86 3 201'.split()))
print(get_best_path(conts))

assert (get_best_path([2, 2])) == 1
assert (get_best_path([2, 3, 2])) == 1
assert (get_best_path([2])) == 0

assert (get_best_path([2,3,4,2])) == 1

continents = [1, 1, 2, 2, 2, 3, 3]  # принадлежность островов к материкам
assert (get_best_path(continents)) == 5

continents = list(map(int, '3 2 5 2 5 2 5 3'.split()))
assert (get_best_path(continents)) == 1
assert (get_best_path([3, 5, 2, 2, 5])) == 2