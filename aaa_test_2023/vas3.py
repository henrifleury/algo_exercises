SPLITTER_L = ["_", "-"]
NEW_SPLITTER = "_"
NEW_PREFIX = "DRIFT"
YEAR_LEN = 4
MONTH_LEN = 2
DAY_LEN = 2
EXT_SPLITTER = "."

EVENTS_NBR = 3
FILES_NBR = 9

def get_new_f_name(old_f_name):
    ext_start = old_f_name.rfind(EXT_SPLITTER)
    ext_s = old_f_name[ext_start+1:].strip()
    old_f_short_name = old_f_name[:ext_start]

    res, event_key, time_code = "", "", ""
    for splitter in SPLITTER_L:
        old_sh_name_splitted_l = old_f_short_name.split(splitter)
        #print(splitter, old_sh_name_splitted_l, len(old_sh_name_splitted_l))
        if len(old_sh_name_splitted_l) <= 1:
            continue
        else:
            if len(old_sh_name_splitted_l)>3:
                #случай когда дата разбита
                year_s = old_sh_name_splitted_l[1]
                month_s = old_sh_name_splitted_l[2]
                day_s = old_sh_name_splitted_l[3]
                time_code = old_sh_name_splitted_l[4]
            else:
                # случай когда дата слитно
                old_pref_len = -1
                if len(old_sh_name_splitted_l) == 2:
                    #некоторые проблемы с неймингом пока пропустим ради минимума изменений в коде
                    old_f_name = old_sh_name_splitted_l[0]
                    time_code = old_f_name[YEAR_LEN + MONTH_LEN + DAY_LEN:]
                    #print(old_f_name, time_code)
                else:
                    #некоторые проблемы с неймингом пока пропустим ради минимума изменений в коде
                    old_f_name = old_sh_name_splitted_l[1]
                    time_code = old_sh_name_splitted_l[2]
                year_start, year_end = old_pref_len + 1, old_pref_len + 1 + YEAR_LEN
                year_s = old_f_name[year_start:year_end]
                m_start, m_end = year_end, year_end + MONTH_LEN
                month_s = old_f_name[m_start: m_end]
                d_start, d_end = m_end, m_end + DAY_LEN
                day_s = old_f_name[d_start: d_end]

            new_f_name_parts = [NEW_PREFIX, year_s, month_s, day_s]
            #print("new_f_name_parts", new_f_name_parts)
            #res = NEW_SPLITTER.join(new_f_name_parts)#+EXT_SPLITTER+ext_s
            #event_key = "".join(new_f_name_parts[1:])
            break
    return new_f_name_parts[1:], ext_s, time_code

#old_f_name = input()
#old_f_name = "202304300924-1.jpg"
#old_f_name = "PXL_20190830_143399492.jpg"
#old_f_name = "DCIM-2023-04-30-1.jpg"
#old_f_name = "PXL_20230430_092422111.jpg"
#old_f_name = "DCIM-2005-07-08-8.jpg"
#old_f_name = "DCIM-2009-01-24-10.jpg"

f = open('input.txt', 'r')

pref_dict = dict()
rev_pref_dict = dict()
event_f_dict = dict()

for i in range(EVENTS_NBR):
    ev_splitted = f.readline().split()
    event_k = "".join(ev_splitted[1:])
    event_f_dict[event_k]=[]
    pref_dict[event_k] = ev_splitted[0]
    rev_pref_dict[ev_splitted[0]] = pref_dict[event_k]
print(pref_dict)

for i in range(FILES_NBR):
    #old_f_name = input()
    old_f_name = f.readline()
    new_f_name_no_time_id, ext_s, time_code = get_new_f_name(old_f_name)
    event_k = "".join(new_f_name_no_time_id)
    event_f_dict[event_k].append((new_f_name_no_time_id, ext_s, time_code))
#print(event_f_dict['20211127'])
for k,v in event_f_dict.items():
    event_f_dict[k] = sorted(v)
#print(event_f_dict)
#dict_keys(['20211127', '20041218', '20020802'])

#for k,v in sorted(pref_dict.values()):
