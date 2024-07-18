f = open('input.txt', 'r')
a = int(f.readline())
b = int(f.readline())
n = int(f.readline())
#print(a,b,n)
a_max = a
a_min = (a+n-1)//n
b_max = b
b_min = (b+n-1)//n

print(a_min, a_max, b_min, b_max)
print(a_max<b_min)
if a_max<=b_min:
    print("No")
else:
    print("Yes")