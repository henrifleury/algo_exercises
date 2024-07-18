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
        res = nearest_left[0], nearest_left[0]+nearest_left[2]#+1
    return sur_l, res

def calc_prgrph(pgph_l, pgph_start_h):
    print(pgph_l)
    #print(pgph_start_h, pgph_l )
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
                #obj = obj[0].split() + obj[1:]
                wrd_len = len(obj[0])*s_w
                if last_obj == "text":
                    wrd_len += s_w
                if pgph_w + wrd_len <= limit_r:
                    pgph_w += wrd_len
                    obj = obj[1:]
                    last_obj = "text"
                    #if pgph_w + s_w <= limit_r:
                        #pgph_w += s_w
                else:
                    #wrd_len += s_w
                    pgph_w = next_w
                    last_obj = 'UNK'
                    if pgph_w >= w:
                        pgph_h += str_h
                        str_h = h
                        pgph_w = 0
                    #else:
                        #if last_obj == "text":
                            #wrd_len -= s_w
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
                emb_width = obj['width']
                if last_obj == "text":
                    emb_width += s_w
                if emb_width < limit_r-pgph_w:
                    if last_obj == "text":
                        print(pgph_w + s_w, pgph_start_h + pgph_h)
                    else:
                        print(pgph_w, pgph_start_h + pgph_h)
                    pgph_w += emb_width
                    str_h = max(str_h, obj['height'])
                    last_obj = 'emb'
                    #obj = False
                    break
                else:
                    pgph_w = next_w
                    last_obj = 'UNK'
                    if pgph_w >= w:
                        pgph_h += str_h
                        str_h = h
                        pgph_w = 0
                        last_obj = None
        elif obj['layout'] == 'surrounded':
            while True:
                #if last_obj == "text":
                    #pgph_w -= s_w
                sur_l, nearest_sur = check_sur_arr(sur_l, pgph_w, pgph_h)
                #limit_r, next_w = nearest_sur[0], nearest_sur[1] if nearest_sur else w, w
                if nearest_sur:
                    limit_r, next_w = nearest_sur
                else:
                    limit_r, next_w = w, w

                if limit_r-pgph_w >= obj['width']:
                    print(pgph_w, pgph_start_h + pgph_h)
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

            if last_obj == "fl":
                prev_right, prev_top = prev_f_w, prev_f_h
                #prev_right = prev_f_w
            else:
                prev_right, prev_top = pgph_w, pgph_h
                #prev_right = pgph_w
            if prev_right + obj['width'] + obj['dx'] > w:
                #floating_w = w - (prev_right + obj['width'] + obj['dx'])
                floating_w = w - obj['width']
                #floating_h = prev_top + obj['dy']
            elif prev_right + obj['dx'] < 0:
                #floating_w = -(prev_right + obj['dx'])
                floating_w = 0
                #floating_h = prev_top + obj['dy']
            else:
                floating_w = prev_right + obj['dx']
            #prev_top = prev_f_h
            floating_h = prev_top + obj['dy']

            print(floating_w, pgph_start_h+floating_h)
            #prev_f_w, prev_f_h = floating_w+obj['width'], prev_top + obj['dy']
            prev_f_w = floating_w + obj['width']
            prev_f_h = floating_h
            last_obj = "fl"


        if pgph_w >= w:
            pgph_h += str_h
            str_h = h
            pgph_w = 0
            last_obj = None
        pgph_l = pgph_l[1:]
    #print(sur_l)

    pgph_h = pgph_h + str_h if pgph_w >0 else pgph_h
    for sur_i in sur_l:
        pgph_h = max(pgph_h, sur_i[1] + sur_i[3])
    return pgph_h







def parse_paragraph(paragraph, cur_h):
    img_tmplt = '(image'
    img_tmplt_len = len(img_tmplt)
    if paragraph:
        img_regex = r"\(image(.*?)\)"
        pattern = re.compile(img_regex)
        img_decr = re.findall(img_regex, paragraph)
        #print('paragraph')#, paragraph)
        start_l, rest = [], paragraph
        for img in img_decr:
            #print('img', img)
            img_id_first = rest.find(img)# - img_tmplt_len
            #print(img, 'img_id_first', img_id_first)
            #print(rest[img_id_first+len(img)+1:])
            #print(rest[:img_id_first])
            tmp_s = rest[:img_id_first - img_tmplt_len].strip()
            tmp_s = ''.join(tmp_s.split('\n'))
            tmp_s = tmp_s.split()
            if tmp_s: start_l.append(tmp_s)
            start_l.append(parse_image(img))
            #print('start_l', start_l)
            rest = rest[img_id_first+len(img)+1:]
            #print('rest', rest)
            #rest[1] = rest[1][1:]
            #rest = ''.join(rest[1:])
        if rest: start_l.append(rest.split())
        #print('start_l', start_l)
        par_h = calc_prgrph(start_l, cur_h)
        return par_h


def parse_paragraph_2(paragraph, cur_h):
    img_tmplt = '(image'
    img_tmplt_len = len(img_tmplt)
    if paragraph:
        img_regex = r"\(image(.*?)\)"
        pattern = re.compile(img_regex)
        img_decr = re.findall(img_regex, paragraph)
        #print('paragraph')#, paragraph)
        start_l, rest = [], paragraph
        for img in img_decr:
            print('img', img)
            img_id_first = rest.find(img)# - img_tmplt_len
            #print(img, 'img_id_first', img_id_first)
            #print(rest[img_id_first+len(img)+1:])
            #print(rest[:img_id_first])
            tmp_s = rest[:img_id_first - img_tmplt_len].strip()
            tmp_s = tmp_s.split('\n')
            #tmp_s = tmp_s.split()
            if tmp_s: start_l.append(tmp_s)
            start_l.append(parse_image(img))
            #print('start_l', start_l)
            rest = rest[img_id_first+len(img)+1:]
            #print('rest', rest)
            #rest[1] = rest[1][1:]
            #rest = ''.join(rest[1:])
        if rest: start_l.append(rest.split())
        #print('start_l', start_l)
        par_h = calc_prgrph(start_l, cur_h)
        return par_h



prph_l, paragraph = [], []
h_cur = 0
for txt_line in txt_file:
    if txt_line == '\n':
        prph_l.append(paragraph)
        paragraph = ''.join(paragraph)
        h_cur += parse_paragraph_2(paragraph, h_cur)# + h
        paragraph = []
    paragraph.append(txt_line)

parse_paragraph_2(''.join(paragraph), h_cur)
