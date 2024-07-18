#работает для k==1
test_f_name = 'input.txt'
f = open(test_f_name, 'r')

#txt_file = f.readlines()
s1 = f.readline().strip()
s2 = f.readline().strip()

from collections import Counter



res = "YES" if Counter(s1)==Counter(s2) else "NO"
print(res)
