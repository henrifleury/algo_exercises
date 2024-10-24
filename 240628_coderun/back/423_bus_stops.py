# https://coderun.yandex.ru/seasons/2024-summer/tracks/backend/problem/two-teams

# import sys

INPUT_F = 'input.txt'


def main(a_l, f):
    r_start = len(a_l)
    for k in map(int, f.readline().split()):
        l, r = 0, r_start
        min_dist = k - a_l[l]
        while l<r:
            cur = (l+r) // 2


    pass



if __name__ == '__main__':
    f = open(INPUT_F, 'r')
    n, k  = map(int, f.readline().split())
    a_l = map(int, f.readline().split())
    main(a_l, f)

    #print(main(a, b, n))

# assert main(10, 8, 2) == 'Yes'
# assert main(10, 8, 2) == 'Yes'