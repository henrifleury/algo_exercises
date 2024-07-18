reset_dict = dict()
disable_dict = dict()
ra_dict = dict()

#with open("input.txt", "r") as f:
f = open('input.txt', 'r')
n, m, q = list(map(int, f.readline().strip().split()))
#for idx in range(1, n+1):
    #reset_dict[idx] = 0
    #disable_dict[idx] = set()


max_ra, max_ra_dc = 0, 1
#min_ra, min_ra_dc = 0, 1
for i in range(q):
    command = f.readline().strip().split()
    print(command)
    if command[0] == 'DISABLE':
        dc_num, serv_num = int(command[1]), int(command[2])
        if dc_num not in disable_dict:
            disable_dict[dc_num] = set()
        disable_dict[dc_num].add(serv_num)
        #disable_len_dict[dc_num] = len(disable_dict[dc_num])
        ra = reset_dict.get(dc_num, 0) * len(disable_dict[dc_num])
        print(ra > max_ra, 'DISABLE', dc_num, ra, max_ra)
        if ra > max_ra:
            max_ra = ra
            max_ra_dc = dc_num

    elif command[0] == 'RESET':
        dc_num = int(command[1])
        if dc_num not in reset_dict:
            reset_dict[dc_num] = 0
        reset_dict[dc_num] += 1
        if dc_num in disable_dict:
            del disable_dict[dc_num]
            #del disable_len_dict[dc_num]
        #if min_ra != 0:
            #min_ra_dc = dc_num
        ra = reset_dict[dc_num] * m
        print(ra > max_ra, 'RESET', dc_num, max_ra)
        if ra > max_ra:
            max_ra = ra
            max_ra_dc = dc_num
        print(ra > max_ra, 'RESET', dc_num, max_ra)
        
    elif command[0] == 'GETMAX':
        print(max_ra_dc)
        '''        worst_dc_num = 1
        #if len(reset_dict) > 0:
        #worst_dc_num = list(reset_dict.keys())[0]
        #ra_max = reset_dict[worst_dc_num] * (m - len(disable_dict[worst_dc_num]))
        ra_max = reset_dict.get(worst_dc_num, 0) * (m - len(disable_dict.get(worst_dc_num, set())))
        for dc_num in range(2, n + 1):
            r = reset_dict.get(dc_num, 0)
            a = m
            if dc_num in disable_dict:
                a -= len(disable_dict[dc_num])
                #a -= disable_len_dict[dc_num]
            if r*a > ra_max:
                ra_max = r*a
                worst_dc_num = dc_num
        print(worst_dc_num)
        '''

    elif command[0] == 'GETMIN':
        best_dc_num = 1
        #if len(reset_dict) > 0:
        #best_dc_num = list(reset_dict.keys())[0]
        ra_min = reset_dict.get(best_dc_num, 0) * (m - len(disable_dict.get(best_dc_num, set())))

        for dc_num in range(2, n + 1):
            r = reset_dict.get(dc_num, 0)
            a = m
            if dc_num in disable_dict:
                a -= len(disable_dict[dc_num])
                #a -= disable_len_dict[dc_num]
            ra = r*a
            if ra < ra_min:
                ra_min = ra
                best_dc_num = dc_num
        print(best_dc_num)
