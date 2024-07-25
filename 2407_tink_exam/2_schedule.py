days = 'MON, TUE, WED, THU, FRI, SAT, SUN'
days_d = dict()
counter = 0
for d in days.split(', '):
    days_d[d] = counter
    counter += 1

#f = open('input.txt', 'r')

#_ = int(f.readline())

hired = []
for wn in range(4):
    #hired_w = f.readline().split()
    hired_w = input().split()
    hired += sorted([wn*7 + days_d[d]+1 for d in hired_w])
if hired:
    if len(hired) == 28:
        print('0 0')
    else:
        hired.append(29)
        start_day = best_start_day = 1
        max_days_free = 0
        for hired_day in hired:
            free = hired_day - start_day
            if free > max_days_free:
                best_start_day = start_day
                max_days_free = free
            start_day = hired_day
        print(f'{best_start_day + 1} {best_start_day + max_days_free - 1}')
else:
    print('1 28')
