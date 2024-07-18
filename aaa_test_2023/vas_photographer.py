"""
Телефон Василия по умолчанию сохраняет фотографии в следующем формате:
 PXL_20230430_092422111.jpg (Пример 1)
где:
    PXL - префикс производителя телефона
    2023 - год
    04 - месяц
    30 - день
    09 - час GMT+0
    24 - минута
    22111 - микросекунды
    jpg - расширение файла
Василий знает, что это фото с мероприятия, которое он посетил - этап чемпионата по дрифту - и хочет переименовать файл на будущее. Из всех форматов, которые он перепробовал, самым подходящим показался следующий:
DRIFT_2023_04_30.jpg (Пример 2).
где:
    DRIFT - название события
    2023 - год
    04 - месяц
    30 - день
    jpg - расширение файла
Напишите программу, чтобы помочь Василию переименовать этот файл из первого формата во второй.
Условия:
    На вход подаётся строка - название файла. Формат как в Примере 1.
    На выходе ожидается строка - название файла. Формат как в Примере 2.
    Проверка осуществляется на большом количестве тестовых "файлов", предполагается, что все фотографии с одного мероприятия, поэтому префикс "DRIFT" в финальном названии для всех них будет одинаковым.
"""
SPLITTER_L = ["_", "-"]
NEW_SPLITTER = "_"
NEW_PREFIX = "DRIFT"
YEAR_LEN = 4
MONTH_LEN = 2
DAY_LEN = 2
EXT_SPLITTER = "."

#old_f_name = input()
#old_f_name = "202304300924-1.jpg"
#old_f_name = "PXL_20190830_143399492.jpg"
#old_f_name = "DCIM-2023-04-30-1.jpg"
#old_f_name = "PXL_20230430_092422111.jpg"
#old_f_name = "DCIM-2005-07-08-8.jpg"
old_f_name = "DCIM-2009-01-24-10.jpg"


ext_start = old_f_name.rfind(EXT_SPLITTER)
ext_s = old_f_name[ext_start+1:]
old_f_short_name = old_f_name[:ext_start]

res = ""
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
        else:
            # случай когда дата слитно
            old_pref_len = -1
            if len(old_sh_name_splitted_l) == 2:
                #некоторые проблемы с неймингом пока пропустим ради минимума изменений в коде
                old_f_name = old_sh_name_splitted_l[0]
            else:
                #некоторые проблемы с неймингом пока пропустим ради минимума изменений в коде
                old_f_name = old_sh_name_splitted_l[1]
            year_start, year_end = old_pref_len + 1, old_pref_len + 1 + YEAR_LEN
            year_s = old_f_name[year_start:year_end]
            m_start, m_end = year_end, year_end + MONTH_LEN
            month_s = old_f_name[m_start: m_end]
            d_start, d_end = m_end, m_end + DAY_LEN
            day_s = old_f_name[d_start: d_end]

        new_f_name_parts = [NEW_PREFIX, year_s, month_s, day_s]
        #print("new_f_name_parts", new_f_name_parts)
        res = NEW_SPLITTER.join(new_f_name_parts)+EXT_SPLITTER+ext_s
        break
print(res)
