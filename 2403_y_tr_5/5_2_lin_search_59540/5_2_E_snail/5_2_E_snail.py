test_f_name = 'input.txt'
f = open(test_f_name, 'r')

#txt_file = f.readlines()
n = int(f.readline())

good_berries, bad_berries = [], []
#max_good_up = max_bad_up = 0
max_good_up = 0
max_h = 0
# max_good_berry =
max_bad_berry = (0, 0, 0)
#max, delta, i


for i in range(1, n+1):
    up, down = list(map(int, f.readline().split()))
    ber_up = up - down
    if ber_up > 0:
        good_berries.append((up, ber_up, i))
        if up > max_good_up:
            max_good_up = up
    else:
        bad_berries.append(i)
        if up > max_bad_berry[0]:
            max_bad_berry = (up, down, i)

max_bad_up, max_bad_id = max_bad_berry[0], max_bad_berry[2]
#if max_bad_up > max_good_up:

good_berries_order = [i[2] for i in good_berries]

#print(max_bad_up, max_bad_berry)
#sorted(good_berries)[::-1]
if good_berries:
    sum_delta = sum([i[1] for i in good_berries])
    #print(sum_delta )
    max_raise, max_id, max_up, max_alt_raise, max_alt_id = 0, 0, 0, 0, 0
    #for gb in sorted(good_berries)[::-1]:
    for gb in sorted(good_berries)[::-1]:
        norm_raise = gb[0]+sum_delta-gb[1]
        if  norm_raise > max_raise:
            max_raise = gb[0]+sum_delta-gb[1]
            max_id = gb[2]
            #print(max_id )
    norm_alt_raise = sum_delta + max_bad_up
    if norm_alt_raise > max_alt_raise:
        max_alt_raise = norm_alt_raise
        max_alt_id = max_bad_id
    if max_raise > max_alt_raise :
        max_h = max_raise
        good_berries_order .remove(max_id )
        res  = good_berries_order  + [max_id] + bad_berries
    else:
        max_h = max_alt_raise
        bad_berries.remove(max_alt_id )
        #bad_berries.remove(max_bad_id)
        res  = good_berries_order  + [max_alt_id] + bad_berries
else:
    max_h = max_bad_up
    bad_berries.remove(max_bad_berry[2])
    res  = [max_bad_berry[2]] + bad_berries
print(max_h)
print(*res)
