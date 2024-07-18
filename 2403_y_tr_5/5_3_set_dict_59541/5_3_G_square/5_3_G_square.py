test_f_name = 'input.txt'
f = open(test_f_name, 'r')


n = int(f.readline())

vert_d = dict()
for i in range(n):
    x, y = list(map(int, f.readline().split()))
    if x not in vert_d:
        vert_d[x] = set()
    vert_d[x].add(y)

def get_max_sq_perimeter():
    max_per = 0
    for x,v in vert_d.items():
        max_per += 1
        print(k,v)
        if y in vert_d:
            for next_x


get_max_sq_perimeter()