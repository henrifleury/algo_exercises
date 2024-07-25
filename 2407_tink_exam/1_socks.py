f = open('input.txt', 'r')

'''
s = ""
n = 100000
for i in range(n):
    #if i%100000 == 0:
        # print(i)
    s += str(i) + ' '

with open('input.txt', 'w') as f:
    f.write(str(n)+'\n')
    f.write(s)
'''


#_ = int(f.readline())
#socks_n: list = map(int, f.readline().split())
_ = int(input())
socks_n: list = map(int, input().split())
rest = 0

for n in socks_n:
    rest += n % 2

if rest % 2:
    print('NO')
else:
    print('YES')

