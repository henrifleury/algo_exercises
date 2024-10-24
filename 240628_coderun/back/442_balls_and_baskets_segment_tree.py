#https://coderun.yandex.ru/seasons/2024-summer/tracks/backend/problem/balls-and-baskets?currentPage=1&pageSize=50&search=
# https://habr.com/ru/articles/721086/
INPUT_F = 'input.txt'
#ASSERTION_F = False
ASSERTION_F = True
GENERATION_F = False #True #False
MODULO = 10**9+7

tree = []

def build_tree(arr, v, tl, tr):
    #print(v, tl, tr, tree)
    if tl==tr:
        tree[v] = arr[tl]
        pass
    else:
        tm = (tl + tr) // 2
        build_tree(arr, v * 2, tl, tm)
        build_tree(arr, v * 2+1, tm+1, tr)
        tree[v] = tree[v*2] * tree[v*2+1]
def prod(v, tl, tr, l, r):
    if l > r:
        return 1
    if (l == tl) & (r == tr):
        return tree[v]
    tm = (tl + tr) / 2;
    return prod(v * 2, tl, tm, l, min(r, tm))
    + prod(v * 2 + 1, tm + 1, tr, max(l, tm + 1), r);

'''
def update_segment(arr, v, tl, tr, l, r):
    if (l==tl) & (r==tr):
        tree[v] = arr[l]
        return
    tm = (tl+tr)//2
    if l <= tm:
        update_segment(arr, v*2, tl, tm, l, min(r,tm))
    if r > tm:
        update_segment(arr, v * 2+1, tm+1, tr, max(l,tm), r)
    tree[v] = tree[v * 2] * tree[v * 2 + 1]
'''
def main(f_name = INPUT_F):
    global tree
    f = open(f_name, 'r')
    n = int(f.readline())

    balls = list(map(int, f.readline().split()))
    print('balls', balls)
    tree = [1]*4*n

    #print(tree)


    q_n = int(f.readline())

    for i in range(q_n):
        q, l, r = map(int, f.readline().split())
        #print(balls, q, l, r, balls, tree)
        if q:
            #print('prod , l, r ', q, l, r, balls[l-1:r])
            build_tree(balls, 1, 0, n - 1)  # len(balls)-1)
            print(balls, q, l, r, tree)
            res = prod(1, 0, n-1, l-1, r-1)
            print(res % MODULO)
        else:
            #print(balls, 'refresh , l, r ', q, l, r, balls[l - 1:r])
            #balls = balls[:l-1] +[j+1 for j in balls[l-1:r]] + balls[r:]
            for i in range(l-1, r):
                balls[i] += 1
            print(q, l, r,balls)
            #print('refresh , l, r ', q, l, r, balls)
            #update_segment(balls, 1, 0, n-1, l-1, r - 1)  # len(balls)-1)
            #print(balls, 'build_tree1 , l, r ', tree)
            #print()
            continue


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

