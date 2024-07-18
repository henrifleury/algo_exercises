f = open('input.txt', 'r')
n = int(f.readline())

raw_busy = [True]+[False for i in range(n)]
col_busy = [True]+[False for i in range(n)]
d1_busy, d1_corr = [False for i in range(1+1, 2*n+1)], -2
d2_busy, d2_corr = [False for i in range(1-n, 1+n)], n-1

coord = []

def order_or_print(coord):
    global nbr
    #print(len(coord), coord, nbr)
    """    
    if len(coord)==n:
        nbr +=1
        coord.pop()
    else:
    """
    for i in range(1, n+1):
        #print(i, raw_busy[i])
        if not raw_busy[i]:
            raw_busy[i] = True
            for j in range(1, n+1):
                if col_busy[j] or (d1_busy[i+j+d1_corr]) or (d2_busy[i-j+d2_corr]):
                    continue
                else:
                    col_busy[j], d1_busy[i+j+d1_corr], d2_busy[i-j+d2_corr] = True, True, True
                    coord.append((i, j))
                    if len(coord) == n:
                        nbr += 1
                        print(nbr, coord)
                    else:
                        order_or_print(coord)
                    coord.pop()
                    col_busy[j], d1_busy[i+j+d1_corr], d2_busy[i-j+d2_corr] = False, False, False
            raw_busy[i] = False

    return

col_busy[1] = True
nbr = 0
for i in range(1, n+1):
    #raw_busy[i] = True
    raw_busy[i], d1_busy[i + 1 + d1_corr], d2_busy[i - 1 + d2_corr] = True, True, True
    #nbr += 1
    order_or_print([(i,1)])
    raw_busy[i], d1_busy[i + 1 + d1_corr], d2_busy[i - 1 + d2_corr] = False, False, False
    #print(i, "nbr", nbr)
print(nbr)



def order_or_print(coord):
    global nbr

    for raw_idx in range(len(coord)+1, n+1):
        print(coord)
        for col_idx in range(1, n+1):
            if col_busy[col_idx] or (d1_busy[raw_idx+col_idx+d1_corr]) or (d2_busy[raw_idx-col_idx+d2_corr]):
                continue
            else:
                col_busy[col_idx], d1_busy[raw_idx+col_idx+d1_corr], d2_busy[raw_idx-col_idx+d2_corr] = True, True, True
                coord.append((raw_idx, col_idx))
                if len(coord) == n:
                    nbr += 1
                    print(nbr, coord)
                else:
                    order_or_print(coord)
                coord.pop()
                col_busy[col_idx], d1_busy[raw_idx+col_idx+d1_corr], d2_busy[raw_idx-col_idx+d2_corr] = False, False, False

    return
