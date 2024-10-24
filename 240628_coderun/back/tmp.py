(1,2,3)+[4,5]


'''
1 задание

Подсловом некоторого слова ﻿WW﻿ называется слово, получаемое из ﻿WW﻿ выкидыванием одной или нескольких букв. Например, ﻿TTATTTAT﻿ — подслово слова ﻿TTAATTTTAATT﻿, т.к. получается из него выкидыванием четвёртой и шестой букв.

Какой наибольшей длины может быть слово из букв ﻿TT﻿ и ﻿AA﻿, если все его ﻿146146﻿-буквенные подслова различны? В ответ впишите число.

2 задание

Каждый рабочий день Аня выходит работать на крышу на 13-м этаже. Она выходит в случайное время между 9:00 и 17:00 и проводит там ровно 3 часа. Её друг Лёша приходит поработать на крышу в случайное время между 14:00 и 20:00 и проводит там ровно 1 час.

Чему равна вероятность, что за один рабочий день Лёша и Аня встретятся на крыше? Ответ дайте в виде несократимой дроби формата ﻿p/qp/q﻿.

Замечание. Время, когда Аня и Лёша уходят с крыши не обязано быть в этих временных рамках, т.е. Лёша может прийти в 19:15 и уйти в 20:15.

3 задание

Лёша и Аня продолжают каждый день работать на крыше 13-го этажа. Напоминаем, что Аня выходит в случайное время между 9:00 и 17:00 и проводит там ровно 3 часа. Лёша приходит поработать на крышу в случайное время между 14:00 и 20:00 и проводит там ровно 1 час.

Чему равна вероятность, что за рабочую неделю (с понедельника по пятницу) Лёша и Аня хотя бы два раза встретятся на крыше? Ответ дайте в виде несократимой дроби формата ﻿p/qp/q﻿.

Замечание. Время, когда Аня и Лёша уходят с крыши не обязано быть в этих временных рамках, т.е. Лёша может прийти в 19:15 и уйти в 20:15.

4 задание

Новый Офис расположен на кольцевой дороге радиуса 5 км. Саша живёт на той же кольцевой дороге в точке, диаметрально противоположной Офису. Саша ездит на работу на машине по кольцевой дороге. Известно, что он едет так, что расстояние (по прямой) между ним и Офисом сокращается со скоростью 1 км в минуту.

Чему равна скорость ﻿VV﻿ изменения угла между Офисом и Сашей в тот момент, когда угол между ними равен ﻿π/2π/2﻿ ? Найдите скорость в радианах в минуту и укажите в ответе целую часть от ﻿1000V1000V﻿.

Замечание. Для наглядности добавляем картинку движения Саши до Офиса.
'''

# Python3 Code Addition

# limit for array size
N = 50;

# Max size of tree
tree = [0] * (2 * N);


# function to build the tree
def build(arr):
    # insert leaf nodes in tree
    for i in range(n):
        tree[n + i] = arr[i];

        # build the tree by calculating parents
    for i in range(n - 1, 0, -1):
        tree[i] = tree[i << 1] + tree[i << 1 | 1];
    print(tree)
    # function to update a tree node


def updateTreeNode(p, value):
    # set value at position p
    tree[p + n] = value;
    p = p + n;

    # move upward and update parents
    i = p;

    while i > 1:
        tree[i >> 1] = tree[i] + tree[i ^ 1];
        i >>= 1;

    # function to get sum on interval [l, r)


def query(l, r):
    res = 0;

    # loop to find the sum in the range
    l += n;
    r += n;

    while l < r:

        if (l & 1):
            res += tree[l];
            l += 1

        if (r & 1):
            r -= 1;
            res += tree[r];

        l >>= 1;
        r >>= 1

    return res;


# Driver Code
if __name__ == "__main__":
    a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12];

    # n is global
    n = len(a);

    # build tree
    build(a);

    # print the sum in range(1,2) index-based
    print(query(1, 3));

    # modify element at 2nd index
    updateTreeNode(2, 1);

    # print the sum in range(1,2) index-based
    print(query(1, 3));

# This code is contributed by AnkitRai01
'''
s = ' Inc.'
for ch in s:
    print(ord(ch))



import sys
#sys.set_int_max_str_digits(10**10000)
a = 10**100
a = a//2
s = '9'*a+'7' + '9'*a +'5'
#print(s)

with open('../input.txt', 'w') as f:
    f.write(s)


def get_cum_sum_l(x_l: list, half_len):
    cum_sums = [0]
    for i in x_l:
        cum_sums.append(cum_sums[-1] + i)

    cum_sums = cum_sums[1:]
    #return cum_sums+[cum_sums[-1]]*(half_len-len(cum_sums))
    return [0]*(half_len-len(cum_sums)) + cum_sums

if __name__ == '__main__':
    f = open(INPUT_F, 'r')
    x_str: str = f.readline().strip()
    #res = main(x_str)

    start_time = time.time()  # время начала выполнения

    half_len = len(x_str) // 2

    #print(x_str[:half_len] > x_str[half_len:])
    x_l = [int(s) for s in x_str]
    _ = get_cum_sum_l(x_l, half_len)
    end_time = time.time()  # время окончания выполнения
    #print(res)


execution_time = end_time - start_time  # вычисляем время выполнения
print(f"Время выполнения программы: {execution_time} секунд")
'''