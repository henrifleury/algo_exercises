def count_happy_seqs(seq, happy_n):
    if len(seq) == 0:
        return 0
    if len(seq)==1:
        if seq[0]==happy_n:
            return 1
        else:
            return 0
    i, j = 0, 0 # длину списка проверили,
    sub_seq_sum = 0
    n_happy_seqs = 0
    #for j, cur_n in enumerate(seq):
    while j < len(seq):
        print(i, j, len(seq), sub_seq_sum)
        if sub_seq_sum<happy_n:
            sub_seq_sum += seq[j]
            j += 1
        while i<j and sub_seq_sum>=happy_n:
            if sub_seq_sum == happy_n:
                n_happy_seqs += 1
            sub_seq_sum -= seq[i]
            i += 1


    return n_happy_seqs

inp_list = []
with open("input.txt", "r") as f:
    for line in f.readlines():
        inp_list.append(line.strip())
n_parking_car, happy_n = map(int, inp_list[0].split())
reg_nbrs = list(map(int, inp_list[1].split()))
print(count_happy_seqs(reg_nbrs, happy_n))