test_f_name = 'input.txt'
f = open(test_f_name, 'r')

#txt_file = f.readlines()
n = int(f.readline())

desk_size = 8
neigh_h, neigh_w = (-1, 1), (-1, 1)
desk = [[1]*(desk_size+2) for i in range(desk_size+2)]
#for i in range(8): desk.append([0]+[1]*8+[0])

#print(desk)
drill_cells = []
for i in range(n):
    hole = list(map(int, f.readline().split()))
    drill_cells.append(hole)
    desk[hole[0]][hole[1]] = 0
    #print(hole)
    #print(desk)


#[print(s) for s in desk]



def get_border_len(drill_cells):
    perimeter = 0
    for cell in drill_cells:
        for dh in neigh_h:
            perimeter += desk[cell[0] + dh][cell[1]]
        for dw in neigh_w:
            perimeter += desk[cell[0]][cell[1] + dw]
    return perimeter

print(get_border_len(drill_cells))
