import random

tasks = ['tennis', 'coding', 'reading']

ten_cod_trhd = 2/3
cod_ten_trhd = 7/8
r_ten_trhd = 3/4

cur_task = random.choice(tasks)
#task_counter_d[cur_task] += 1

res_list = []
n_exp = int(1e7)
for i in range(100):
    exp_counter = 0
    task_counter_d = {k: 0 for k in tasks}
    while exp_counter<n_exp:
        task_counter_d[cur_task] += 1
        exp_counter += 1
        next_task_proba = random.random()
        #print(cur_task, task_counter_d, next_task_proba)
        if cur_task == 'tennis':
            if next_task_proba <= ten_cod_trhd:
                cur_task = 'coding'
            else:
                cur_task = 'reading'
        elif cur_task == 'coding':
            if next_task_proba <= cod_ten_trhd:
                cur_task = 'tennis'
            else:
                cur_task = 'reading'
        elif cur_task == 'reading':
            if next_task_proba <= r_ten_trhd:
                cur_task = 'tennis'
            else:
                cur_task = 'coding'

    #print(exp_counter, task_counter_d['tennis'])
    #print(task_counter_d['tennis'] / exp_counter)
    res_list.append(task_counter_d['tennis'] / exp_counter)

    print(res_list)
print(sum(res_list)/len(res_list))