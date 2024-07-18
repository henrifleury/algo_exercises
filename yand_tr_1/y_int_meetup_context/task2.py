import numpy as np
#from math import exp, cos
import random

inp_list = []
with open("data1.txt", "r") as f:
    for line in f.readlines():
        inp_list.append(list(map(float, line.strip().split())))

x_y = np.array(inp_list)
x = x_y[:,0]
y = x_y[:,1]

def my_func(a,b,c,x):
    first_brackets = (a*np.exp(x) + b*np.power(x, .75))
    return first_brackets*first_brackets + c * np.cos(x)*np.cos(x)

#print(my_func(1,0,0,3.692393498914544))
def err(a,b,c):

    return np.sum(np.abs(my_func(a,b,c,x)-y))

#a,b,c = [1,1,1]
#print(my_func(a,b,c,x))

pop_list = []
n_pop = 2
pop_bot_nbr = 2
not_mut = .6
dec_mut = .1
ep_dec = 200

for idx in range(n_pop):
    bot_l=[]
    for j in range(pop_bot_nbr):
        bot_l.append(np.random.sample(3))

    pop_list.append(np.random.sample(3))


n_dead = pop_bot_nbr // 2



