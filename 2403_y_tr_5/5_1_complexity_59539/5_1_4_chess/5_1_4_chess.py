test_f_name = 'input.txt'
f = open(test_f_name, 'r')
desk = []
beat_field = []
for i in range(8):
    desk.append(f.readline()[:8])
    beat_field.append([0]*8)
#print('desk', desk, len(desk))

#положим начало координат в левом верхнем углу
def rook_beat(row_n, col_n):
    # обход вверх
    #print('rook_beat(h, v)', row_n, col_n)
    for i in range(0, row_n)[::-1]:
        if desk[i][col_n] == '*':
            beat_field[i][col_n] = 1
        else:
            break
    # обход вниз
    for i in range(row_n+1, 8):
        if desk[i][col_n] == '*':
            beat_field[i][col_n] = 1
        else:
            break
    # обход к началу строки
    for i in range(0, col_n)[::-1]:
        if desk[row_n][i] == '*':
            beat_field[row_n][i] = 1
        else:
            break
    # обход к концу строки
    for i in range(col_n+1, 8):
        if desk[row_n][i] == '*':
            beat_field[row_n][i] = 1
        else:
            break


def bishop_beat(row_n, col_n):
    #print('bishop_beat(h, v)', row_n, col_n)
    # - -
    for h in range(1, min(row_n, col_n)+1):
        if desk[row_n-h][col_n-h] == '*':
            beat_field[row_n-h][col_n-h] = 1
        else:
            break
    # + -
    #print('min(col_n, 8-row_n)', min(col_n, 7-row_n))
    for h in range(1, min(col_n, 7-row_n)+1):
        #print(h, row_n+h, col_n-h)
        if desk[row_n+h][col_n-h] == '*':
            beat_field[row_n+h][col_n-h] = 1
        else:
            break
    # - +
    for h in range(1, min(row_n, 7-col_n)+1):
        if desk[row_n-h][col_n+h] == '*':
            beat_field[row_n-h][col_n+h] = 1
        else:
            break

    # + +
    for h in range(1, min(7-row_n, 7-col_n)+1):
        if desk[row_n+h][col_n+h] == '*':
            beat_field[row_n+h][col_n+h] = 1
        else:
            break



for i in range(8):
    for j in range(8):
        #print(i, j, desk[i][j])
        if desk[i][j] == "B":
            beat_field[i][j] = 1
            bishop_beat(i, j)
        elif desk[i][j] == "R":
            beat_field[i][j] = 1
            rook_beat(i, j)


#[print(s) for s in beat_field]
res = sum(sum(s) for s in beat_field)
print(8*8-res)