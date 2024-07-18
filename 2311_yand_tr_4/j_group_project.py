f = open('input.txt', 'r')
t = int(f.readline())


def if_splitted(n, a, b):
    res_a = int(n / a)
    res_b = int(n / b)

    # print(res_a, res_b, n, a, b, b-a)

    if res_a - res_b:
        return "YES"
    return "NO"


for _ in range(t):
    n, a, b = map(int, f.readline().split())
    # print(n, a, b)
    if (n % a == 0) or (n % b == 0) or (a == 1) or (b == 1):
        print("YES")
    else:
        print(if_splitted(n, a, b))