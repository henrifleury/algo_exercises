'''
a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())
f = int(input())
'''
def get_answer(a11,a12,a21,a22,b1,b2):
    if a11==a12==a21==a22==b1==b2==0:
        return 5
    #if (a11 + a12 + a21 + a22 == 0) and (b1!=0 | b2!=0):
        #return 0
    if (a11==a12==0 & b1!=0) | (a21==a22==0 & b2!=0):
        return 0 #пред проверку
    if (a11==a12==b1==0) | (a21==a22==b2==0):
        if a11==a12==b1==0:
            a01, a02, b0 = a21, a22, b2
        else:
            a01, a02, b0 = a11, a12, b1
        if a02==0:
            return 3, b0/a01
        elif a01==0:
            return 4, b0/a02
        else:
            return 1, b0/a02, -b0/a01

    det = a11 * a22 - a12 * a21
    min1 = a21 * b2 - a22*b1
    min2 = a11 * b2 - a21*b1
    if det == 0:
        if min1 != 0 or min2 != 0:
            return 0
    #else:


a, b, c, d, e, f = 1, 0, 0, 1, 3, 3
print(get_answer(a,b,c,d,e,f))

