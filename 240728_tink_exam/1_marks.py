'''Олег — настоящий герой, чьи школьные будни наполнены заботами, уроками и оценками. Он изо всех сил старается, но, как и любой человек, он время от времени допускает ошибки и получает не самые лучшие оценки.

Сегодня Олег стоит перед особенным испытанием — ему предстоит показать своим родителям свои оценки. Родители попросили показать ему все его оценки за какие-то последовательные ﻿77﻿ дней. Оценки представляют собой последовательность целых чисел от ﻿22﻿ до ﻿55﻿ включительно — по одной оценке на каждый день. Олег хочет выбрать такой непрерывный отрезок своих оценок, чтобы в этом отрезке не было оценок ﻿22﻿ и ﻿33﻿, а количество оценок ﻿55﻿ было максимальным.

Помогите Олегу найти этот особенный момент, когда его школьный свет преобладает над тьмой, и его оценки сияют наиболее ярко!

Формат входных данных

Первая строка содержит одно натуральное число ﻿nn﻿ — количество оценок ﻿(1≤n≤105)(1≤n≤105)﻿. Вторая строка содержит ﻿nn﻿ целых чисел — по оценке ﻿mm﻿ за каждый день ﻿(2≤m≤5)(2≤m≤5)﻿.

Формат выходных данных

Выведите количество пятерок в выбранном Олегом отрезке, удовлетворяющем всем условиям. Если такого отрезка не существует, выведите ﻿−1−1﻿.'''


def main(marks):
    week_len = 7
    mark_nbr = len(marks)

    two_three_nbr = 0
    five_nbr = 0

    for i in range(min(week_len, mark_nbr)):
        if marks[i] <= 3:
            two_three_nbr += 1
        #if not two_three_nbr:
        if marks[i] == 5:
            five_nbr += 1

    best_week = five_nbr if not two_three_nbr else 0
    for i in range(week_len, mark_nbr):
        left = i-week_len
        mark_out = marks[left]

        if mark_out == 5:
            five_nbr -= 1
        if mark_out <= 3:
            two_three_nbr -= 1

        if marks[i] <= 3:
            two_three_nbr += 1
        if marks[i] == 5:
            five_nbr += 1

        if not two_three_nbr:
            if five_nbr > best_week:
                best_week = five_nbr
                print(best_week)

    return best_week if best_week else -1


'''
if __name__ == '__main__':
    n = int(input())
    marks = list(map(int, input().strip().split()))
    print(main(marks))
'''

marks = list(map(int, '5 5 4 5 4 5 4 5 4'.strip().split()))
assert main(marks) == 4
marks = list(map(int, '3 4 4 4 4 5 4 5'.strip().split()))
assert main(marks) == 2

marks = list(map(int, '5 5 5 5 5 3 5 5 5 5'.strip().split()))
assert main(marks) == -1
