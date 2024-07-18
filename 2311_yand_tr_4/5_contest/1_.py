f = open('input.txt', 'r')
n = int(f.readline())

#a = []
#b = []

def cet_c_x():
    i, j  = 2, 2
    #next_a, next_b = 1, 1
    #x = i
    c = [1]
    next_a, next_b = 4, 8
    delta = 0
    while i + delta <= n:
        print("start", i, "j", j, "next_a", next_a, "next_b",next_b)
        next_a = i * i
        if next_b <= next_a:
            if next_b != next_a:
                delta += 1
            c.append(next_b)
            next_b = j*j*j
            j += 1
        else:
            c.append(next_a)
        i += 1
        print(i, "delta", delta, i+delta,  c)
    """
    if i>n:
        return next_a
    else:
        if next_a<next_b:
            return next_b
    """
    #print((j-2)*(j-2)*(j-2))
    print(next_a, next_b)
    return min(next_a, (j-2)*(j-2)*(j-2))


if n<=1:
    print(1)
else:
    print(cet_c_x())
