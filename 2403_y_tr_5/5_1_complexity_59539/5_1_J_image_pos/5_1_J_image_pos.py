test_f_name = 'input.txt'
f = open(test_f_name, 'r')

txt_file = f.readlines()
w, h, s_w = list(map(int, txt_file[0].split()))
# w - ширина документа, h - высота строки, s_w - ширина символа
txt_file = txt_file[1:]
import re

def parse_image(img_line):
    res = dict()
    if img_line:
        res = {param.split('=')[0]: param.split('=')[1] for param in img_line.split()}
        res = {k: v if k == 'layout' else int(v) for k, v in res.items()}
    return res


def check_sur_arr(sur_l, h, w):
    # вернем диапазоны, на уровне h и правее текущей w, занятые sur рисунками

    res = []
    for sur_left, sur_top, sur_w, sur_h in sur_l:
        if sur_top <= h <= sur_top + h:
            if sur_left >= w:
                res = [sur_left, sur_left + sur_w]
                break
    return res

def calc_prgrph(obj_l):
    cur_h = 0
    cur_w = 0
    next_h = h
    obj = obj_l[0]
    sur_l = []
    while obj_l:
        if not obj:
            obj = obj_l[0]
        #if type(obj) == "class 'str'":
        if isinstance(obj, list) and len(obj)>0:
            sur_img = check_sur_arr(sur_l, h, cur_w)
            w_r_limit, next_w = sur_img if sur_img else w, 0
            #tmp_s = ""
            while len(obj) > 0:
                wrd = obj[0]
                if wrd:
                    if len(wrd) * s_w <= (w_r_limit - cur_w):
                        if len(wrd) * s_w == (w_r_limit - cur_w):
                            cur_w = next_w
                            break
                        cur_w += (len(wrd)+1)*s_w
                        obj = obj[1:]
                    else:
                        #cur_w = next_w
                        break
                else:
                    obj = obj[1:]
            if not obj:
                obj = False
                obj_l = obj_l[1:]
            if cur_w >= w:
                cur_h += next_h
                next_h = h
                cur_w = 0

        elif obj['layout'] == 'embedded':
            cur_img_w = obj['width'] if cur_w == 0 else obj['width']+1
            sur_imges = check_sur_arr(sur_l, h, cur_w)
            for (l, r) in sur_imges:
                if cur_img_w <= (l - cur_w):
                    print(cur_w, cur_h)
                    cur_w += cur_img_w
                    obj_l = obj_l[1:]
                    obj = False
                    next_h = max(obj['height'], h)
                    break
                else:
                    cur_w = r
            if obj and (cur_img_w <= (w - cur_w)):
                print(cur_w, cur_h)
                cur_w += cur_img_w
                obj_l = obj_l[1:]
                next_h = obj['height']
                obj = False
            else:
                cur_h += next_h
                next_h = h
                cur_w = 0

        elif obj['layout'] == 'surrounded':
            cur_img_w = obj['width']
            sur_imges = check_sur_arr(sur_l, h, cur_w)
            for (l, r) in sur_imges:
                if cur_img_w <= (l - cur_w):
                    print(cur_w, cur_h)
                    sur_l.append((cur_w, cur_h, obj['width'], obj['height']) )
                    cur_w += cur_img_w
                    obj_l = obj_l[1:]
                    obj = False
                    break
                else:
                    cur_w = r
            if obj != False and (cur_img_w <= (w - cur_w)):
                print(cur_w, cur_h)
                sur_l.append((cur_w, cur_h, obj['width'], obj['height']))
                cur_w += cur_img_w
                obj_l = obj_l[1:]
                obj = False
            else:
                cur_h += next_h
                next_h = h
                cur_w = 0
        elif obj['layout'] == 'floating':
            if cur_w + obj['width'] + obj['dx'] > w:
                print(cur_w + obj['width'] + obj['dx'] - w, cur_h)
            elif cur_w + obj['dx'] <0:
                print(-(cur_w + obj['dx']), cur_h)
            else:
                print(cur_w + obj['dx'] - w, cur_h)



def parse_paragraph(paragraph):
    img_tmplt = '(image'
    img_tmplt_len = len(img_tmplt)
    if paragraph:
        img_regex = r"\(image(.*?)\)"
        pattern = re.compile(img_regex)
        img_decr = re.findall(img_regex, paragraph)
        #print('paragraph')#, paragraph)
        start_l, rest = [], paragraph
        img_d_l = []
        for img in img_decr:
            #img_d_l.append(parse_image(img))
            rest = rest.split(img)
            tmp_s = rest[0][:-img_tmplt_len].strip()#.split('\n')
            tmp_s = ''.join(tmp_s.split('\n'))
            tmp_s = tmp_s.split()
            if tmp_s: start_l.append(tmp_s)
            start_l.append(parse_image(img))
            rest[1] = rest[1][1:]
            rest = ''.join(rest[1:])
        print(start_l)
        cur_w = calc_prgrph(start_l)




prph_l, paragraph = [], []
for txt_line in txt_file:
    if txt_line == '\n':
        prph_l.append(paragraph)
        paragraph = ''.join(paragraph)
        parse_paragraph(paragraph)
        paragraph = []
    paragraph.append(txt_line)

parse_paragraph(''.join(paragraph))
#prph_l.append(paragraph)



#print(len(prph_l), prph_l)
#parse_image(txt_line)
