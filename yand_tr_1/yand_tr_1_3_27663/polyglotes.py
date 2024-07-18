'''len_arr = int(input())
lang_lst=[]
for i in range(len_arr):
    lang_nbr = int(input())
    pup_list=[]
    for j in range(lang_nbr):
        pup_list.append(input())
    lang_lst.append(pup_list)
'''
def print_lang(lang_lst):
    lang_dict={}
    for pup_lang in lang_lst:
        for lang in pup_lang:
            lang_dict[lang] = lang_dict.get(lang, 0)+1

    comm_lang=[]
    for k,v in lang_dict.items():
        if v == len(lang_dict):
            comm_lang.append(k)

    print(len(comm_lang))
    for lang in comm_lang:
        print(lang)

    print(len(lang_dict))
    for lang in lang_dict.keys():
        print(lang)

lang_lst=[["Russian", "English", "Japanese"], ["Russian", "English"], ["English"]]
print_lang(lang_lst)

