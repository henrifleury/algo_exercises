inp_list = []
with open("data1.txt", "r") as f:
    for line in f.readlines():
        inp_list.append(line.strip())

#print(inp_list)