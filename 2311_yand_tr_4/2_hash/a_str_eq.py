f = open('input.txt', 'r')
s = f.readline().strip()
n = int(f.readline())

for _ in range(n):
    l, a, b = tuple(map(int, f.readline().split()))
    print(l, a, b)
    #print(l,a,b)
#arr_a = list(map(int, f.readline().split()))

