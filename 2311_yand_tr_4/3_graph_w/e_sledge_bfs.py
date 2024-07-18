import heapq

f = open('input.txt', 'r')
n = int(f.readline().strip())
# в первой строке всегда будем считать 1 1, отбросим, n поправим чтоб старому
#city_time_to_ready, city_velosity = map(int, f.readline().split())
#ttready_d, vel_d = {0: city_time_to_ready}, {0: city_velosity}
ttready_d, vel_d = dict(), dict()
for i in range(1, n+1):
    ttready_d[i], vel_d[i] = map(int, f.readline().split())

max_dist, max_time = 3333333333, 5555555555
#dist_d = dict()
dist_arr = [[max_dist]*(n+1)for i in range(n+1)]
time_arr = [[max_time]*(n+1)for i in range(n+1)]
print(len(dist_arr), dist_arr)
#  в строке - город отправления, в столбцах - город прибытия
for i in range(1, n):
    a, b, l = map(int, f.readline().split())
    print(a, b, l)

    #if a!=1
    dist_arr[a][b] = l
    dist_arr[b][a] = l
    time_arr[a][b] = ttready_d[a] + l / vel_d[a]
    time_arr[b][a] = ttready_d[b] + l / vel_d[b]
    #if b!=1

    #break

print(dist_arr[11])

visited = [1]  # List to keep track of visited nodes.
for a in range(2, n+1):
    queue = []  # Initialize a queue
    
    visited.append(a)
    queue.append((a, [a]))
    print(a)
    while queue:
        b = queue.pop(0)
        #time = (ttready_d[a] + dist_arr[a][b] / vel_d[a], b)
        #print(b, end=" ")
        for neighbour, l in enumerate(dist_arr[b]):
            #if l != max_dist:
                print(neighbour, l, end="__")
                if neighbour not in visited:
                    visited.append(neighbour)
                    queue.append(neighbour)
    print()
    #break
