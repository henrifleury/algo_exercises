# Проверить, правильно ли расставлены скобки в данном коде.
# []{}()

# start_time = time.time()  # время начала выполнения
# end_time = time.time()  # время окончания выполнения
# execution_time = end_time - start_time  # вычисляем время выполнения
# print(f"Время выполнения программы: {execution_time} секунд")

INPUT_F = 'input.txt'
OPEN_BR = set(['[', '{', '('])
CLOSE_BR = set([']', '}', ')'])
CLOSE_BR_PAIRS = {']': '[', '}': '{', ')': '('}

def main(inp_str: str) -> str:
    stack = []
    for i,s in enumerate(inp_str):
        if s in OPEN_BR:
            stack.append((i,s))
        elif s in CLOSE_BR:
            if not stack:
                return i+1
            else:
                if stack[-1][1] == CLOSE_BR_PAIRS[s]:
                    stack.pop()
                else:
                    return i + 1
    if stack:
        return stack[-1][0]+1
    else:
        return 'Success'


if __name__ == '__main__':
    f = open(INPUT_F, 'r')
    inp_str: str = f.readline().strip()
    res = main(inp_str)
    print(res)

assert main('([](){([])})') == 'Success'
assert main('()[]}') == 5
assert main('{{[()]]') == 7
assert main('[]') == 'Success'
assert main('{}[]') == 'Success'
assert main('[()]') == 'Success'

assert main('{[]}()') == 'Success'
assert main('{') == 1
assert main('{[}') == 3
assert main('foo(bar);') == 'Success'

assert main('foo(bar[i);') == 10

assert main("([](){([])})") == 'Success'
assert main("()[]}") == 5
assert main("{{[()]]") == 7
assert main("{{{[][][]") == 3
assert main("{*{{}") == 3
assert main("[[*") == 2
assert main("{*}") == 'Success'
assert main("{{") == 2
assert main("{}") == 'Success'
assert main("") == 'Success'
assert main("}") == 1
assert main("*{}") == 'Success'
assert main("{{{**[][][]") == 3