#len_arr = int(input())
#arr = list(map(int, input().split()))


# несколько строк, одно целое в строке
len_inp, inp_lst = 4, []
for i in range(len_inp):
    inp_lst.append(int(input()))
t1, t2, n1, n2 = inp_lst

#
min_max_arr=[]
for i in range(n):
    tmp_s=input()
    min_max_arr.append(list(map(int, tmp_s.split())))


#
inp_lst = []
while True:
    el = int(input())
    if el == -2000000000:
        break
    inp_lst.append(el)


#strWords = ''
word_l = []
f = open('input.txt', 'r')
for line in f:
    #тупильня strWords = strWords + ' ' + line.replace('\n', '')
    word_l += line[:-1].split()
