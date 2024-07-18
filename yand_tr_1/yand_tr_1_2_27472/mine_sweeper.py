'''n, m, mines_nbr = map(int, input().split())
mine_coord = []
for i in range(mines_nbr):
    tmp_s=input()
    mine_coord.append(list(map(int, tmp_s.split())))'''
def get_zero_pole(n,m):
    return [[0 for j in range(m)] for i in range(n)]

def get_mine_pole(n, m, mine_coord_l):
    pole = get_zero_pole(n,m)
    if len(mine_coord_l)==0:
        return pole
    #print(pole)

    mines_set=set()
    for mine_x, mine_y in mine_coord_l:
        mine_x, mine_y = mine_x-1, mine_y-1 #координаты мин начинаются с 1
        if (mine_x, mine_y) in mines_set:
            continue
        mines_set.add((mine_x, mine_y))
        for i in range(max(0, mine_x-1), min(n-1, mine_x+1)+1):
            for j in range(max(0, mine_y - 1), min(m-1, mine_y + 1)+1):
                #print(i,j)
                pole[i][j] += 1
        #print(mine_x, mine_y, pole)
    for mine_x, mine_y in mine_coord_l:
        mine_x, mine_y = mine_x - 1, mine_y - 1  # координаты мин с 1
        pole[mine_x][mine_y] = "*"
    return pole


assert get_mine_pole(2,3,[]) == [[0, 0, 0], [0, 0, 0]]
assert get_mine_pole(3,2,[[1, 1], [2, 2]]) == [["*",2], [2, "*"], [1, 1]]
assert get_mine_pole(4,4,[[1, 3], [2, 1], [4, 2], [4, 4]]) == [[1,2,"*",1], ["*",2,1,1], [2,2,2,1], [1, "*", 2, "*"]]

res = get_mine_pole(3,2,[[1, 1], [2, 2]])
for s in res:
    print(" ".join([str(w) for w in s]))
