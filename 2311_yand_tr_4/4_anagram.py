f = open('input.txt', 'r')
s1 = f.readline()
s2 = f.readline()

def check_an(s1,s2):
    s_dict = {}
    for i in s1:
        if i in s_dict:
            s_dict[i] = s_dict[i]+1
        else:
            s_dict[i] = 1

    for i in s2:
        if i in s_dict:
            if s_dict[i] < 1:
                return "NO"
            else:
                s_dict[i] = s_dict[i] - 1
        else:
            return "NO"

    if sum(s_dict.values())==0:
        return "YES"
    else:
        return "NO"

print(check_an(s1,s2))