'''успел записать только адрес дома и номер квартиры K1, а затем связь прервалась.
 Однако он вспомнил, что по этому же адресу дома некоторое время назад скорая помощь выезжала
 в квартиру K2, которая расположена в подъезда P2 на этаже N2.
  Известно, что в доме M этажей и количество квартир на каждой лестничной площадке одинаково.
  Напишите программу, которая вычилсяет номер подъезда P1 и номер этажа N1 квартиры K1. '''
# Во входном файле записаны пять положительных целых чисел K1, M, K2, P2, N2. Все числа не превосходят 106.
'''Выведите два числа P1 и N1. 
Если входные данные не позволяют однозначно определить P1 или N1, вместо соответствующего числа напечатайте 0.
 Если входные данные противоречивы, напечатайте два числа –1 (минус один). '''
# nt(get_flat_params(20, 4, 4, 1, 1))
# rt get_flat_params(89, 20, 41, 1, 11)==(2,3)

def print_flat_params():
    import math

    k1, m, k2, p2, n2 = list(map(int, input().split()))

    if k1 != k2:

        # list with all possible options of number of flats per floor
        ls = []

        for i in range(1, 1001):
            if math.ceil(math.ceil(k2 / i) / m) == p2 and math.ceil((k2 - (i * m) * (p2 - 1)) / i) == n2:
                ls.append(i)

        if len(ls) == 0:
            print(-1, -1)

        elif len(ls) == 1:
            x = ls[0]
            p1 = math.ceil(math.ceil(k1 / x) / m)
            n1 = math.ceil((k1 - (x * m) * (p1 - 1)) / x)
            print(p1, n1)

        else:
            p1_vals = set()
            n1_vals = set()

            for i in ls:
                p1 = math.ceil(math.ceil(k1 / i) / m)
                n1 = math.ceil((k1 - (i * m) * (p1 - 1)) / i)
                p1_vals.add(p1)
                n1_vals.add(n1)

            if len(p1_vals) > 1 and len(n1_vals) > 1:
                print(0, 0)

            elif len(p1_vals) == 1 and len(n1_vals) > 1:
                print(*p1_vals, 0)

            elif len(p1_vals) > 1 and len(n1_vals) == 1:
                print(0, *n1_vals)
            else:
                print(*p1_vals, *n1_vals)

    else:
        ls = []
        for i in range(1, 1001):
            if math.ceil(math.ceil(k2 / i) / m) == p2 and math.ceil((k2 - (i * m) * (p2 - 1)) / i) == n2:
                ls.append(i)

        if len(ls) == 0:
            print(-1, -1)
        else:
            print(p2, n2)
import sys


def main():
    """
    Для чтения входных данных необходимо получить их
    из стандартного потока ввода (sys.stdin).
    Данные во входном потоке соответствуют описанному
    в условии формату. Обычно входные данные состоят
    из нескольких строк.
    Можно использовать несколько методов:
    * input() -- читает одну строку из потока без символа
    перевода строки;
    * sys.stdin.readline() -- читает одну строку из потока,
    сохраняя символ перевода строки в конце;
    * sys.stdin.readlines() -- вернет список (list) строк,
    сохраняя символ перевода строки в конце каждой из них.
    Чтобы прочитать из строки стандартного потока:
    * число -- int(input()) # в строке должно быть одно число
    * строку -- input()
    * массив чисел -- map(int, input().split())
    * последовательность слов -- input().split()
    Чтобы вывести результат в стандартный поток вывода (sys.stdout),
    можно использовать функцию print() или sys.stdout.write().
    Возможное решение задачи "Вычислите сумму чисел в строке":
    print(sum(map(int, input().split())))
    """
    #K1, M, K2, P2, N2 = map(int, input().split())
    #P1, N1 = get_flat_params(K1, M, K2, P2, N2)
    #print(P1, N1)
    print_flat_params()
    return
    #pass


if __name__ == '__main__':
    main()
    pass

'''
assert get_flat_params(10, 1, 4, 2, 1) == (0, 1)

assert get_flat_params(89, 20, 41, 1, 11) == (2, 3)
assert get_flat_params(11, 1, 1, 1, 1) == (0, 1)
assert get_flat_params(3, 2, 2, 2, 1) == (-1, -1)
assert get_flat_params(5, 20, 2, 1, 1) == (0, 0)

assert get_flat_params(10, 5, 20, 2, 5) == (1, 5)
assert get_flat_params(10, 5, 20, 4, 5) == (2, 5)
assert get_flat_params(20, 5, 10, 1, 3) == (1, 5)
assert get_flat_params(60, 5, 10, 1, 3) == (3, 5)
assert get_flat_params(55, 5, 20, 2, 2) == (4, 4)
assert get_flat_params(55, 5, 20, 1, 5) == (3, 4)
assert get_flat_params(55, 3, 28, 1, 3) == (2, 0)
assert get_flat_params(20, 4, 5, 1, 2) == (2, 0)
assert get_flat_params(89, 20, 41, 1, 11) == (2, 3)
assert get_flat_params(55, 3, 21, 1, 3) == (0, 0)
assert get_flat_params(55, 3, 30, 1, 3) == (2, 0)
assert get_flat_params(55, 5, 20, 1, 5) == (3, 4)
assert get_flat_params(55, 5, 17, 1, 5) == (3, 4)
assert get_flat_params(55, 5, 4, 1, 1) == (0, 0)
assert get_flat_params(10, 5, 5, 1, 5) == (2, 5)
'''