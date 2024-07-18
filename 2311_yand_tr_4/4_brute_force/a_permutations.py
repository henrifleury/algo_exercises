f = open('input.txt', 'r')
n = int(f.readline())

f_busy = [True]+[False for i in range(n)]
#print(f_busy)

def order_or_print(pref):
    #print(len(pref), pref)
    if len(pref)==n:
        #end = f_busy.index(True)
        print("".join(map(str, pref)))
    else:
        for i in range(1, n+1):
            if not f_busy[i]:
                f_busy[i] = True
                order_or_print(pref+[i])
                f_busy[i] = False
    return

order_or_print([])