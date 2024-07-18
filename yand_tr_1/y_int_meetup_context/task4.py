inp_list = []
with open("input.txt", "r") as f:
    for line in f.readlines():
        inp_list.append(line.strip())


#n = int(input())
n = int(inp_list[0])


hash_d = set()
max_len_s = 100
for idx in range(1, n+1):
    s = inp_list[idx].strip()
    #s = input().strip()
    #if s:
    if s:
        s = s[:min(len(s), max_len_s)]
        hash_d.add(hash(s))
print(len(hash_d))