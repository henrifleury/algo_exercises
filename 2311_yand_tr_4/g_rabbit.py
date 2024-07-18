f = open('input.txt', 'r')
n, m = map(int, f.readline().split())
sq = []
for i in range(n):
    sq.append(list(map(int, f.readline().split())))
max_side = min(n,m)
min_side = 0

#print(sq)
#тут я встрял sq_s_len = [[0]*n]*m
sq_s_len = [[0 for j in range(n)] for i in range(m)]
for i, line in enumerate(sq):
    counter=0
    #max_line_side = min(max_side, n-i)
    for j,is_parrot in enumerate(line):
        if is_parrot:
            #if counter<max_line_side:
            if counter<max_side:
                counter+=1
        else:
            counter=0
        sq_s_len[j][i] = counter
#sq_s_len = [[0, 0, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 27, 27, 27, 27, 27, 27, 27, 27, 27, 27, 27, 27, 27, 27, 27, 27, 27, 27, 27, 59, 59, 59, 59, 59, 59, 59, 59, 0, 0, 0, 0, 0]]
#sq_s_len = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 23, 23, 23, 23, 23, 23, 23, 23, 23, 23, 23, 23, 23, 23, 23, 23, 23, 23, 23, 23, 23, 23, 23, 23, 23, 23, 23, 23, 0, 0, 0, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 27, 27, 27, 27, 27, 27, 27, 27, 27, 27, 27, 27, 27, 27, 27, 27, 27, 27, 27, 59, 59, 59, 59, 59, 59, 59, 59, 0, 0, 0, 0, 0]]
#sq_s_len = [[0, 0, 23, 23, 23, 23, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 27, 27, 27, 27, 27, 27, 27, 27, 27, 27, 27, 27, 27, 27, 27, 27, 27, 27, 27, 59, 59, 59, 59, 59, 59, 59, 59, 0, 0, 0, 0, 0]]
#n = len(sq_s_len[0])
#print(n)

for i, line in enumerate(sq_s_len[::-1]):
    for j, side_len in enumerate(line):
        side_len = min(side_len, n-j)
        #min_side=26
        if side_len>min_side:
            #248 1 27 [27, 27, 27, 27, 27, 27, 27, 27, 27, 27, 27, 27, 27, 27, 27, 27, 27, 27, 59, 59, 59, 59, 59, 59, 59, 59]
            prev_side=1
            #for k in range(1, side_len):
            cur_side = min(side_len, line[j])
            k=1
            prev_side=1
            while k<side_len:
            #for k in range(1, side_len)
                cur_side = min(side_len, line[j+k])
                if cur_side<=min_side:
                    break
                if cur_side<side_len:
                    side_len=cur_side

                prev_side = min(k+1, cur_side)
                #print(k, "prev_side", prev_side)
                k += 1
            if prev_side>min_side:
                #print(j, min_side, prev_side)
                min_side=prev_side
    if min_side>=max_side:
        break
print(min(min_side, max_side))