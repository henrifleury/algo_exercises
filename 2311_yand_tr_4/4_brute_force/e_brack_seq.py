#f = open('input.txt', 'r')
f = open('brackets2.in', 'r')
n = int(f.readline())


br_arr = "(["
cl_br_d = {"(": ")", "[": "]", ")":"", "]":""}

def brack_permutate(br_seq="", br_closed=""):
    #print(n, br_seq, br_closed)
    if len(br_seq) == n:
        print(br_seq)
    else:
        #print(n - len(br_seq), len(br_closed))
        if n - len(br_seq) > len(br_closed):
            for bracket in br_arr:
                brack_permutate(br_seq + bracket, br_closed+cl_br_d[bracket])
        if len(br_closed) != 0:
            brack_permutate(br_seq + br_closed[-1], br_closed[:-1])

if n%2:
    print("")
else:
    brack_permutate()



"""        
        if n-len(br_seq) == len(br_closed):
            cur_br_seq = br_closed[-1]
            brack_permutate
            if_close_first = True
        #el
            #cur_br_seq = br_seq
            #if_close_first = False
        else:
            if len(br_closed) == 0:
                cur_br_seq = br_seq
            else:
                cur_br_seq = br_closed[-1] + br_seq
                if_close_first = True
        for bracket in cur_br_seq:
            #br_closed += cl_br_d[bracket]
            brack_permutate(br_seq+bracket, br_closed)
            br_closed = 
"""

