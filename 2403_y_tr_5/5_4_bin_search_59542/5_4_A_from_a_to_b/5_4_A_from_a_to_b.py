test_f_name = 'input.txt'
f = open(test_f_name, 'r')


n = int(f.readline())
arr = sorted(map(int,f.readline().split()))

def search_x(x):
    l, r = 0, len(arr)
    while l<r:
        cur = (l+r)//2
        #print( x, 'l,r,x, cur, arr[cur]', l, r, cur, arr[cur], arr[cur] > x)
        if arr[cur] >= x:
            r = cur
        else:
            l = cur+1
    #print('l,r,x ex', l, r, x)
    return l

def search_y(x):
    l, r = 0, len(arr)
    while l<r:
        cur = (l+r)//2
        #print( x, 'l,r,x, cur, arr[cur]', l, r, cur, arr[cur], arr[cur] > x)
        if arr[cur] > x:
            r = cur
        else:
            l = cur+1
    #print('l,r,x ex', l, r, x)
    return l

def count_interval(a, b):
    a_idx = search_x(a)
    b_idx = search_y(b)
    #print(a_idx, b_idx)
    #print('a_idx', a_idx)
    return b_idx - a_idx



n_q = int(f.readline())

for i in range(n_q):
    a, b = list(map(int,f.readline().split()))
    print(count_interval(a, b))
    #break
