#len_arr = int(input())
#arr = list(map(int, input().split()))

def get_Vasya_place(arr):
    if len(arr)<3:
        return 0
    maybe_vasyas_res_l = []
    #maybe_vasyas_ind = []
    #maybe_vasya_d = dict()
    best_res = max(arr)
    first_winner_ind = arr.index(best_res)
    for ind in range(first_winner_ind+1, len(arr)-1):
        #print(ind, arr[ind])
        if arr[ind]%10 == 5:
            #if arr[ind-1]==best_res:
            if arr[ind + 1] < arr[ind]:
                #maybe_vasyas_ind.append(ind)
                maybe_vasyas_res_l.append(arr[ind])
                #maybe_vasya_d[arr[ind]]=ind
    if not maybe_vasyas_res_l:
        return 0

    best_vasya_res=max(maybe_vasyas_res_l)
    if best_vasya_res==best_res:
        return 1
    vasya_place=1
    for l in arr:
        if l > best_vasya_res:
            vasya_place+=1
    return vasya_place

#print(get_Vasya_place(arr))

arr = list(map(int, "10 20 15 10 30 5 1".split()))
assert get_Vasya_place(arr)==6

arr = list(map(int, "15 15 10".split()))
assert get_Vasya_place(arr)==1

arr = list(map(int, "10 15 20".split()))
assert get_Vasya_place(arr) == 0
