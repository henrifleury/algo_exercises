test_f_name = 'input.txt'
f = open(test_f_name, 'r')
l,x1,v1,x2,v2  = list(map(int, f.read().strip().split()))
#print(l,x1,v1,x2,v2)

def get_equal_distance(l,x1,v1,x2,v2):
    if (abs(x1) == abs(x2)) or (abs(x1) == (l-abs(x2))):
        return ('YES', 0.)
    else:
        if v1 == v2 == 0:# уже проверено and x1!=x2:
            return ('NO', )

    if v1*v2 == 0: #случай когда обе скорости равны 0 уже проверили
        (x_fixed, x, v) = (x1, x2, v2) if v1 == 0 else (x2, x1, v1)
        #x_fixed = x1 if v1 == 0 else x2
        if x_fixed == 0:
            #t = (l-x)/v if x > 0 else -x/v
            t_list = [ - x / v, (l - x) / v, (-l - x) / v]
            # return ('YES', t)
        else:
            #y = abs(l-x_fixed)
            #t_list = [(l-x-y)/v, (l+y-x)/v]
            t_list = [(l - x_fixed - x) / v, (x_fixed - x) / v]
        '''            
        elif abs(v1) == abs(v2):
            v=abs(v1)
            t_list = [() / , () / ]
        '''
    else:
        t_list = []
        if v1 != v2:
            t_list.append((x2 - x1) / (v1 - v2))
            t_list.append((x2 - x1 - l) / (v1 - v2))

        if v1 != -v2:
            t_list.append((-x2 - x1) / (v1 + v2))
            t_list.append((l - x2 - x1) / (v1 + v2))
            t_list.append((2 * l - x2 - x1) / (v1 + v2))
            t_list.append((x1 + x1 - 2 * l) / (v1 + v2))


    print(t_list)
    t_list = [t for t in t_list if t>=0]
    if not t_list:
        return ('NO',)
    t = min(t_list)
    return ('YES', t)

res = get_equal_distance(l,x1,v1,x2,v2)
[print(s) for s in res]

assert get_equal_distance(6, 3, 1, 1, 1) == ('YES', 1.)
assert get_equal_distance(12, 8, 10, 5, 20) == ('YES', .3)
assert get_equal_distance(5, 0, 0, 1, 2) == ('YES', 2.)
assert get_equal_distance(10, 7, -3, 1, 4)[1]-.8571428571 < 1e-9
assert get_equal_distance(615143346, 79387687, -80123649, 306422480, -80123649) == ('YES', 2.4075923389360363)
assert get_equal_distance(948744004, 861724643, 848773505, 584154450, 730556189) == ('YES', 0.2859497397634569)
assert get_equal_distance(55444931, 17419156, 0, 53245822, -398046024) == ('YES', 0.03823690247437316)
assert get_equal_distance(72036282, 55132452, -373561948, 11464466, -887525183) == ('YES', 0.026808345885816515)
assert get_equal_distance(956390104, 549514100, 7, 315097830, -7) == ('YES', 51569559.5714285714)



# print([d/7 for d in [956390104, 549514100, 7, 315097830, -7]])
