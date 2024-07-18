g, s = map(int, input().split())
w = input()
seq = input()
'''
g,s = 4,11
w = "cAda"
seq = "AbrAcadAbRa"
'''

maya_w_counter = 0

if (g < 1) | (g > s):
    pass
else:
    w_dict = dict()
    for sym in w:
        w_dict[sym] = w_dict.get(sym, 0) + 1
    # print(w_dict)

    maybe_w = seq[:g - 1]  # для старта 3 символа, четвертый в цикле
    maybe_w_dict = dict()
    for sym in maybe_w:
        maybe_w_dict[sym] = maybe_w_dict.get(sym, 0) + 1

    st = 0
    len_w_dict = len(w_dict)
    while st <= s - g:
        sym = seq[st + g - 1]
        maybe_w_dict[sym] = maybe_w_dict.get(sym, 0) + 1
        # print(maybe_w_dict)

        # if w_dict == maybe_w_dict:
        win_counter = 0
        for k in w_dict.keys():
            if w_dict[k] == maybe_w_dict.get(k, None):
                win_counter += 1
        if win_counter == len_w_dict:
            maya_w_counter += 1

        if maybe_w_dict[seq[st]] == 1:
            del maybe_w_dict[seq[st]]
        else:
            maybe_w_dict[seq[st]] -= 1
        st += 1

print(maya_w_counter)
'''
lenW, lenS = map(int, input())
w = input()
s = input()
'''

lenW, lenS = 4,11
w = "cAda"
s = "AbrAcadAbRa"


def makeDict(s):
    sDict = {}
    for c in s:
        if c not in sDict:
            sDict[c] = 0
        sDict[c] += 1
    return sDict

def matchDicts(dict1, dict2):
    matches = 0
    for c in dict1:
        if c in dict2 and dict1[c]==dict2[c]:
            matches+=1
    return matches


def modDict(sDict, wDict, sym, countMod):
    ans=0
    if sym not in sDict:
        sDict[sym] = 0
    if sym in wDict and sDict[sym] == wDict[sym]:
        ans = -1
    sDict[sym] += countMod
    if sym in wDict and sDict[sym] == wDict[sym]:
        ans=1
    return ans



wDict = makeDict(w)
sDict = makeDict(s[:lenW])
matchingLetters = matchDicts(wDict, sDict)
occurrences = 0
if matchingLetters==len(wDict):
    occurrences+=1

for i in range(lenW, lenS):
    matchingLetters += modDict(sDict, wDict, s[i-lenW], -1)
    matchingLetters += modDict(sDict, wDict, s[i], +1)
    if matchingLetters == len(wDict):
        occurrences += 1
print(occurrences)