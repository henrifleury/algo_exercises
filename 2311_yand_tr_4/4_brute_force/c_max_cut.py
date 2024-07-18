f = open('input.txt', 'r')
n = int(f.readline())
e_arr, e_sum = [], 0

for i in range(n):
    e_arr.append(list(map(int, f.readline().split())))
    e_sum += sum(e_arr[-1][:i+1])


#group_a = set()
#group_b = set()


group_num = [1 for i in range(n)]
group_nbr = 2
#print(group_num, e_sum)

def group_permutate(i, edge_sum):
    global max_edge_sum, max_group_num
    #print(i, group_num, edge_sum)
    if i <n-1:

        group_permutate(i + 1, edge_sum)
        group_num[i] = 2
        delta_edge = 0 #TODO
        #for v_idx, w in e_arr[i][:i]:
        for v_idx in range(i):
            if group_num[v_idx] == 1:
                delta_edge += e_arr[i][v_idx]
            else:
                delta_edge -= e_arr[i][v_idx]

        for v_idx in range(i+1, n):
            #if group_num[v_idx] == 1:
            delta_edge += e_arr[i][v_idx]


        #for v_idx in e_arr[i][i+1:]:
        if edge_sum + delta_edge > max_edge_sum:
            max_edge_sum = edge_sum + delta_edge
            max_group_num = [gr_n for gr_n in group_num]
        group_permutate(i + 1, edge_sum+delta_edge)
        group_num[i] = 1

    else:
        #print(group_num)
        #print(group_num, max_edge_sum)
        group_num[i] = 2
        delta_edge = 0
        for v_idx in range(i+1):
            if group_num[v_idx] == 1:
                delta_edge += e_arr[i][v_idx]
            else:
                delta_edge -= e_arr[i][v_idx]
                #print(v_idx, "delta_edge", delta_edge, "i", i)
        if edge_sum + delta_edge > max_edge_sum:
            max_edge_sum = edge_sum + delta_edge
            max_group_num = [gr_n for gr_n in group_num]

        #print(group_num, edge_sum, max_edge_sum)
        group_num[i] = 1

max_edge_sum = 0
max_group_num = []
group_permutate(0, 0)
print(max_edge_sum)
print(" ".join(map(str, max_group_num)))

"""
e_len_d = dict()
for i, e_weights in enumerate(e_arr):
    for j, weight in enumerate(e_weights[:i]):
        if weight in e_len_d:
            e_len_d[weight].append((i,j))
        else:
            e_len_d[weight] = [(i, j)]

e_len_d = {k: e_len_d[k] for k in sorted(e_len_d, reverse=True)}
#print(e_len_d)

for k in e_len_d.keys():
    for v in e_len_d[k]:
        if v not in group_a:
            group_a.add(v)"""