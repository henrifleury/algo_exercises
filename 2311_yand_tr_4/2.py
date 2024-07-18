"""Даны две рациональные дроби: a/b и c/d. Сложите их
 и результат представьте в виде несократимой дроби m/n."""
def gcd(n1, n2):
    low, big = (n1, n2) if n1 < n2 else (n2, n1)
    if low == 0:
        return big
    else:
        return gcd(low, big % low)

f = open('input.txt', 'r')
a, b, c, d = map(int, f.readline().split())
m, n = a*d+b*c, b*d

gcd_m_n = gcd(m, n)

print(m // gcd_m_n, n // gcd_m_n)