inp_list = []
with open("input.txt", "r") as f:
    #for line in f.readlines():
        #inp_list.append(line.strip())
    n, r = map(int, f.readline().split())
    dist_l = list(map(int, f.readline().split()))

pair_count = 0
last = 0
for first in range(n):
    while last < n and dist_l[last] - dist_l[first] <= r:
        last += 1
    pair_count += n - last
print(pair_count)