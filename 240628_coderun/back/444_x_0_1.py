# https://coderun.yandex.ru/seasons/2024-summer/tracks/backend/problem/tic-tac-toe?currentPage=1&pageSize=50&search=
F_ASSERTION = True
INPUT_F = 'input9.txt'
WIN_LEN = 5

#проверку диагоналей можно бы сделать только для одного случая,
# а потом прогнать через нее же транспонированную матрицу

def main(f_name=INPUT_F):
    f = open(f_name, 'r')
    n, m = map(int, f.readline().split())
    pole = []

    #check rows on input
    for i in range(n):
        cur_str = f.readline().strip()
        if m >= WIN_LEN:
            prev = cur_str[0]
            seq_len = 1
            for s in cur_str[1:]:
                if s == prev:
                    seq_len += 1
                else:
                    if seq_len >= WIN_LEN:
                        if prev != '.':
                            return 'Yes'
                    prev, seq_len = s, 1
            if seq_len >= WIN_LEN:
                if prev != '.':
                    return 'Yes'
        pole.append(cur_str)

    #check diag 1
    if (n >= WIN_LEN) and (m >= WIN_LEN):
        if m >= WIN_LEN:
            for row_n in range(n-WIN_LEN+1):
                prev = pole[row_n][0]
                seq_len = 1
                for col_n in range(1, min(m,n-row_n)):
                    s = pole[row_n + col_n][col_n]
                    if s == prev:
                        seq_len += 1
                    else:
                        if seq_len >= WIN_LEN:
                            if prev != '.':
                                return 'Yes'
                        prev, seq_len = s, 1
                    #print(row_n+col_n, col_n, prev, seq_len)
                #print('******')

                if seq_len >= WIN_LEN:
                    if prev != '.':
                        return 'Yes'

        if n >= WIN_LEN:
            for col_n in range(m-WIN_LEN+1):
                prev = pole[0][col_n]
                seq_len = 1
                for row_n in range(1, min(n, m-col_n)):
                    s = pole[row_n][col_n+row_n]
                    if s == prev:
                        seq_len += 1
                    else:
                        if seq_len >= WIN_LEN:
                            if prev != '.':
                                return 'Yes'
                        prev, seq_len = s, 1
                    # print(row_n+col_n, col_n, prev, seq_len)
                    # print('******')

                if seq_len >= WIN_LEN:
                    if prev != '.':
                        return 'Yes'

        #check diag 1
        if m >= WIN_LEN:
            for row_n in range(WIN_LEN-1, n):
                prev = pole[row_n][0]
                seq_len = 1
                for col_n in range(1, min(m, row_n+1)):
                    s = pole[row_n - col_n][col_n]
                    if s == prev:
                        seq_len += 1
                    else:
                        if seq_len >= WIN_LEN:
                            if prev != '.':
                                return 'Yes'
                        prev, seq_len = s, 1
                    #print(row_n - col_n, col_n, prev, seq_len)
                #print('******')

                if seq_len >= WIN_LEN:
                    if prev != '.':
                        return 'Yes'

        if n >= WIN_LEN:
            #for col_n in range(WIN_LEN-1, m):
            for col_n in range(1, m-WIN_LEN+1):
                prev = pole[1][n-1]
                seq_len = 1
                #for row_n in range(1, min(n, col_n)):
                #a = n - col_n + 1
                a = m - col_n
                for shift in range(1, min(n, a)):
                    row_id = n - 1 - shift
                    col_id = col_n + shift
                    s = pole[row_id][col_id]
                    if s == prev:
                        seq_len += 1
                    else:
                        if seq_len >= WIN_LEN:
                            if prev != '.':
                                return 'Yes'
                        prev, seq_len = s, 1
                    # print(row_n+col_n, col_n, prev, seq_len)
                # print('******')

                if seq_len >= WIN_LEN:
                    if prev != '.':
                        return 'Yes'
    # check columns
    if n >= WIN_LEN:
        transposed = map(list, zip(*pole))
        #print(f_name, 'transposed')
        #print(pole)
        #print(f_name, list(transposed))
        for cur_str in transposed:
            prev = cur_str[0]
            seq_len = 1
            for s in cur_str[1:]:
                if s == prev:
                    seq_len += 1
                else:
                    if seq_len >= WIN_LEN:
                        if prev != '.':
                            return 'Yes'
                    prev, seq_len = s, 1
            if seq_len >= WIN_LEN:
                if prev != '.':
                    return 'Yes'

    return 'No'

if __name__ == '__main__':
    print(main(INPUT_F))

if F_ASSERTION:
    # assertion for WIN_LEN = 4
    assert main('input1.txt') == 'No'
    assert main('input2.txt') == 'Yes'
    assert main('input3.txt') == 'Yes'
    assert main('input4.txt') == 'Yes'
    assert main('input5.txt') == 'Yes'
    assert main('input6.txt') == 'Yes'
    assert main('input7.txt') == 'Yes'
    assert main('input8.txt') == 'Yes'
    assert main('input9.txt') == 'Yes'