def deposit(*args):
    cl = args[0]
    sum = int(args[1])
    acc_d[cl] = acc_d.get(cl, 0) + sum

def withdraw(*args):
    cl = args[0]
    sum = int(args[1])
    acc_d[cl] = acc_d.get(cl, 0) - sum

def balance(*args):
    cl = args[0]
    print(acc_d.get(cl, "ERROR"))

def transfer(*args):
    cl1 = args[0]
    cl2 = args[1]
    sum = int(args[2])
    withdraw(cl1, sum)
    deposit(cl2, sum)

def income(*args):
    perc = int(args[0]) / 100
    for k,v in acc_d.items():
        if acc_d[k]>0:
            acc_d[k] = acc_d[k] + int(acc_d[k]*perc)

acc_d = dict()
op_dict = {"DEPOSIT": deposit, "WITHDRAW": withdraw, "BALANCE":balance, "TRANSFER": transfer, "INCOME": income}

#f = open('input.txt', 'r')

f = ["DEPOSIT Ivanov 100", "INCOME 5", "BALANCE Ivanov", "TRANSFER Ivanov Petrov 50", "WITHDRAW Petrov 100",
     "BALANCE Petrov", "BALANCE Sidorov"]

f = """BALANCE a
BALANCE b
DEPOSIT a 100
BALANCE a
BALANCE b
WITHDRAW a 20
BALANCE a
BALANCE b
WITHDRAW b 78
BALANCE a
BALANCE b
WITHDRAW a 784
BALANCE a
BALANCE b
DEPOSIT b 849
BALANCE a
BALANCE b""".split("\n")
print(f)

#for line in f.readlines():
for op in f:
    op_dict[op.split()[0]](*op.split()[1:])


