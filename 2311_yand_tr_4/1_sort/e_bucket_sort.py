f = open('input.txt', 'r')
n = int(f.readline())
arr = []
for i in range(n):
    arr.append(f.readline().strip())

print("Initial array:")
print(', '.join(arr))
print("**********")

def log_phase(phase_id, phase_dict):
    print(f"Phase {phase_id}")
    for k, v in phase_dict.items():
        print(f"Bucket {k}: {', '.join(v) if v else 'empty'}")
    print("**********")

empty_dict = {str(i):[] for i in range(10)}
s_len = len(arr[0])
cur_dict = {k: v[:] for k, v in empty_dict.items()}
for s in arr:
    #cur_dict[s[-1]] = cur_dict[s[-1]].append(s)
    cur_dict[s[-1]].append(s)
log_phase(1, cur_dict)

phase_id = 2
for idx in range(s_len-1)[::-1]:
    new_dict = {k: v[:] for k, v in empty_dict.items()}
    for v in cur_dict.values():
        for s in v:
            new_dict[s[idx]].append(s)
    cur_dict = {k: v[:] for k, v in new_dict.items()}
    #print(cur_dict)
    log_phase(phase_id, cur_dict)
    phase_id+=1

#print("**********")
print("Sorted array:")
res = []
for v in cur_dict.values():
    res += v
print(', '.join(res))