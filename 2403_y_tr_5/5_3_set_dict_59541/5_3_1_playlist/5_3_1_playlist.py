#работает для k==1
test_f_name = 'input.txt'
f = open(test_f_name, 'r')

#txt_file = f.readlines()
n = int(f.readline())

def get_common_pl():
    _ = f.readline()
    play_list = set(f.readline().split())

    #if n == 1:
        #return sorted(play_list)
    for i in range(1, n):
        tmp = f.readline()
        pl = f.readline().split()
        #print('pl, tmp', pl, tmp)
        play_list = play_list.intersection(pl)
        #print('play_list', play_list)
    return sorted(play_list)

res = get_common_pl()
print(len(res))
print(*res)