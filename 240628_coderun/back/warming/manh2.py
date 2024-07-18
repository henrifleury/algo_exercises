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

    START_COORD = (0, 0)

    def get_manh_dist(coord_1, coord_2):
        return abs(coord_2[0] - coord_1[0]) + abs(coord_2[1] - coord_1[1])

    def get_coord_enabled(cur_coord, cur_t):
        cur_step_set = set([tuple(cur_coord)])
        cur_x, cur_y = cur_coord
        dx = [1, -1, 0, 0]  # 0]
        dy = [0, 0, 1, -1]  # 0]

        for i in range(4):
            next_x, next_y = cur_x + dx[i], cur_y + dy[i]
            cur_step_set.add((next_x, next_y))
        if cur_t == 1:
            return cur_step_set
        else:
            res_step = cur_step_set.copy()
            for coord in cur_step_set:
                res_step |= get_coord_enabled(coord, cur_t - 1)
            return res_step

    def get_points(coord_l):
        prev_coord_set = set([START_COORD])
        navy_coord_enabled = set()
        for navy_coord in coord_l:
            cur_coord_set = prev_coord_set.copy()
            for path_coord in prev_coord_set:
                cur_coord_set |= get_coord_enabled(path_coord, t)
            # print('path_coord', len(cur_coord_set) ,cur_coord_set)
            # navy_coord_enabled.add(navy_coord)
            navy_coord_enabled = get_coord_enabled(navy_coord, d)
            # print('navy_coord_enabled', navy_coord_enabled)
            cur_coord_set = cur_coord_set & navy_coord_enabled
            # print('cur_coord_set', cur_coord_set)
            prev_coord_set = cur_coord_set
        return cur_coord_set

    res = get_points(coord_l)
    print(len(res))
    for coord in res:
        print(*coord)

    pass


if __name__ == '__main__':
    main()



