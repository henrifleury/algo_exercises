# 1 2 3
# 1123

arr = set(map(int, input().split()))
n = int(input())

#arr = set(map(int, "1 2 3".split()))
#n = 1123

digs = set()
while n>0:
    digs.add(n%10)
    n = n//10

print(len(digs-arr))

