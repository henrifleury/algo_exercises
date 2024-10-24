# https://coderun.yandex.ru/seasons/2024-summer/tracks/backend/problem/tiles?currentPage=1&pageSize=50&search=

INPUT_F = 'input.txt'

def main(f_name = INPUT_F):
    f = open(f_name, 'r')
    b, w = map(int, f.readline().split())
    half_p = b // 2
    for x in range(3, half_p):
        #print(half_p-x)
        y = half_p-x
        sq = (x-2)*y
        if sq == w:
            return x, y+2

    return b, w



if __name__ == '__main__':
    res = main()
    print(*(sorted(res)[::-1]))