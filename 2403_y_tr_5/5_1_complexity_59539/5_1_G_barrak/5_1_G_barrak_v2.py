test_f_name = 'input.txt'
f = open(test_f_name, 'r')
sold, bar_health, bar_prod = list(map(int, f.read().strip().split('\n')))
#enemy = 0

def end_battle(sold, bar_health, bar_prod, enemy):
    if bar_prod+bar_health-sold == 2*sold:
        # типа ничья но условия разрушения и уничтожения выполнены
        return 1
    step_n = 0
    while sold > 0:
        #print(sold, bar_health, bar_prod, enemy)
        step_n += 1
        attack_p = sold

        if attack_p >= bar_health:
            att_barr_p = min(bar_health, attack_p)
            att_enemy_p = attack_p - att_barr_p
        else:
            att_enemy_p = min(enemy, attack_p)
            att_barr_p = attack_p - att_enemy_p

        enemy -= att_enemy_p
        bar_health -= att_barr_p
        sold -= enemy
        if bar_health > 0:
            enemy += bar_prod
        else:
            if enemy <= 0:
                break
        if sold <= 0:
            step_n = -1
            break
    return step_n

def calck_battle(sold, bar_health, bar_prod, enemy=0):
    if sold >= bar_health:
        return 1
    #if bar_prod+bar_health-sold <= 2*sold:
        #return end_battle(sold, bar_health, bar_prod, enemy=bar_prod)
    if bar_prod >= sold:
        if bar_prod + bar_health - sold <= 2 * sold:
            bar_health -= sold
            res = end_battle(sold, bar_health, bar_prod, enemy=bar_prod)
            if res>0:
                return res+1
            return -1
        else:
            return -1
    res = 1
    bar_health -= sold
    delta = sold - bar_prod
    res += bar_health//delta
    #print('res', res, delta)
    bar_health -= delta*(res-1)
    if bar_health + enemy ==0:
        return res
    #print(sold, bar_health, bar_prod)
    res += end_battle(sold, bar_health, bar_prod, enemy)
    return res

print(calck_battle(sold, bar_health, bar_prod))


import os
for test_f_name in sorted(os.listdir('.')):
#for test_f_name in ['input2.txt']:
    #print(f_name)
    if test_f_name[:5] == 'input':
        f = open(test_f_name, 'r')
        sold, bar_health, bar_prod = list(map(int, f.read().strip().split('\n')))
        print(test_f_name, calck_battle(sold, bar_health, bar_prod))
