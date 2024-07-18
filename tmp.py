#tmp_lst = [1,2]
#print(len(tmp_lst), len(tmp_lst[1:]), len(tmp_lst[3:]))

# несколько строк, одно целое в строке
word_l = []
f = open('input.txt', 'r')
n, m = map(int, f.readline().split())
a=[]
for n_str in range(n):
    a.append(list(map(int, f.readline().split())))
print(a)
