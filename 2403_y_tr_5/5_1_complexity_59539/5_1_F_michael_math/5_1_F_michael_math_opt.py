test_f_name = 'input.txt'
f = open(test_f_name, 'r')
n = int(f.readline())
arr = list(map(int, f.readline().split()))
#res, arr = arr[0], arr[1:]

plus = '+'
mul = 'x'

def parse_arr():
    first_odd_idx = 0
    while arr[first_odd_idx] % 2==0:
        first_odd_idx += 1
    sum_first = sum(arr[:first_odd_idx])
    sum_last = sum(arr[first_odd_idx+1:])
    #print(sum_before, sum_after)
    #res_str = '+'*first_odd_idx
    odd_counter = sum_first % 2 + sum_last % 2
    print(n, 'first_odd_idx', first_odd_idx, 'odd_counter', odd_counter)

    res_str = ''

    if first_odd_idx == 0:
        if sum_last % 2 == 0:
            res_str += '+'
        else:
            res_str += 'x'
        if n>2:
            res_str += '+'*(n-2)
    else:
        #if first_odd_idx == 1:
            #res_str += ''
        #else:
        res_str += '+'*(first_odd_idx-1)
        if odd_counter == 1:
            res_str += 'x'
        else:
            res_str += '+'
        if first_odd_idx < n-1:
            res_str += '+' * (n-1-first_odd_idx)
    return res_str

res = parse_arr()
[print(ord(i)) for i in res]
print(parse_arr())