from math import atan2, pi
f = open('input.txt', 'r')
#x1, y1, x2, y2 = map(int, f.readline().split())
k = int(f.readline())
n = int(f.readline())
#empl_l = list(map(int, f.readline().split()))

time=0
empl_d = dict()
not_empty_floors = []
for i in range(n):#enumerate(empl_l):
    a = int(f.readline())
    fl_race_nbr = a // k
    time += 2*fl_race_nbr*(i+1)
    #empl_l.append(a % k)
    rest = a % k
    if rest > 0:
        empl_d[i+1] = rest
        not_empty_floors.append(i + 1)
if empl_d:
    lift = k
    #for fl_nbr in list(empl_d.keys())[::-1]:
    #not_empty_floors = list(empl_d.keys())
    last_id = len(not_empty_floors)-1
    while last_id>=0:
        fl_nbr = not_empty_floors[last_id]
        #print(time, fl_nbr, not_empty_floors)
        if lift == 0:
            lift = k
        pass_nbr = empl_d[fl_nbr]
        if lift == k:
            time += 2*fl_nbr
            lift -= pass_nbr
            #del empl_d[fl_nbr]
            #not_empty_floors = not_empty_floors[:-1]
            last_id-=1
        else:
            if pass_nbr <= lift:
                lift -= pass_nbr
                #not_empty_floors = not_empty_floors[:-1]
                last_id -= 1
            else:
                empl_d[fl_nbr] -= lift
                lift = 0
print(time)
        #print(k)
#while empl_d:
    #lift = k



    #for k in empl_d

"""    #rest = empl_d.get(a % k, [])
    #rest
    if rest in empl_d:
        empl_d[rest] = empl_d[rest]+[i+1]
    else:
        empl_d[rest] = [i+1]

    if 0 in empl_d: del empl_d[0]

    print(sorted(empl_d.keys()))
    #while empl_d:
        # нужно объезжать все этажи минусовать людей, плюсовать время
"""

