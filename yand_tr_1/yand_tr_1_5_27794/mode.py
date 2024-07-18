inp_list = []
with open("input.txt", "r") as f:
    for line in f.readlines():
        inp_list.append(line.strip())

mayka_nbr = int(inp_list[0])
mayka_colors = list(map(int, inp_list[1].split()))
# найти минимум майки
# найти ближайшие штаны

shtany_nbr = int(inp_list[2])
shtany_colors = list(map(int, inp_list[3].split()))

def dec_color(colors_l, dec_color):
    #norm_col = []
    #for col in colors_l
    return [col - dec_color for col in colors_l]

def get_min_diff(mayka_colors, shtany_colors):

    if not (mayka_colors and shtany_colors):
        return
    if mayka_colors[-1] <= shtany_colors[0]:
        return mayka_colors[-1], shtany_colors[0]
    if mayka_colors[0] >= shtany_colors[-1]:
        return mayka_colors[0], shtany_colors[-1]

    print("mayka_colors", mayka_colors)
    print("shtany_colors", shtany_colors)

    best_pair = (mayka_colors[0], shtany_colors[0])
    abs_min_dist = abs(mayka_colors[0] - shtany_colors[0])

    for i in mayka_colors:
        for j in shtany_colors:
            abs_dist = abs(i-j)
            if abs_dist < abs_min_dist:
                abs_min_dist = abs_dist
                best_pair = (i, j)
            if abs_min_dist == 0:
                break
        if abs_min_dist == 0:
            break
    return best_pair

print(get_min_diff(mayka_colors, shtany_colors))