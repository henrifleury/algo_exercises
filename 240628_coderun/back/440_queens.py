# https://coderun.yandex.ru/seasons/2024-summer/tracks/backend/problem/couple-of-letters

INPUT_F = 'input.txt'

def main(words):
    q_sum = 0
    for i, q_n in enumerate(sorted(q_nbrs)):
        q_sum += q_n
        if q_sum > 4:
            return 4-i
    if q_sum >=2 :
        return 0
    else:
        return 1



if __name__ == '__main__':
    f = open(INPUT_F, 'r')
    q_nbrs: list = map(int, f.readline().strip().split())
    print(main(q_nbrs))
