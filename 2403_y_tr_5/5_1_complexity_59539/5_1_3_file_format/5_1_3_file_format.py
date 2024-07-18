test_f_name = 'input.txt'
f = open(test_f_name, 'r')

tab_spaces = 4
#score_gamenum_command
#print(f.read().strip().split('\n'))
#arr = list(map(int, f.read().strip().split('\n')))
n = int(f.readline())
#arr = arr[1:]
#print(n)
press_counter = 0
for i in range(n):
    sp_nbr = int(f.readline())
    quotient, remainder = divmod(sp_nbr, tab_spaces)
    press_counter += quotient
    if remainder <= 2:
        press_counter  += remainder
    else:
        press_counter += 2
print(press_counter)
