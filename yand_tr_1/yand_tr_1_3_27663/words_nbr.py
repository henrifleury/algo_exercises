input_str = """She sells sea shells on the sea shore;
The shells that she sells are sea shells I'm sure.
So if she sells sea shells on the sea shore,
I'm sure that the shells are sea shore shells.
"""

#input_str = input()

"""word_set = set()
prev_idx=0
for idx, s in enumerate(input_str):
    if (s == " ") or (s=="\n"):
        word_set.add(input_str[prev_idx: idx])
        prev_idx = idx+1
print(len(word_set))
"""

print(len(set(input_str.split())))