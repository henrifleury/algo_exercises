t0 = pow(33,.5)
tprev = pow(t0,.5)
print(t0, tprev)

n_exp = int(1e2)

exp_counter = 0
while exp_counter<n_exp:
    exp_counter += 1
    tnext = pow(t0+tprev, .5)
    tprev = tnext
    print(tnext)