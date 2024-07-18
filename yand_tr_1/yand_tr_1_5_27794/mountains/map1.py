n = int(input())
a = [0, 0]
b = [0, 0]
x_prev, y_prev = -1, -1
for i in range(n):
    x, y = map(int, input().split())
    if x_prev == -1:
        x_prev = x
        y_prev = y
    elif y > y_prev:
        a.append(a[-1] + y - y_prev)
        b.append(b[-1])
        x_prev = x
        y_prev = y
    else:
        a.append(a[-1])
        b.append(b[-1] + y_prev - y)
        x_prev = x
        y_prev = y
m = int(input())
for i in range(m):
    x, y = map(int, input().split())
    if x < y:
        print(a[y] - a[x])
    else:
        print(b[x] - b[y])

