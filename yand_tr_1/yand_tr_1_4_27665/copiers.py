#f = open('input.txt', 'r')
#txt_lines = f.readlines()

'''txt_lines = ["0 yes no", "int main() {", "  int a;", "  int b;", '  scanf("%d%d", &a, &b);', '  printf("%d", a + b);',
"}"
]
'''

#txt_lines = ['0 yes no','#define INT int','int main() {','  INT a, b;','  scanf("%d%d", &a, &b);','  printf("%d %d", a + b, 0);','}']
txt_lines = ['1 yes yes','_','a = 0h','b = 0h','c = 0h']

len_voc, reg_sense, first_dig_en = txt_lines[0].split()
len_voc = int(len_voc)
reg_sense = True if reg_sense == "yes" else False
first_dig_en = True if first_dig_en == "yes" else False

voc_set = set()
for idx in range(1, len_voc+1):
    if reg_sense:
        voc_set.add(txt_lines[idx])
    else:
        voc_set.add(txt_lines[idx].upper())

id_counter = dict()
most_freq = 0
most_freq_id = ''
for text_str in txt_lines[len_voc+1:]:
    word = []
    word_l = []
    only_dig = True
    for idx, sym in enumerate(text_str):
        if ((ord(sym) >= 65) and (ord(sym) <= 122)) or ((ord(sym) >= 48) and (ord(sym) <= 57)) or (ord(sym) == 95):
            word.append(sym)
            if ord(sym) > 57: # будет ошибка если ключевые слова могут состоять из цифр
                only_dig = False
        else:
            if word:
                if not only_dig:
                    word_l.append(''.join(word))
                word = []
    if word:
        if not only_dig:
            word_l.append(''.join(word))
        #word = []
    for word in word_l:
        if not reg_sense:
            word = word.upper()
        if word not in voc_set:
            if (not first_dig_en) and (ord(word[0]) <= 57):
                continue
            else:
                id_freq = id_counter.get(word, 0)
                new_freq = id_freq + 1
                id_counter[word] = new_freq
                if new_freq > most_freq:
                    most_freq_id = word
                    most_freq = new_freq


print(most_freq_id)


