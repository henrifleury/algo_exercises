test_f_name = 'input.txt'
f = open(test_f_name, 'r')

from datetime import *

n = int(f.readline())
year = f.readline().strip()
hol_dow = []
for i in range(n):
    #hol = datetime.date(f.readline().strip().split()+[year])
    hol = f.readline().strip() + ' ' + year
    hol = datetime.strptime(hol, '%d %B %Y').date().strftime('%A')
    #print(hol)
    hol_dow.append(hol)

new_year_dow = f.readline().strip()

from collections import Counter
def is_leap_year(year):
    return (year % 4 == 0 and year % 100 != 0) or year % 400 == 0

def count_days_oneliner(year):
    #return Counter((date(year, 1, 1) + timedelta(days=i)).weekday() for i in range(365 + is_leap_year(year)))
    return Counter((date(year, 1, 1) + timedelta(days=i)).strftime('%A') for i in range(365 + is_leap_year(year)))



#print(n, year, hol_dow, new_year_dow)
dow_counter = count_days_oneliner(int(year))
#print(dow_counter)
for k in hol_dow:
    dow_counter[k] -= 1

dow_counter_rev = {v: k for k, v in dow_counter.items()}
#print(dow_counter_rev, sorted(dow_counter_rev)[0], sorted(dow_counter_rev)[-1])

best_for_work = dow_counter_rev[sorted(dow_counter_rev)[0]]
best_for_hol = dow_counter_rev[sorted(dow_counter_rev)[-1]]

print(best_for_hol)
print(best_for_work)


