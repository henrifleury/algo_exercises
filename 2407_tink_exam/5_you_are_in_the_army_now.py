f = open('input.txt', 'r')
n, m = map(int, f.readline().split())
#n, m = map(int, input().split())





pairs = set()
for i in range(m):
    #pairs.add(tuple(map(int, input().split())))
    pairs.add(tuple(map(int, f.readline().split())))

pairs = sorted(pairs)

def check_contradictions(pairs):

    dependencies = {}
    for key1, key2 in pairs:
        if key1 not in dependencies:
            dependencies[key1] = []
        dependencies[key1].append(key2)

    # Создаем пустой список для хранения порядка ключей.
    order = []

    # Проходим по каждому ключу и пытаемся его добавить в порядок.
    for key, values in dependencies.items():
        # Проверяем, есть ли у ключа зависимость от себя самого (цикл).
        if key in dependencies[key]:
            return None

        # Создаем стек для отслеживания зависимостей.
        stack = [key]

        # Пока стек не пуст, продолжаем проверку.
        while stack:
            current_key = stack.pop(0)

            # Проверяем, есть ли у текущего ключа зависимость от ключа, уже добавленного в порядок.
            if current_key in order:
                for v in values:
                    if v in order:
                        continue
                    else:
                        return None
            else:

                # Добавляем ключ в порядок.
                order.append(current_key)

            # Добавляем всех зависимых ключей в стек.
            if current_key in dependencies:
                for dependent_key in dependencies[current_key]:
                    if not dependent_key in stack:
                        stack.append(dependent_key)

    return order


order = check_contradictions(pairs)

if order:
    print("Yes")
    print(order)
else:
    print("No")


