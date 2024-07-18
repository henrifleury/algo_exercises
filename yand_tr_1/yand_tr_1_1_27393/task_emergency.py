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

def get_flat_params(K1, M, K2, P2, N2):
    if K1 == 1:
        return 1, 1
    if K1 == K2:
        return P2, N2
    if (P2 > 1) & (K2 <= M):
        return -1, -1
    if N2 > M:
        return -1, -1

    K2_landing_nbr = M * (P2 - 1) + N2
    if K2_landing_nbr == 1:
        # то же что и if ((N2==1) & (P2==1)) & (M*(P2-1)+N2==1):
        # если квартира2 в первом подъезде на первом этаже -
        # нельзя определить сколько квартир на лестничной клетке и все остальное
        # кроме некоторых исключений
        if K1 <= K2:
            return P2, N2
        elif M == 1:
            return 0, 1
        else:
            return 0, 0
    # flat_per_floor_l = []
    if K2 == 1:
        # это невозможно, так как выше проверили условие if K2_landing_nbr==1:
        # а кв №1 должна быть в первом подъезде на первом этаже
        return -1, -1
    flat_per_f = K2 // K2_landing_nbr
    #flat_per_floor_l = [flat_per_f]
    flat_per_floor_l = []
    # теперь нужно проверить все возможные варианты количества квартир на площадку
    while flat_per_f >= 1:
        if flat_per_f * (K2_landing_nbr-1) < K2 <= flat_per_f * K2_landing_nbr:
            flat_per_floor_l.append(flat_per_f)
        else:
            break
        flat_per_f -= 1

    #flat_per_f = flat_per_floor_l[0]+1
    flat_per_f = K2 // K2_landing_nbr + 1
    while flat_per_f < 1e6:
        if flat_per_f * (K2_landing_nbr - 1) < K2 <= flat_per_f * K2_landing_nbr:
            flat_per_floor_l.append(flat_per_f)
        else:
            break
        flat_per_f += 1

    N1_set = []  # set()
    P1_set = []  # set()
    for flat_per_f in flat_per_floor_l:
        flat_per_stair = M * flat_per_f

        P1 = (K1 - 1) // flat_per_stair + 1
        P1_set.append(P1)
        N1 = (K1 - (P1 - 1) * flat_per_stair - 1) // flat_per_f + 1
        N1_set.append(N1)
    P1_set, N1_set = set(P1_set), set(N1_set)
    P1 = list(P1_set)[0] if len(P1_set) == 1 else 0
    N1 = list(N1_set)[0] if len(N1_set) == 1 else 0
    return P1, N1


# K1, M, K2, P2, N2 = map(int, input().split())
# P1, N1 = get_flat_params(K1, M, K2, P2, N2)
# P1, N1 = get_flat_params(55, 3, 28, 1, 3)
# print(P1, N1)

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

