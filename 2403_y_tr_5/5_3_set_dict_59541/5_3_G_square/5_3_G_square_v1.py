test_f_name = 'input.txt'
f = open(test_f_name, 'r')


n = int(f.readline())

vert_set = set()
vert_set.add(tuple(map(int, f.readline().split())))
dist_d2 = dict()
for i in range(1, n):
    new_v = tuple(map(int, f.readline().split()))
    if new_v not in vert_set:
        for v in vert_set:
            d2 = (new_v[0]-v[0])*(new_v[0]-v[0]) + (new_v[1]-v[1])*(new_v[1]-v[1])
            #print(d2, v, new_v, (new_v[0]-v[0])*(new_v[0]-v[0]), new_v[1]-v[1])
            if d2 not in dist_d2:
                dist_d2[d2] = []
            dist_d2[d2].append((v, new_v))
        vert_set.add(new_v)

# отсортировать словарь по длине списка
# не рассматривать короткие списки

from collections import Counter
def get_square(square, vert_l):
    res = 2
    #print('square', square)

    for v1, v2 in vert_l:
        new_v = False

        if v1 in square:
            new_v = v2
        elif v2 in square:
            new_v = v1
        if new_v:
            square.append(new_v)
            res += 1
            x_l = [v[0] for v in square]
            y_l = [v[1] for v in square]
            x_counter = Counter(x_l)
            y_counter = Counter(y_l)
            x_keys = list(x_counter.keys())
            next_x = x_keys[0] if x_counter[x_keys[0]] == 1 else x_keys[1]
            y_keys = list(y_counter.keys())
            next_y = y_keys[0] if y_counter[y_keys[0]] == 1 else y_keys[1]
            if (next_x, next_y) in vert_set:
                square.append((next_x, next_y))
                res += 1
                return res, square
    return res, square



best = 1
#best_square = vert_set[0]
for k, vert_l in dist_d2.items():
    #print(k)
    square = list(vert_l[0])
    next, square = get_square(square, vert_l[1:])
    #next = max(best, cur)
    if next > best:
        best = next
        best_square = square
        if best == 4:
            break
print(4-best)
[print(*v) for v in best_square]




