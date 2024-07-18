import heapq

def fast_dijkstra(num, graph_dict, start):
    dist = [float('inf')] * num
    dist[start] = 0
    pq = [(0, start)]

    while pq:
        current_distance, current_vertex = heapq.heappop(pq)

        if current_distance > dist[current_vertex]:
            continue

        for v, e in graph_dict[current_vertex]:
            new_distance = current_distance + e

            if new_distance < dist[v]:
                dist[v] = new_distance
                heapq.heappush(pq, (new_distance, v))

    return dist

def main():
    with open("input.txt", "r") as file:
        N = int(file.readline().strip())

        times = []
        matrix = []

        for line in file:
            rez = list(map(int, line.strip().split()))
            if len(rez) == 2:
                times.append(rez)
            else:
                matrix.append(rez)

    n = N
    transfer, velocity = zip(*times)

    graph = {i: [] for i in range(n)}
    distance_matrix = []

    for road in matrix:
        city_from, city_to, distance = road
        graph[city_from - 1].append((city_to - 1, distance))
        graph[city_to - 1].append((city_from - 1, distance))

    for current in range(n):
        distance_matrix.append(fast_dijkstra(n, graph, current))


    distance_matrix = [[distance_matrix[i][j] / velocity[i] + transfer[i] for j in range(n)] for i in range(n)]
    print(distance_matrix[14])

    distances = [float("inf")] * n
    min_values = [(0, 0, None)]
    visited = [False] * n
    previous = [None] * n

    while min_values:
        current_distance, current_vertex, prev = heapq.heappop(min_values)

        if visited[current_vertex]:
            continue

        visited[current_vertex] = True
        distances[current_vertex] = current_distance
        previous[current_vertex] = prev

        for i in range(n):
            if i != current_vertex:
                heapq.heappush(min_values, (distance_matrix[i][current_vertex] + current_distance, i, current_vertex))

    max_distance = max(distances)
    print(max_distance)

    way = [distances.index(max_distance)]
    while previous[way[-1]] is not None:
        way.append(previous[way[-1]])

    print(' '.join(map(lambda x: str(x + 1), way)))

if __name__ == "__main__":
    main()