# https://coderun.yandex.ru/seasons/2024-summer/tracks/backend/problem/biggest-square?currentPage=1&pageSize=50&search=

INPUT_F = 'input.txt'
#ASSERTION_F = False
ASSERTION_F = True
GENERATION_F = False #True #False

import heapq

def get_res(n, m, pole):
    max_row = []
    for i in range(n):
        cur_row = pole[i]
        row_sum = [0]
        for x in cur_row:
            if x:
                row_sum.append(row_sum[-1]+1)
            else:
                row_sum.append(0)
        max_row.append(row_sum)
    min_side = 0
    for i in range(n):
        if n-i < min_side:
            break
        for j in range(min_side, m+1):
            cur = max_row[i][j]
            if cur>min_side:
                max_k = min(i+cur, n)
                sq_set = set()
                for k in range(i, max_k):
                    if max_row[k][j]>min_side:
                        sq_set.add(max_row[k][j])
                    else:
                        if k-i>min_side:
                            min_side = min(k - i, cur, min(sq_set))
                            sq_coords = (i + 1, j - min_side + 1)
                        break
                else:
                    min_side = min(max_k-i, cur, min(sq_set))
                    sq_coords = (i+1, j-min_side+1)
    return min_side, sq_coords





    '''
    for i in range(1, m):
        prev = 0
        cur_len = 0
        for j in range(m):
            cur = max_row[j][i]
    '''



    return max_row

def main(f_name = INPUT_F):
    f = open(f_name, 'r')
    n, m = map(int, f.readline().split())
    pole = []
    for i in range(n):
        pole.append(map(int, f.readline().split()))
    return get_res(n, m, pole)

if __name__ == '__main__':
    res = main()
    print(res[0])
    print(*res[1])
