test_f_name = 'input.txt'
f = open(test_f_name, 'r')
x, bh, prod = list(map(int, f.read().strip().split('\n')))

from math import ceil

def calc_big_prod(x, bh, prod, y):
    # шансы есть, если prod равно или ненамного больше x и здоровья у барака не очень много
    # оценка нестрогая, но кое-что можно отбросить сразу
    if 1.7 * x <= bh + prod:
        return -1
    # тк prod>x первым шагом очевидно нужно добивать барак
    step = 2
    y -= x - bh
    # bh = 0
    while x * y > 0:
        x -= y
        y -= x
        step += 1
    if y > 0:
        return -1
    else:
        return step

def test_end(x, bh, prod, y, ba_points):
    #print(x, 'bh', bh, prod, y, ba_points)
    end_step = 0
    res = -1
    while (x > 0) & (bh + y > 0):
        if x >= bh + y:
            return end_step+1

        #if bh > 0:
        ba = min(bh, ba_points)
        bh -= ba
        y_att_points = x - ba
        y = max((y - y_att_points), 0)
        x -= y

        if bh>0:
            y += prod
        end_step +=1
        #end_step +=1
        #print('end_step', end_step, 'x', x, bh, 'y', y)
    if y == 0:
        res = end_step
    #print('res', res)
    return res

def beat_barr_prior(x, bh, prod, y):

    end_step = 0
    res = -1
    while (x > 0) & (bh + y > 0):
        if x >= bh + y:
            return end_step+1

        #if bh > 0:
        ba = max(bh, 0)
        bh -= ba
        y_att_points = x - ba
        y = max((y - y_att_points), 0)
        x -= y

        if bh>0:
            y += prod
        end_step +=1
        #end_step +=1
        #print('end_step', end_step, 'x', x, bh, 'y', y)
    if y == 0:
        res = end_step
    #print('res', res)
    return res

def calc_battle(x, bh, prod):
    # если барак ничего не произведет
    if bh <= x:
        return 1

    # первый удар по бараку
    step = 1
    bh -= x
    y = prod

    if prod >= x:
        # d
        return calc_big_prod(x, bh, prod, y)

    # далее пока не выполнится условие нужно уничтожать всех врагов и барак на оставшиеся очки
    #if 1.7 * x <= bh + prod:
    barr_attack_points = x-prod
    best_step = step +(bh+barr_attack_points)//barr_attack_points
    #print('best_step', best_step)

    bh_goal = ceil(1.7 * x) - prod + 1
    #
    if (bh - bh_goal) > barr_attack_points:
        step += (bh-bh_goal) // barr_attack_points
        bh -= (step-1) * barr_attack_points
        y = prod#+barr_attack_points
        #y = 0
    if bh >= bh_goal:
        bh -= barr_attack_points
        y = prod#+barr_attack_points
        step += 1
    while (x > 0) & ((y + bh) > 0):
        #print('step', step)
        # когда выполнено условие можно пробовать поменьше громить барак
        #for test_ba_p in range(0, barr_attack_points+1)[::-1]:
        #print('barr_attack_points, bh + 1', barr_attack_points, bh + 1)
        #for test_ba_p in range(barr_attack_points, bh + 1):
        #for test_ba_p in [bh]:
        for test_ba_p in [bh]:
            test_step = test_end(x, bh, prod, y, test_ba_p)
            #print(best_step > step+test_step, best_step, step+test_step,  'test_ba_p', test_ba_p, 'test_step', test_step)
            if test_step == -1:
                break
            elif best_step > step+test_step:
                best_step = step+test_step
        ba = min(bh, barr_attack_points)
        bh -= ba
        #y = max((x - ba), 0)
        y_att_points = x - ba
        y = max((y - y_att_points), 0)
        x -= y
        if bh > 0:
            y += prod
        #print(step, 'x,y, bh', x, y, bh)
        step += 1
    best_step = min(best_step, step)
    return best_step
#print("*****")
print(calc_battle(x, bh, prod))


"""
import os
for test_f_name in sorted(os.listdir('.')):
#for test_f_name in ['input2.txt']:
    #print(f_name)
    if test_f_name[:5] == 'input':
        f = open(test_f_name, 'r')
        x, bh, prod = list(map(int, f.read().strip().split('\n')))
        print(test_f_name, calc_battle(x, bh, prod))
"""
assert calc_battle(300, 301, 485) == -1
assert calc_battle(300, 301, 484) == 6
assert calc_battle(250, 500, 230) == 8
assert calc_battle(5, 8, 5) == 4
assert calc_battle(25, 200, 10) == 13
assert calc_battle(250, 500, 187) == 4
assert calc_battle(250, 500, 218) == 6
assert calc_battle(2, 3, 2) == 3
assert calc_battle(250, 500, 249) == 101
assert calc_battle(2500, 5000, 2499) == 961
assert calc_battle(78, 4934, 77) == 4812
assert calc_battle(78, 126, 77) == 5
assert calc_battle(1661, 4327, 1107) == 6
assert calc_battle(1092, 2892, 950) == 11
assert calc_battle(31, 495, 15) == 30
assert calc_battle(250, 500, 209) == 6
assert calc_battle(3000, 5000, 2998) == 79
assert calc_battle(2500, 5000, 2420) == 16
"""
run_test 250 500 209 6
run_test 3000 5000 2998 79
run_test 2500 5000 2420 16"""