test_f_name = 'input.txt'
f = open(test_f_name, 'r')
sold, bar_health, bar_prod = list(map(int, f.read().strip().split('\n')))
#enemy = 0

def calck_battle(sold, bar_health, bar_prod, enemy=0):
    step_n =0
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
    print(step_n)

calck_battle(sold, bar_health, bar_prod)

'''
import os
for test_f_name in sorted(os.listdir('.')):
    #print(f_name)
    if test_f_name[:5] == 'input':
        f = open(test_f_name, 'r')
        sold, bar_health, bar_prod = list(map(int, f.read().strip().split('\n')))
        calck_battle(sold, bar_health, bar_prod)
'''