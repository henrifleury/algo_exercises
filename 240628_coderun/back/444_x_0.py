# https://coderun.yandex.ru/seasons/2024-summer/tracks/backend/problem/tic-tac-toe?currentPage=1&pageSize=50&search=
INPUT_F = 'input.txt'
WIN_LEN = 4

def main(f):
    n, m = map(int, f.readline().split())
    pole = []
    #check line on input
    for i in range(n):
        cur_str = f.readline().strip()
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
    for row_n in range(n-WIN_LEN+1):
        prev = pole[row_n][0]
        seq_len = 1
        for col_n in range(1, n-row_n):
            s = pole[row_n+col_n][col_n]
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


    for col_n in range(1, m-WIN_LEN+1):
        prev = pole[0][col_n]
        seq_len = 1
        for row_n in range(1, m-col_n):
            s = pole[row_n][col_n+row_n]
            if s == prev:
                seq_len += 1
            else:
                if seq_len >= WIN_LEN:
                    if prev != '.':
                        return 'Yes'
                prev, seq_len = s, 1
            print(row_n, row_n+col_n, prev, seq_len)
        print('******')

        if seq_len >= WIN_LEN:
            if prev != '.':
                return 'Yes'
    '''
    #check diag 2
    for row_n in range(WIN_LEN-1, n):
        prev = pole[row_n][0]
        seq_len = 1
        for col_n in range(1, n-row_n):
            s = pole[row_n+col_n][col_n]
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
    '''



    return False


if __name__ == '__main__':
    f = open(INPUT_F, 'r')
    print(main(f))
