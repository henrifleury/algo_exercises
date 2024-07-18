reset_dict = dict()
disable_dict = dict()
ra_dict = dict()

f = open('input.txt', 'r')
n, m, q = list(map(int, f.readline().strip().split()))


for idx in range(1, n+1):
    reset_dict[idx] = 0
    disable_dict[idx] = set()

for i in range(q):
    command = f.readline().strip().split()

    if command[0] == 'DISABLE':
        dc_num, serv_num = int(command[1]), int(command[2])
        disable_dict[dc_num].add(serv_num)

        r = reset_dict.get(dc_num, 0)
        a = m - len(disable_dict[dc_num])

        ra_dict[dc_num] = r*a
        #print(command, r, a, ra_dict)

    elif command[0] == 'RESET':
        dc_num = int(command[1])
        reset_dict[dc_num] += 1
        disable_dict[dc_num] = set()
        ra_dict[dc_num] = reset_dict[dc_num]*m
        #print(command, r, a, ra_dict)

    elif command[0] == 'GETMAX':
        #print('GETMAX', ra_dict.values())
        if ra_dict:
            max_ra = max(ra_dict.values())
            print(list(ra_dict.values()).index(max_ra)+1)
        else:
            print(1)

    elif command[0] == 'GETMIN':
        if ra_dict:
            min_ra = min(ra_dict.values())
            print(list(ra_dict.values()).index(min_ra)+1)
        else:
            print(1)
