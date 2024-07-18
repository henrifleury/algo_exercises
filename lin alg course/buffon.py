#from math import pi
f = open('input.txt', 'r')
#n = int(f.readline())
res_list = list(map(int,f.readline().split(',')))
zeros_list = [zero for zero in res_list if zero==0]
ones_list = [zero for zero in res_list if zero==1]

#res_list = f.readline().split(',')
n_ones = len(ones_list)
p = n_ones/len(res_list)
assert (len(zeros_list)+len(ones_list)==len(res_list))
print(p,  len(res_list), res_list[:10])

a = 2.2/2
l = 1.6/2

print(a, l)
print(2*l/p/a)
