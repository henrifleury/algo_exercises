'''input_s = input()#.split("\n")
n, s = list(map(int, input_s.split()))
min_max_arr=[]
for i in range(n):
    tmp_s=input()
    min_max_arr.append(list(map(int, tmp_s.split())))
'''

verbose = True

def my_print(*args):
    if verbose:
        print(*args)


def get_best_median(s, min_max_arr):
    all_marks = []
    for possible_marks in min_max_arr:
        for mark in range(possible_marks[0], possible_marks[1]+1):
            all_marks.append(mark)
    all_marks_s = set(all_marks)
    marks_freq_d = dict()
    for mark in all_marks_s:
        marks_freq_d[mark] = sum([1 for i in all_marks if i==mark])
    my_print(all_marks)
    my_print(marks_freq_d)

    possible_median


n,s = 3,27
min_max_arr = [[11, 14], [2, 10], [11, 14]]
get_best_median(s, min_max_arr)