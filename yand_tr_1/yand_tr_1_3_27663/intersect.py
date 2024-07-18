#arr1 = list(map(int, input().split()))
#arr2 = list(map(int, input().split()))

arr1 = list(map(int, "1 3 2".split()))
arr2 = list(map(int, "4 3 2".split()))
print(sorted(set(arr1) & set(arr2)))