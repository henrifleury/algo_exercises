'''VOC_LEN = int(input())
INP_LST = []
for i in range(VOC_LEN):
    INP_LST.append(input().split())
ASK = input()
'''

INP_LST = [["Hello", "Hi"], ["Bye", "Goodbye"], ["List", "Array"]]
ASK = "Goodbye"

def get_vocs(syn_list):
    voc = dict()
    rev_voc = dict()
    for s1,s2 in syn_list:
        voc[s1]=s2
        rev_voc[s2] = s1
    return voc, rev_voc



voc, rev_voc = get_vocs(INP_LST)
print(voc. get(ASK, rev_voc.get(ASK,"")))
