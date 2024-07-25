n,k,a,m = map(int, input().split())
#n,k,a,m = map(int, '3 1000 252149039 281474977'.split())
def lcg(e):
    return (a * e + 11) % m

def generator(seed):
    #sequence = []
    total_counter = n*3
    portion = k*3
    cur = 0
    coin_counter = 0
    while True:
        coin_counter += 1
        seed = lcg(seed)
        next = (abs(seed % 3 - 1) * 5 + abs(seed % 3) * 2) % 8
        cur += next
        if cur >= portion:
            candies = cur // 3
            candies_sum = candies * 3
            total_counter -= candies_sum
            cur -= candies_sum
        #print(next)

        if total_counter <=0:
            break
    print(coin_counter)

gen = generator(0)


