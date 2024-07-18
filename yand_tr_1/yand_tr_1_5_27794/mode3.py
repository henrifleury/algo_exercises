def get_best_pair_slow(mayka_colors, shtany_colors):

    if mayka_colors[-1] <= shtany_colors[0]:
        return mayka_colors[-1], shtany_colors[0]
    if mayka_colors[0] >= shtany_colors[-1]:
        return mayka_colors[0], shtany_colors[-1]

    best_pair = (mayka_colors[0], shtany_colors[0])
    abs_min_dist = abs(mayka_colors[0] - shtany_colors[0])

    for i in mayka_colors:
        for j in shtany_colors:
            abs_dist = abs(i-j)
            if abs_dist < abs_min_dist:
                abs_min_dist = abs_dist
                best_pair = (i, j)
            #if abs_min_dist == 0:
                #break
        if abs_min_dist == 0:
            break
    return best_pair

def get_best_pair(seq1, seq2):
    #print(seq1, seq2)
    if seq1[-1] <= seq2[0]:
        return seq1[-1], seq2[0]
    if seq1[0] >= seq2[-1]:
        return seq1[0], seq2[-1]
    if seq1[0] == seq2[0]:
        return seq1[0], seq2[0]

    i, j = 0, 0
    max_i, max_j = len(seq1), len(seq2)
    min_dist = abs(seq1[i]-seq2[j]) #это точно не 0, проверили на входе равенство seq1[0] и seq2[0]
    best_pair = (min_dist, i, j)
    if seq1[0] < seq2[0]:
        i += 1
    else:
        j += 1

    while True:
        #print(i, j)
        cur_dist = abs(seq1[i] - seq2[j])
        if cur_dist < min_dist:
            min_dist = cur_dist
            best_pair = (min_dist, i, j)
            if cur_dist == 0:
                break
        if seq1[i] < seq2[j]:
            i += 1
        else:
            j += 1
        if i == max_i or j == max_j:
            break
    return seq1[best_pair[1]], seq2[best_pair[2]]


inp_list = []
with open("input.txt", "r") as f:
    for line in f.readlines():
        inp_list.append(line.strip())

mayka_nbr = int(inp_list[0])
mayka_colors = list(map(int, inp_list[1].split()))
shtany_nbr = int(inp_list[2])
shtany_colors = list(map(int, inp_list[3].split()))


print(*get_best_pair(mayka_colors, shtany_colors))
'''
import random
for i in range(100):
    n = random.randint(1, 5)
    mayka_colors = sorted(random.sample(range(1, 10), n))
    m = random.randint(1, 5)
    shtany_colors = sorted(random.sample(range(1, 10), m))
    print(len(mayka_colors), 'mayka_colors', *mayka_colors)
    print(len(shtany_colors), 'shtany_colors', *shtany_colors)
    slow = get_best_pair_slow(mayka_colors, shtany_colors)
    fast = get_best_pair(mayka_colors, shtany_colors)
    if slow != fast:
        print(slow, fast)
        break
'''
for f_name in ["input.txt", "input1.txt", "input2.txt", "input3.txt", "input4.txt"]:#
    inp_list = []
    with open(f_name, "r") as f:
        for line in f.readlines():
            inp_list.append(line.strip())

    mayka_nbr = int(inp_list[0])
    mayka_colors = list(map(int, inp_list[1].split()))
    # найти минимум майки
    # найти ближайшие штаны

    shtany_nbr = int(inp_list[2])
    shtany_colors = list(map(int, inp_list[3].split()))
    print(*get_best_pair(mayka_colors, shtany_colors))
