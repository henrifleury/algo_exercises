a1, b1, a2, b2 = map(int, input().split())
def get_table_size(a1, b1, a2, b2):
    def get_width(a, b):
        if a > b:
            return a, b
        else:
            return b, a

    w1, h1 = get_width(a1, b1)
    w2, h2 = get_width(a2, b2)

    if w1>w2:
        wb, hb, ws, hs = w1, h1, w2, h2
    else:
        wb, hb, ws, hs = w2, h2, w1, h1

    table_sizes_d = dict()
    for (w,h) in [(wb, hb+hs), (wb, hb+ws), (wb+hs, max(hb,ws)), (wb+ws, max(hb, hs))]:
        table_sizes_d[w*h]=(w,h)
    #print(table_sizes_d)
    return table_sizes_d[min(table_sizes_d.keys())]


print(*get_table_size(a1, b1, a2, b2))

#assert get_table_size(10, 2, 2, 10) in [(20,2), (2,20), (10,4), (4,10)]
#assert get_table_size(5, 7, 3, 2) in [(9, 5), (5, 9)]
#assert get_table_size(10, 2, 2, 10) in [(10, 4), (4, 9)]