'''len_inp, inp_lst = 5, []
for i in range(len_inp):
    inp_lst.append(int(input()))
a, b, c, d, e = inp_lst
'''
def is_good_hole(a, b, c, d, e):
    brick_sizes = [a,b,c]
    brick_w = max(brick_sizes)
    brick_sizes.pop(brick_w)
    brick_h = min(brick_sizes)
    brick_depth = max(brick_sizes)

    (hole_w, hole_h) = (d, e) if d > e else (e, d)

    if (hole_w >= brick_depth) and (hole_h >= brick_h):
        return "YES"
    if (hole_w >= brick_h) and (hole_h >= brick_depth):
        return "YES"

    if (hole_w >= brick_w) and (hole_h >= brick_h):
        return "YES"
    if (hole_w >= brick_h) and (hole_h >= brick_w):
        return "YES"

    if (hole_w >= brick_w) and (hole_h >= brick_depth):
        return "YES"
    if (hole_w >= brick_depth) and (hole_h >= brick_w):
        return "YES"

    return "NO"

#print(is_good_hole(a, b, c, d, e))

assert is_good_hole(1, 1, 1, 1, 1) == "YES"
assert is_good_hole(2, 2, 2, 1, 1) == "NO"

print(is_good_hole(2, 2, 2, 1, 1))