test_f_name = 'input.txt'
f = open(test_f_name, 'r')


n = int(f.readline())
#arr = sorted(map(int,f.readline().split()))


def get_max_ship():
    l,r = 0, n
    while l < r:
        m = (l+r+1)//2
        size = 0
        n_sh = 1
        for i in range(1, m+1)[::-1]:
            size += n_sh*i+n_sh
            n_sh +=1
            #print(i, size)
        size -= 1
        if size>n:
            r = m-1
        else:
            l = m


    return l

print(get_max_ship())
