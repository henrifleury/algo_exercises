word_l = []
#f = open('input.txt', 'r')
buy_dict = dict()

f = ["Ivanov paper 10", "Petrov pens 5", "Ivanov marker 3", "Ivanov paper 7", "Petrov envelope 20", "Ivanov envelope 5"]
#for line in f.readlines():
for line in f:
    buyer, position, q = line.split()
    q = int(q)
    stock_dict = buy_dict.get(buyer, dict())
    stock_dict[position] = stock_dict.get(position, 0) + q
    buy_dict[buyer] = stock_dict

for buyer in sorted(buy_dict.keys()):
    print(f"{buyer}:")
    stock_dict = buy_dict.get(buyer, dict())
    for k in sorted(stock_dict.keys()):
        print(f"{k} {stock_dict[k]}")


