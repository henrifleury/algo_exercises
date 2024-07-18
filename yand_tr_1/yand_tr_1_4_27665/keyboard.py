'''n_keys = int(input())
key_resourse = list(map(int, input().split()))
n_press = int(input())
key_seq = list(map(int, input().split()))
'''


n_keys = 4
key_resourse = list(map(int, "1 50 3 4 3".split()))
n_press = 16
key_seq = list(map(int, "1 2 3 4 5 1 3 3 4 5 5 5 5 5 4 5".split()))



key_counter=dict()
for key in key_seq:
    key_counter[key] = key_counter.get(key, 0)+1

#print(key_counter)
#key_counter = sorted(key_counter)

for idx, resourse  in enumerate(key_resourse):
    if key_counter[idx+1]>resourse:
        print("YES")
    else:
        print("NO")

