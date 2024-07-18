#arr = list(map(int, input().split()))

def is_rising(arr):
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

#print(is_rising(arr))

assert is_rising([1,7,9]) == "YES"
assert is_rising([1,7,5]) == "NO"