import random
f = open('input.txt', 'r')

n = int(f.readline().strip())
pr_list = list()
for idx in range(n):
    pr_list.append(list(map(int, f.readline().split())))
    #print(list(map(int, f.readline().split())))

cube_nbrs = [i for i in range(n)]
cube_score_ids = [i for i in range(6)]

n_exp = int(1e4)

exp_counter = 0
res_counter = 0
res_counter_2 = 0
while exp_counter<n_exp:
    exp_counter += 1
    cube1_id, cube2_id = random.sample(cube_nbrs, k=2)
    cube_1 = pr_list[cube_nbrs[cube1_id]]
    cube_1_choice = random.choice(cube_score_ids)
    cube_1_score = cube_1[cube_1_choice]

    cube_2 = pr_list[cube_nbrs[cube2_id]]
    cube_2_choice = random.choice(cube_score_ids)
    cube_2_score = cube_2[cube_2_choice]

    res_score = max(cube_1_score, cube_2_score)
    res_counter += res_score * res_score * res_score
    res_counter_2 += res_score
    #print(res_counter_1, res_counter_2)
    #print(cube1_id, cube_1, cube_1_choice, cube_1_score)


    # res_counter +=


#print(res_counter_1/n_exp + res_counter_2/n_exp)
print(res_counter/n_exp)
res_counter_2 = res_counter_2/n_exp
print(res_counter_2*res_counter_2*res_counter_2)