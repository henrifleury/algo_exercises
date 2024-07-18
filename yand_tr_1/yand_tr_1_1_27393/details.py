#N, K, M = map(int, input().split())

verbose = False
def my_print(*args):
    if verbose:
        print(*args)

def get_det_nbr(mat_w, bil_w, det_w):
    if mat_w < bil_w:
        return 0
    if bil_w < det_w:
        return 0

    det_nbr = 0
    bil_nbr = mat_w // bil_w
    ret_mat = mat_w % bil_w
    bil_det_nbr = bil_w // det_w
    ret_bil_mat = bil_w % det_w
    ret_mat += bil_nbr*ret_bil_mat
    my_print(ret_mat, mat_w, bil_w, det_w)
    det_nbr = bil_nbr*bil_det_nbr
    if ret_mat >= bil_w:
        det_nbr += get_det_nbr(ret_mat, bil_w, det_w)
    return det_nbr

#print(get_det_nbr(N, K, M))

assert get_det_nbr(10, 5, 2) == 4
assert get_det_nbr(13, 5, 3) == 3
assert get_det_nbr(14, 5, 3) == 4