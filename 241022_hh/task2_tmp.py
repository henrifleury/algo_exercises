from collections import deque

def find_best_path(continents):
    n = len(continents)
    distances = [[] for _ in range(n)]
    print(distances, len(distances))

    for i in range(n - 1):
        distances[i].append(i + 1)
        distances[i + 1].append(i)
    print(distances)

    # Добавляем портальные соединения
    continent_islands = {}
    for i in range(n):
        if continents[i] not in continent_islands:
            continent_islands[continents[i]] = []
        continent_islands[continents[i]].append(i)
    print('continent_islands', continent_islands)

    for islands in continent_islands.values():
        for i in islands:
            for j in islands:
                if i != j:
                    distances[i].append(j)

    # BFS для поиска кратчайшего пути
    visited = [-1] * n
    queue = deque([0])  # Начинаем с первого острова
    visited[0] = 0

    while queue:
        current = queue.popleft()

        if current == n - 1:  # Достигли последнего острова
            return visited[current]

        for next_island in distances[current]:
            if visited[next_island] == -1:
                visited[next_island] = visited[current] + 1
                queue.append(next_island)

    return -1  # Если путь не найден


'''continents = [1, 1, 2, 2, 2, 3, 3]  # принадлежность островов к материкам
print(find_best_path(continents))


continents = list(map(int, '11 -86 -86 201 11 86 86 86 3 201'.split()))
print(find_best_path(continents))


continents = list(map(int, '3 2 5 2 5 2 5 3'.split()))
print(find_best_path(continents))
'''
continents = list(map(int, '3 5 2 2 5'.split()))
print(find_best_path(continents))
