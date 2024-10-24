# https://coderun.yandex.ru/seasons/2024-summer/tracks/backend/problem/two-teams

# import sys

INPUT_F = 'input.txt'


def main(a, b, n):

    max_tm_a = a
    min_tm_b = (b+n-1) // n

    if max_tm_a > min_tm_b:
        return 'Yes'
    else:
        return 'No'

if __name__ == '__main__':
    f = open(INPUT_F, 'r')
    a, b, n = map(int, f.readlines())
    print(main(a, b, n))

assert main(10, 8, 2) == 'Yes'
#assert main(10, 8, 2) == 'Yes'