# N - мест, M - часов
def get_min_k(N: int, M: int, max_K:int, Cook_nbr_l: list):
    if M < N:
        return 0
    if N < 1:
        return 0
    '''    
    if M == N:
        return max_K
    if max_K == 1:
        return N
    if N == 1:
        return (Cook_nbr_l[0] + M -1) // M
    '''
    min_K = 1
    while min_K < max_K:
        k_mid = (min_K + max_K)//2
        m_mid = sum((room_c + k_mid - 1) // k_mid for room_c in Cook_nbr_l)
        if m_mid <= M:
            max_K = k_mid
        else:
            min_K = k_mid+1
        #print(k_mid, m_mid, min_K, max_K)
    return min_K

N, M = map(int, input().split())
C_l = []
max_K = 0
# total_cook_nbr = 0
for i in range(N):
    room_cook_nbr = int(input())
    if room_cook_nbr > 0:
        C_l.append(room_cook_nbr)
        max_K = max(max_K, room_cook_nbr)
    else:
        N -= 1
print(get_min_k(N, M, max_K, C_l))    


# N - мест, M - часов
N, M, C_l = 3, 3, [4, 4, 4]
max_K = max(C_l)
res = get_min_k(N, M, max_K, C_l)
assert res == 4


N, M, C_l = 3, 6, [4, 4, 4]
max_K = max(C_l)
res = get_min_k(N, M, max_K, C_l)
assert res == 2


N, M, C_l = 4, 6, [0, 0, 0, 0]
C_l = [i for i in C_l if i >0]
N = len(C_l)
max_K = max(C_l) if C_l else 0
print((N, M, max_K, C_l))
res = get_min_k(N, M, max_K, C_l)
assert res == 0

N, M, C_l = 4, 6, [4, 0, 4, 6]
C_l = [i for i in C_l if i >0]
N = len(C_l)
max_K = max(C_l)
print((N, M, max_K, C_l))
#print(get_min_k(N, M, max_K, C_l))
res = get_min_k(N, M, max_K, C_l)
assert res == 3


N, M, C_l = 3, 3, [4, 4, 5]
max_K = max(C_l)
res = get_min_k(N, M, max_K, C_l)
assert res == 5


N, M, C_l = 3, 6, [4, 4, 5]
max_K = max(C_l)
res = get_min_k(N, M, max_K, C_l)
assert res == 3


N, M, C_l = 3, 2, [4, 4, 5]
max_K = max(C_l)
res = get_min_k(N, M, max_K, C_l)
assert res == 0


N, M, C_l = 1, 2, [4]
max_K = max(C_l)
res = get_min_k(N, M, max_K, C_l)
assert res == 2

N, M, C_l = 1, 1, [4]
max_K = max(C_l)
res = get_min_k(N, M, max_K, C_l)
assert res == 4
