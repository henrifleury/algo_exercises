# https://coderun.yandex.ru/seasons/2024-summer/tracks/backend/problem/crystals

INPUT_F = 'input.txt'


def parse(s):
    s = '_' + s
    char_seq = ''
    char_count = []

    for i in range(1, len(s)):
        if s[i] != s[i - 1]:
            char_seq += s[i]
            char_count += [1]
        else:
            char_count[-1] += 1
    return char_seq, char_count

def mid(a, b, c):
    return a + b + c - min(a, b, c) - max(a, b, c)

def main(s1, s2, s3):
    res = ''
    ch_seq_1, ch_count_1 = parse(s1)
    ch_seq_2, ch_count_2 = parse(s2)
    ch_seq_3, ch_count_3 = parse(s3)

    if ch_seq_1 == ch_seq_2 == ch_seq_3:

        for i, ch in enumerate(ch_seq_1):
            res += ch * mid(ch_count_1[i], ch_count_2[i], ch_count_3[i])
    else:
        res = 'IMPOSSIBLE'


    return res

if __name__ == '__main__':
    f = open(INPUT_F, 'r')
    s1  = f.readline().strip()
    s2 = f.readline().strip()
    s3 = f.readline().strip()
    print(main(s1, s2, s3))
