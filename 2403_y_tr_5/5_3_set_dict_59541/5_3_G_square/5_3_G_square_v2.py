test_f_name = 'input.txt'
f = open(test_f_name, 'r')


n = int(f.readline())

vert_set = set()
vert_set.add(tuple(map(int, f.readline().split())))
dist_d2 = dict()
for i in range(1, n):
    new_v = tuple(map(int, f.readline().split()))
    if new_v not in vert_set:
        '''
        for v in vert_set:
            d2 = (new_v[0]-v[0])*(new_v[0]-v[0]) + (new_v[1]-v[1])*(new_v[1]-v[1])
            #print(d2, v, new_v, (new_v[0]-v[0])*(new_v[0]-v[0]), new_v[1]-v[1])
            if d2 not in dist_d2:
                dist_d2[d2] = []
            dist_d2[d2].append((v, new_v))
        '''
        vert_set.add(new_v)
vert_arr = sorted(vert_set)

# отсортировать словарь по длине списка
# не рассматривать короткие списки

from collections import Counter
def check_side(v1, v2):
    print(v1, v2)



if n==1:
    best = 1
else:
    best = 2
    for i, v1 in range(len(vert_arr)):
        for j in range(i, len(vert_arr)):

            next, square = check_side(vert_arr[i], vert_arr[j])
            if next > best:
                best = next
                best_square = square
                if best == 4:
                    break
print(4-best)
[print(*v) for v in best_square]




