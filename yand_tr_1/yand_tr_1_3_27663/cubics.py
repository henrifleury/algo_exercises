ann_d, bor_d = dict(), dict()
'''n, m = map(int, input().split())


for i in range(n):
    color = int(input())
    ann_d[color] = ann_d.get(color, 0)+1
for i in range(m):
    color = int(input())
    bor_d[color] = bor_d.get(color, 0) + 1
'''

for color in [1, 2]:
    ann_d[color] = ann_d.get(color, 0)+1
for color in [2, 3]:
    bor_d[color] = bor_d.get(color, 0) + 1

ann_colors = set(ann_d.keys())
bor_colors = set(bor_d.keys())
common_colors = set(ann_colors & bor_colors)
#print(ann_d, bor_d, common_colors)
print(len(common_colors))
print(*sorted(common_colors))
only_ann_colors = ann_colors - common_colors
only_bor_colors = bor_colors - common_colors
print(len(only_ann_colors))
print(*sorted(only_ann_colors))
print(len(only_bor_colors))
print(*sorted(only_bor_colors))

