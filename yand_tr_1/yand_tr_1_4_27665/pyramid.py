#n_blocks = int(input())

n_blocks = 3
w_h_list = [[3,1], [2,2], [3,3]]

block_w_dict = dict()
for idx in range(n_blocks):
    #w, h = map(int, input().split())
    w, h = w_h_list[idx]
    #block_list.append((w, h, idx))
    cur_w_block_l = block_w_dict.get(w, list())
    #print(idx, w, h, block_w_dict, cur_w_block_l)
    cur_w_block_l.append(h)
    block_w_dict[w] = cur_w_block_l

max_h=0
for k in sorted(block_w_dict.keys()):
    max_h+=max(block_w_dict[k])
print(max_h)