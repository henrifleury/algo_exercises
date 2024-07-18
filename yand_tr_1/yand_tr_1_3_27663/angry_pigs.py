len_arr = int(input())
inp_lst=[]
for i in range(len_arr):
    inp_lst.append(map(int, input().split()))

def get_shot_nbr(arr):
    shot_nbr = set()
    for x,_ in arr:
        shot_nbr.add(x)
    return len(shot_nbr)


print(get_shot_nbr(inp_lst))