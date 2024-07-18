def let_only_good_sym(s):
    res = []
    for sym in s:
        if sym.isalpha() or sym.isdigit() or sym=="_":
            res.append(sym)
        else:
            res.append(" ")
    return ''.join(res)

def is_correct(w, first_dig_enable_flag):
    if w.isdigit():
        return False
    if not w[0].isdigit() or first_dig_enable_flag:
        return True
    return False

# загрузить длину словаря ключевых слов и 2 переменные - чувствительность к регистру и доступность первой цифры в имени
inp_list=[]
with open("input.txt", "r") as f:
    for line in f.readlines():
        inp_list.append(line.strip())
len_voc, reg_sense_f, first_dig_en_f = (inp_list[0].split())
len_voc = int(len_voc)
reg_sense_f = reg_sense_f == "yes"
first_dig_en_f = first_dig_en_f == "yes"

# создать множество ключевых слов и заполнить построчным чтением len_voc слов
voc_s = set()
for idx in range(1, len_voc+1):
    voc_w = inp_list[idx].strip()
    if not reg_sense_f:
        voc_w = voc_w.lower()
    voc_s.add(voc_w)
# завести словарь для подсчета операндов и скорости вхождения
op_d = dict()
# сделать счетчик слов
w_counter = 0
# построчно загрузить текст программы
for prog_str in inp_list[len_voc+1:]:
    # для каждой строки
    # заменить все кроме букв, цифр и подчеркивания на пробел
    prog_str = let_only_good_sym(prog_str)
    # сделать сплит по пробелам
    word_l = prog_str.split()
    # каждое слова проверить на словарность с учетом регистра
    for w in word_l:
        w_counter+=1
        if not reg_sense_f:
            w = w.lower()
        if w in voc_s:
            continue
        if is_correct(w, first_dig_en_f):
            # если не словарное - занести в словарь с учетом чувствительности к регистру и разрешения на цифру
            if w not in op_d:
                # если слово встретилось впервые - занести позицию первого входа
                op_d[w] = [0, w_counter]
            op_d[w][0] += 1

best_op = ''
best_op_pos = [0, 0]
# найти макс числа вхождений
 # найти самое раннее вхождение (можно одновременно? - нет в одном случае минимум в другом - макс)
for w, [op_nbr, op_occ] in op_d.items():
    if op_nbr == best_op_pos[0]:
        if op_occ < best_op_pos[1]:
            best_op = w
            best_op_pos[1] = op_occ
    if op_nbr > best_op_pos[0]:
        best_op = w
        best_op_pos = [op_nbr, op_occ]

print(best_op)

