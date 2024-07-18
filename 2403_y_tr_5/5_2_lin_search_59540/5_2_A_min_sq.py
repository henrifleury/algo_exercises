test_f_name = 'input.txt'
f = open(test_f_name, 'r')

#txt_file = f.readlines()
k = int(f.readline())
inp_arr_x, inp_arr_y = [], []

for i in range(k):
    dot = list(map(int, f.readline().split()))
    inp_arr_x.append(dot[0])
    inp_arr_y.append(dot[1])

print(min(inp_arr_x), min(inp_arr_y), max(inp_arr_x), max(inp_arr_y))
