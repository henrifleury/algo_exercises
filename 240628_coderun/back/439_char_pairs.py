# https://coderun.yandex.ru/seasons/2024-summer/tracks/backend/problem/couple-of-letters

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

def main(words):
    pairs: dict = dict()
    for w in words:
        w_len = len(w)
        if w_len > 1:
            for i in range(1, w_len):
                p = w[i-1:i+1]
                if p in pairs:
                    pairs[p] += 1
                else:
                    pairs[p] = 1
    max_freq = max(pairs.values())
    freq_pairs = [p for p in pairs.keys() if pairs[p]==max_freq]
    return sorted(freq_pairs)[-1]


if __name__ == '__main__':
    f = open(INPUT_F, 'r')
    words: list = f.readline().strip().split()
    print(main(words))
