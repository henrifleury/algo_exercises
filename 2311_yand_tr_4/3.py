from math import atan2, pi
#x1, y1, x2, y2 = map(int, input().split())
f = open('input.txt', 'r')
x1, y1, x2, y2 = map(int, f.readline().split())

r1 = (x1*x1 + y1*y1)**.5
r2 = (x2*x2 + y2*y2)**.5


fi_1 = atan2(y1, x1)# if x1 != 0 else pi/2
fi_2 = atan2(y2, x2)# if x2 != 0 else pi/2

if y1*y2 > 0:
    arc = abs(fi_1-fi_2)
else:
    arc = abs(fi_1) + abs(fi_2)
    #print(arc, pi)
    if arc > pi: arc = 2*pi-arc
#print(fi_1, fi_2, arc)
if arc <= 2:
    # дуга + разница радиусов
    res = min(r1, r2)*arc + abs(r1-r2)
else:
    #сумма радиусов
    res =r1 + r2
print(res)

#2481183.366012966726
#2481185.9568153536
#-444444 -333333 888888 666666
#0 5 4 -3
#1000000 -372066 -999998 -1000000
# -820932 -715885 391455 764657
#1948262.194216139615