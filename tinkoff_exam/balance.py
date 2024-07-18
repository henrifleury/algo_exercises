#len_arr = int(input())
#arr = list(map(int, input().split()))


verbose = True

def my_print(*args):
    if verbose:
        print(*args)

def n_norm(arr):
    n=len(arr)
    #my_print(n, arr)
    good_per=[]
    for st in range(n-1):
        for end in range(st+2, n+1):
            #my_print(st, end, sum(arr[st:end]))
            if sum(arr[st:end]) == 0:
                my_print("st, end, sum(arr[st:end]), n", st, end, sum(arr[st:end]), n)
                good_per.append((n - end+1))
                break

    my_print(good_per)
    return sum(good_per)

print(n_norm(arr))
#arr = list(map(int, "1 2 3 -6".split()))
arr = list(map(int, "3 3 -6 1".split()))
n_norm(arr)
arr = list(map(int, "42 -42 42".split()))
print(n_norm(arr))
arr = list(map(int, "-1 1 2 -3 6".split()))
print(n_norm(arr))
arr = list(map(int, "1 2 3 -6".split()))
print(n_norm(arr))