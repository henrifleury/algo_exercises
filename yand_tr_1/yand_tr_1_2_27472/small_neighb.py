#arr = list(map(int, input().split()))

def count_big_neighb_nbr(arr):
    if len(arr)<3:
        return 0
    ind=1 # не с 0 а с 1
    res=0
    while ind<len(arr)-1: #до предпоследнего включительно
        if arr[ind-1] < arr[ind] > arr[ind+1]:
            res+=1
            ind+=2
        else:
            ind += 1
    return res

#print(count_big_neighb_nbr(arr))

assert count_big_neighb_nbr([1, 2, 3, 4, 5])==0
assert count_big_neighb_nbr([5, 4, 3, 2, 1])==0
assert count_big_neighb_nbr([1, 5, 1, 4, 1])==2

arr = list(map(int, "1 5 1 5 1".split()))
print(count_big_neighb_nbr(arr))