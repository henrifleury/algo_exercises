f = open('input.txt', 'r')
"""n = int(f.readline())
rel_power_l = list(map(int, f.readline().split()))
#arr_a = list(map(int, f.readline().split()))

rel_d = dict()
for pow in rel_power_l:
    rel_d[pow] = rel_d.get(pow,0)+1

rel_d = {k:rel_d[k] for k in sorted(rel_d)}
print(rel_d)
"""

n = int(input())
rel_power_l = list(map(int, f.readline().split()))
