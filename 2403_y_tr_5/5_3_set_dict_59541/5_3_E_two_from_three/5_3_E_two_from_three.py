test_f_name = 'input.txt'
f = open(test_f_name, 'r')

#txt_file = f.readlines()
#n = int(f.readline())
n = int(f.readline())
set_1 = set(map(int, f.readline().split()))
_ = int(f.readline())
set_2 = set(map(int, f.readline().split()))
_ = int(f.readline())
set_3 = set(map(int, f.readline().split()))

m1 = set_1 & set_2
m2 = set_2 & set_3
m3 = set_3 & set_1

res = sorted(m1 | m2 | m3)
print(*res)


