# https://coderun.yandex.ru/seasons/2024-summer/tracks/backend/problem/work-schedule?currentPage=1&pageSize=50&search=

#INPUT_F = 'input.txt'
INPUT_F = '430_input_20000.txt'
#ASSERTION_F = False
ASSERTION_F = True
GENERATION_F = False #True #False


def get_res(task_nbr, tasks):
    task_d = dict()
    for tsk in tasks:
        t_lim, stress = tsk
        if t_lim in task_d:
            task_d[t_lim].append(stress)
        else:
            task_d[t_lim] = [stress]
    backlog = []
    t_limits = sorted(task_d.keys(), reverse=True)
    for cur_id, cur in enumerate(t_limits):
        if cur > task_nbr:
            backlog += task_d[cur]
            cur_id += 1
        else:
            break
    if cur_id >= len(task_d):
        return 0
    backlog = sorted(backlog, reverse=True)
    # сейчас в бэклоге задачи, которые можно выполнять в любой день,
    # а t указывает на первый срок, меньший task_nbr
    if not backlog: cur_id = 0
    prev = task_nbr+1
    for cur_id in range(max(0, cur_id), len(t_limits)):
        cur = t_limits[cur_id]
        backlog = backlog[prev - cur - 1:]
        backlog = sorted(task_d[cur] + backlog, reverse=True)
        backlog.pop(0)
        prev = cur
    if prev > 1:
        backlog = backlog[prev - 1:]
    return sum(backlog)

def main(f_name = INPUT_F):
    f = open(f_name, 'r')
    task_nbr = int(f.readline())
    tasks = []
    for i in range(task_nbr):
        tasks.append(map(int, f.readline().split()))
    return get_res(task_nbr, tasks)

if __name__ == '__main__':
    res = main()
    print(res)


import time
start_time = time.time()  # время начала выполнения
if __name__ == '__main__':
    res = main()
    print(res)
end_time = time.time()  # время окончания выполнения
execution_time = end_time - start_time  # вычисляем время выполнения
print(f"Время выполнения программы: {execution_time} секунд")

if GENERATION_F:
    def generate_test_data(n=20000, f_name='430_input_20000.txt'):
        import random
        f = open(f_name, 'w')
        f.write(str(n)+'\n')
        for i in range(n):
            f.write(f'{str(random.randint(1, n+n//10))} {str(random.randint(1, 20))}\n')
        f.write('\n')
        return
    generate_test_data()

if ASSERTION_F:
    assert get_res(3, ((2, 4), (3, 1), (2, 3))) == 0
    assert get_res(3, ((5, 2), (5, 3), (5, 1))) == 0
    assert get_res(3, ((1, 4), (3, 1), (1, 3))) == 3
    assert get_res(3, ((1, 4), (3, 1), (1, 3))) == 3
    assert get_res(3, ((1, 2), (1, 3), (3, 1))) == 2
    assert get_res(3, ((1, 2), (1, 3), (1, 1))) == 3
    assert get_res(4, ((3, 5), (2, 7), (3, 9), (2, 8))) == 5
    assert get_res(6, ((1, 10), (2, 100), (2, 100), (3, 1000), (3, 1000), (3, 1000))) == 210
    assert get_res(5, ((1, 2), (2, 10), (4, 5), (8, 12), (9, 10))) == 0

