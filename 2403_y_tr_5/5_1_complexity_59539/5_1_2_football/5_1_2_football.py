test_f_name = 'input.txt'
f = open(test_f_name, 'r')

#score_gamenum_command
score_1_1, score_1_2 = list(map(int, f.readline().split(':')))
score_2_1, score_2_2 = list(map(int, f.readline().split(':')))
is_first_at_home = int(f.readline())==1
score_cur_1 = score_1_1 + score_2_1
score_cur_2 = score_1_2 + score_2_2
(score_guest_1, score_guest_2) = (score_2_1, score_1_2) if is_first_at_home else (score_1_1, score_2_2)
if score_cur_1 > score_cur_2:
    print(0)
else:
    goal_need = score_cur_2-score_cur_1
    score_guest_cur = score_guest_1+goal_need if is_first_at_home else score_guest_1
    if score_guest_cur <= score_guest_2:
        goal_need += 1
    print(goal_need)