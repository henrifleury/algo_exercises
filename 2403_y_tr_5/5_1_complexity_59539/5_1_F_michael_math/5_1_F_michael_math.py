test_f_name = 'input.txt'
f = open(test_f_name, 'r')
n = int(f.readline())
arr = list(map(int, f.readline().split()))
res = arr[0]
odd_counter = res % 2
for i in range(1, n):
    next = arr[i]
    odd_counter += next %2
    #print(odd_counter, next %2, res % 2)
    if odd_counter<=1:
        print('+', end='')
        res += next
    else:
        print('x', end='')
        res *= next
        odd_counter = 1
