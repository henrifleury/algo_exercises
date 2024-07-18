f = open('input.txt', 'r')
s = f.readline()[:-1]

def check_str(s):
    #if not s:
        #return
    opened = []
    #close_s=[]
    close_d = {")": "(", "]": "[" , "}": "{"}
    #print(open_d)

    for sym in s:
        if sym in close_d:
            #print(sym)
            if opened and close_d[sym] == opened[-1]:
                opened.pop()
            else:
                return "no"
        else:
            opened.append(sym)
    if opened:
        return "no"
    else:
        return "yes"
    #print("opened", opened)

print(check_str(s))
