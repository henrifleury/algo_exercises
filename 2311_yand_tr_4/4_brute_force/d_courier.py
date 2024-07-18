f = open('input.txt', 'r')
n = int(f.readline())

def naive_check_vert(v_dist):
    #if sum(v_dist) <= 0:
        #return False
    not_zero_nbr = 0
    for v in v_dist:
        if v > 0:
            not_zero_nbr += 1
    if not_zero_nbr <= 1:
        return False
    return True


def read_arr(n):
    e_arr = []
    for i in range(n):
        new_dist = list(map(int, f.readline().split()))
        if naive_check_vert(new_dist):
            e_arr.append(new_dist)
        else:
            return False
    return e_arr

def permutate(v, unknown, cur_len):
    global min_path_len
    #print(v, unknown, cur_len)
    if len(unknown) == 0:
        next_len = e_arr[v][0]
        if next_len > 0:
            if cur_len+next_len < min_path_len:
                min_path_len = cur_len + next_len

    else:
        for next_v in unknown:
            next_len = e_arr[v][next_v]
            if next_len > 0:
                permutate(next_v, unknown - set([next_v]), cur_len+next_len)


if n == 0:
    print(0)
elif n == 1:
    print(int(f.readline()))
elif n == 2:
    print(list(map(int, f.readline().split()))[1]+list(map(int, f.readline().split()))[0])
else:
    e_arr = read_arr(n)
    if not e_arr:
        print(-1)
    else:
        max_path_len = sum(sum(l) for l in e_arr) + 100
        min_path_len = max_path_len
        for v in range(1, n):
        #for v in range(1, 2):
            cur_len = e_arr[0][v]
            if cur_len > 0:
                unknown = set([i for i in range(1, n)]) - set([v])
                permutate(v, unknown, cur_len)
        if min_path_len == max_path_len:
            print(-1)
        else:
            print(min_path_len)

