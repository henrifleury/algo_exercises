

f = open('input.txt', 'r')
res_list = list(map(int,f.readline().split(',')))

print(sum(res_list))
print(len(res_list))
print(sum(res_list)/len(res_list))