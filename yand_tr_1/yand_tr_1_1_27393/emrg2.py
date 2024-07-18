# K1, M, K2, P2, N2 = map(int, input().split())
# P1, N1 = get_flat_params(K1, M, K2, P2, N2)
# P1, N1 = get_flat_params(55, 3, 28, 1, 3)
# print(P1, N1)

verbose = False
def my_print(*args):
    if verbose:
        print(*args)

def get_flat_params(K1, M, K2, P2, N2):
    if N2 > M:
        return -1, -1

    #if K1 == K2:
        #return P2, N2
    K2_landing_nbr = M * (P2 - 1) + N2
    if K2_landing_nbr == 1:
        if K1 <= K2:
            return 1, 1
        else:
            if M == 1:
                return 0, 1
            else:
                return 0, 0
    else:    #K2_landing_nbr>1
        #flats_per_floor_min = K2//((P2-1)*M+N2)
        # мудрено, но смысл в том, что если квартира 2 находится на i-m этаже
        prev_land_max_flat_num = K2 - 1
        prev_landing = K2_landing_nbr-1
        # то максимальный номер квартиры пред этажа должен делиться нацело на номер пред этажа и должен быть меньше К2
        flats_per_floor_max = (prev_land_max_flat_num-(prev_land_max_flat_num % prev_landing))//prev_landing
        if flats_per_floor_max<1:
            #if M == 1:
                #return -1, 1
            #if (K1 < K2) & (P2==1):
                #return 1, -1
            #else:
            return -1, -1

        flats_per_floor_list = []
        flats_per_f = flats_per_floor_max
        while flats_per_f*prev_landing < K2 <= flats_per_f*K2_landing_nbr:
            flats_per_floor_list.append(flats_per_f)
            flats_per_f-=1

        P1_set = set()
        N1_set = set()
        my_print(flats_per_floor_list)
        for flats_per_f in flats_per_floor_list:
            fl_per_stair = M*flats_per_f
            #P1 = (K1+1) // fl_per_stair + 1
            P1 = K1 // fl_per_stair + 1 if K1 % fl_per_stair != 0 else K1 // fl_per_stair
            #N1 = (K1+flats_per_f-1) // flats_per_f - M*P1
            N1 = K1 // flats_per_f + 1 if K1 % flats_per_f != 0 else K1 // flats_per_f
            N1 -= M*(P1-1)
            P1_set.add(P1)
            N1_set.add(N1)
            my_print("fl_per_stair, P1, N1, P1_set, N1_set", fl_per_stair, P1, N1, P1_set, N1_set)

        P1 = list(P1_set)[0] if len(P1_set) == 1 else 0
        N1 = list(N1_set)[0] if len(N1_set) == 1 else 0
        my_print(P1, N1)
        return P1, N1


# K1, M, K2, P2, N2 = map(int, input().split())
#get_flat_params(89, 20, 41, 1, 11)
#get_flat_params(75, 2, 15, 1, 2) # 2этажный дом 10 квартир на площадку
#get_flat_params(75, 2, 21, 2, 1) # 2этажный дом 10 квартир на площадку
#get_flat_params(75, 2, 31, 2, 2) # 2этажный дом 10 квартир на площадку
#get_flat_params(75, 2, 40, 2, 2) # 2этажный дом 10 квартир на площадку


assert get_flat_params(5, 3, 8, 3, 3) == (-1, -1)
assert get_flat_params(10, 1, 4, 2, 1) == (0, 1)
assert get_flat_params(10, 10, 11, 1, 3) == (1, 0)

assert get_flat_params(89, 20, 41, 1, 11) == (2, 3)
assert get_flat_params(11, 1, 1, 1, 1) == (0, 1)

assert get_flat_params(3, 2, 2, 2, 1) == (-1, -1)
assert get_flat_params(5, 20, 2, 1, 1) == (0, 0)

assert get_flat_params(18, 9, 36, 2, 9) == (1, 9)
assert get_flat_params(36, 9, 5, 1, 3) == (2, 9)
assert get_flat_params(20, 9, 5, 1, 3) == (2, 1)
assert get_flat_params(20, 10, 5, 1, 5) == (2, 10)
assert get_flat_params(10, 10, 5, 1, 5) == (1, 10)
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

