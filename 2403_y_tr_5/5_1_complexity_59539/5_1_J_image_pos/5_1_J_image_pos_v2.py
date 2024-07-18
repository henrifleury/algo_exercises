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


def check_sur_arr(sur_l, w, h):
    # вернем диапазоны, на уровне h и правее текущей w, занятые sur рисунками

    sur_l = [sur for sur in sur_l if sur[1]<=h<=sur[1]+sur[3]]
    res = []
    nearest_left = sorted([sur[0]-w for sur in sur_l if sur[0]-w>=0])
    if nearest_left:
        nearest_left = nearest_left[0]
        nearest_left = [sur for sur in sur_l if sur[0]-w == nearest_left][0]
        #for sur_left, sur_top, sur_w, sur_h in sur_l:
        res = nearest_left[0], nearest_left[0]+nearest_left[2]
    return sur_l, res

def calc_prgrph(pgph_l):
    pgph_h, pgph_w, sur_l = 0, 0, []
    str_h = h
    last_obj = None
    while len(pgph_l) > 0:
        obj = pgph_l[0]
        if isinstance(obj, list):
            sur_l, nearest_sur = check_sur_arr(sur_l, pgph_w, pgph_h)
            if nearest_sur:
                limit_r, next_w = nearest_sur
            else:
                limit_r, next_w = w, w
            while len(obj) > 0:
                wrd_len = len(obj[0])*s_w
                if pgph_w + wrd_len <= limit_r:
                    pgph_w += wrd_len
                    obj = obj[1:]
                    if pgph_w + s_w <= limit_r:
                        pgph_w += s_w
                else:
                    pgph_w = next_w
                    if pgph_w >= w:
                        pgph_h += str_h
                        str_h = h
                        pgph_w = 0
                        last_obj = None
                    sur_l, nearest_sur = check_sur_arr(sur_l, pgph_w, pgph_h)
                    #limit_r, next_w = nearest_sur[0], nearest_sur[1] if nearest_sur else w, w
                    if nearest_sur:
                        limit_r, next_w = nearest_sur
                    else:
                        limit_r, next_w = w, w

            last_obj = 'text'
        elif obj['layout'] == 'embedded':
            while True: #pgph_w <= w - obj['width']:
                sur_l, nearest_sur = check_sur_arr(sur_l, pgph_w, pgph_h)
                #limit_r, next_w = nearest_sur[0], nearest_sur[1] if nearest_sur else w, w
                if nearest_sur:
                    limit_r, next_w = nearest_sur
                else:
                    limit_r, next_w = w, w

                if limit_r-pgph_w >= obj['width']:
                    print(pgph_w, pgph_h)
                    pgph_w += obj['width']
                    str_h = max(h, obj['height'])
                    last_obj = 'emb'
                    #obj = False
                    break
                else:
                    pgph_w = next_w
                    if pgph_w >= w:
                        pgph_h += str_h
                        str_h = h
                        pgph_w = 0
                        last_obj = None

        elif obj['layout'] == 'surrounded':
            while True:
                if last_obj == "text":
                    pgph_w -= s_w
                sur_l, nearest_sur = check_sur_arr(sur_l, pgph_w, pgph_h)
                #limit_r, next_w = nearest_sur[0], nearest_sur[1] if nearest_sur else w, w
                if nearest_sur:
                    limit_r, next_w = nearest_sur
                else:
                    limit_r, next_w = w, w

                if limit_r-pgph_w >= obj['width']:
                    print(pgph_w, pgph_h)
                    sur_l.append((pgph_w, pgph_h, obj['width'], obj['height']))
                    pgph_w += obj['width']
                    last_obj = 'sur'


                    break
                else:
                    pgph_w = next_w
                    if pgph_w >= w:
                        pgph_h += str_h
                        str_h = h
                        pgph_w = 0
                        last_obj = None
        elif obj['layout'] == 'floating':
            if last_obj == "text":
                pgph_w -= s_w
            if pgph_w + obj['width'] + obj['dx'] > w:
                print(pgph_w - (pgph_w - obj['width'] + obj['dx'] - w), pgph_h + obj['dy'])
            elif pgph_w + obj['dx'] < 0:
                print(pgph_w + (pgph_w - obj['dx']), pgph_h + obj['dy'])
            else:
                print(pgph_w + obj['dx'], pgph_h + obj['dy'])
            if last_obj == "text":
                pgph_w += s_w

        if pgph_w >= w:
            pgph_h += str_h
            str_h = h
            pgph_w = 0
            last_obj = None
        pgph_l = pgph_l[1:]

    return pgph_h







def parse_paragraph(paragraph):
    img_tmplt = '(image'
    img_tmplt_len = len(img_tmplt)
    cur_h = 0
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
        cur_h += calc_prgrph(start_l)




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
