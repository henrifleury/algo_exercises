f = open('input.txt', 'r')

k, n = map(int, f.readline().split())
pr_list = sorted(map(int, f.readline().split()))

print(sum(pr_list) * (n // k) + sum(pr_list[:n % k]))
