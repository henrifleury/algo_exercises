'''inp_lst = []
while True:
    el = int(input())
    if el == -2000000000:
        break
    inp_lst.append(el)
'''

def is_asc(arr):
    if not arr:
        return "NO"
    if len(arr)<1:
        return "NO"
    prev_el=arr[0]-1
    for el in arr:
        if el>prev_el:
            prev_el=el
        else:
            return "NO"
    return "YES"

def is_w_asc(arr):
    if not arr:
        return "NO"
    if len(arr)<1:
        return "NO"
    prev_el=arr[0]-1
    for el in arr:
        if el>=prev_el:
            prev_el=el
        else:
            return "NO"
    return "YES"

def is_desc(arr):
    if not arr:
        return "NO"
    if len(arr)<1:
        return "NO"
    prev_el=arr[0]+1
    for el in arr:
        if el<prev_el:
            prev_el=el
        else:
            return "NO"
    return "YES"

def is_w_desc(arr):
    if not arr:
        return "NO"
    if len(arr)<1:
        return "NO"
    prev_el=arr[0]+1
    for el in arr:
        if el<=prev_el:
            prev_el=el
        else:
            return "NO"
    return "YES"



def seq_type(arr):
    if len(arr)<2:
        return None

    first_el = arr[0]
    last_el = arr[-1]

    if first_el == last_el:
        for el in arr:
            if el != first_el:
                return "RANDOM"
        return "CONSTANT"
    elif first_el < last_el:
        if is_asc(arr)=="YES":
            return "ASCENDING"
        elif is_w_asc(arr)=="YES":
            return "WEAKLY ASCENDING"
    elif first_el > last_el:
        if is_desc(arr) == "YES":
            return "DESCENDING"
        elif is_w_desc(arr) == "YES":
            return "WEAKLY DESCENDING"

    return "RANDOM"


#print(seq_type(inp_lst))
'''
assert seq_type([100,100,100]) == "CONSTANT"
assert seq_type([100,101,100]) == "RANDOM"
assert seq_type([100,101,102]) == "ASCENDING"
assert seq_type([100,101,101]) == "WEAKLY ASCENDING"
'''
assert seq_type([100,99,98]) == "DESCENDING"
assert seq_type([100,99,99]) == "WEAKLY DESCENDING"
