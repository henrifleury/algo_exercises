#https://coderun.yandex.ru/seasons/2024-summer/tracks/backend/problem/balls-and-baskets?currentPage=1&pageSize=50&search=

INPUT_F = 'input.txt'
#ASSERTION_F = False
ASSERTION_F = True
GENERATION_F = False #True #False
MODULO = 10**9+7

import heapq

def get_res(balls, queries):
    for q, l, r in queries:
        #print(q, l, r, balls)
        if q:
            res = balls[l]
            for i in range(l+1, r+1):
                res *= balls[i]
            print(res % MODULO)
        else:
            for i in range(l, r + 1):
                balls[i] += 1
        #print(balls)
    return res

def main(f_name = INPUT_F):
    f = open(f_name, 'r')
    n = int(f.readline())
    balls = [0] + list(map(int, f.readline().split()))
    q_n = int(f.readline())
    queries = []
    for i in range(q_n):
        queries.append(map(int, f.readline().split()))
    return get_res(balls, queries)

if __name__ == '__main__':
    res = main()
    #print([i for i in res])

'''

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
'''

