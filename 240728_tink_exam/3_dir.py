'''
Понятная файловая система — залог успеха любой операционной системы. К сожалению, не каждая файловая система может похвастаться таким свойством. Но, как говорится, если что-то хочешь сделать хорошо — сделай это сам! Хочется иметь удобное для просмотра представление директорий, чтобы можно было видеть, какие директории в какие вложены.

Для этого требуется по списку директорий вывести их перечисление в алфавитном порядке. При этом вложенные директории должны быть выведены с отступом на два пробела больше, чем у родительской.

Формат входных данных

В первой строке дано число ﻿nn﻿ — количество директорий ﻿(1≤n≤105)(1≤n≤105)﻿. В следующих ﻿nn﻿ строках по одному в строке заданы абсолютные пути ко всем директориям, каждый абсолютный путь — это последовательность вложенных папок, начиная с корневой, разделенная символами "﻿//﻿".

Гарантируется, что первая директория во всех путях одинаковая и имеет непустое имя. Имена всех директорий состоят из маленьких латинских букв и имеют длину не более ﻿1010﻿. Гарантируется, что если директория выведена, то выведены и все, в которые она вложена.

Формат выходных данных

Выведите перечисление всех директорий, в котором все директории внутри одной упорядочены по алфавиту, вложенные идут сразу после родительской и имеют отступ на два пробела больше, чем у нее.
'''

def main(dir_d):

    tree = dict()
    sorted_levels= sorted(dir_d.keys())
    tree = {k: [] for k in dir_d[1][0]}
    print(tree)
    for level in sorted_levels[1:]:
        dirs_cur_level = dir_d[level]
        for dir_name_list in dirs_cur_level:
            tree[level-1][dir_name_list[-2]].append({dir_name_list[-1]: []})


def get_tree(root_dir, tree, dir_d, cur_level):
    for dir_name_l in dir_d[cur_level]:
        cur_branch = tree[root_dir]
        for dir_level in range(1, cur_level):
            cur_branch = cur_branch[dir_name_l[dir_level]]
        cur_branch[dir_name_l[-1]] = dict()
        #print(cur_branch, dir_name_l[-1])

def print_tree(tree, level=0):
    for k in tree:
        print(2*level*' ', end='')
        print(k)
        print_tree(tree[k], level+1)

if __name__ == '__main__':
    f = open('input.txt', 'r') ##
    n = int(f.readline())
    #n = int(input())
    dir_d = dict()
    for i in range(n):
        dir_l: str = f.readline().strip().split('/') ##
        #dir_l = input().strip().split('/')
        level = len(dir_l)-1
        if not level in dir_d:
            dir_d[level] = []
        dir_d[level].append(dir_l)
    cur_level = 0
    tree = dict()
    root_dir = dir_d[cur_level][0][0]
    tree[root_dir] = dict()
    for cur_level in sorted(dir_d.keys())[1:]:
        get_tree(root_dir, tree, dir_d, cur_level)
    print_tree(tree)

    #dir_tree = main(dir_d)
    #print(dir_tree)


'''    
    
    n = int(input())
    dir_d = dict()
    for i in range(n):
        dir_l = input().strip().split('/')
        if not len(dir_l) in dir_d:
            dir_d[len(dir_l)] = []
        dir_d[len(dir_l)].append(dir_l)

    dir_tree = main(dir_d)
    print(dir_tree)'''