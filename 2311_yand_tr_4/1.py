""" Задана последовательность целых чисел a1, a2, …, an. Задаются запросы: сказать любой элемент последовательности
на отрезке от L до R включительно, не равный минимуму на этом отрезке.
"""
f = open('input.txt', 'r')
n, m = map(int, f.readline().split())
arr_a = list(map(int, f.readline().split()))
for n_str in range(m):
    l, r = map(int, f.readline().split())
    if l < r:
        for i in range(l+1, r+1):
            if arr_a[i] != arr_a[l]:
                print(max(arr_a[i], arr_a[l]))
                break
        if arr_a[i] == arr_a[l]:
            print("NOT FOUND")
    else:
        print("NOT FOUND")



