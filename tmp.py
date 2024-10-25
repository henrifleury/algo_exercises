def max_area(heights):
    max_s = 0
    stack = []  # (idx, h)

    #for idx, h in enumerate(heights):
    for idx, h in enumerate(map(int, heights)):
        start = idx
        while stack and stack[-1][1] > h:
            prev_idx, prev_h = stack.pop()
            max_s = max(max_s, prev_h * (idx - prev_idx))
            start = prev_idx
        stack.append((start, h))


    h_len = idx+1
    #print(h_len)
    for idx, h in stack:
        max_s = max(max_s, h * (len(heights) - idx))
    return max_s

#inp = input().split()
#inp = map(int, )

#2 4 3 2 1 4 1
#print(max_area(inp))


def max_rectangle_area(heights):
    stack = []
    max_area = 0
    index = 0

    while index < len(heights):
        # If this bar is higher than the bar at stack top, push it to the stack
        if not stack or heights[stack[-1]] <= heights[index]:
            stack.append(index)
            index += 1
        else:
            # Pop the top
            top_of_stack = stack.pop()
            # Calculate the area with heights[top_of_stack] as the smallest (or minimum height) bar 'h'
            area = (heights[top_of_stack] * ((index - stack[-1] - 1) if stack else index))
            # Update max_area, if needed
            max_area = max(max_area, area)

    # Now pop the remaining bars from stack and calculate area with each popped bar
    while stack:
        top_of_stack = stack.pop()
        area = (heights[top_of_stack] * ((index - stack[-1] - 1) if stack else index))
        max_area = max(max_area, area)

    return max_area


# Пример использования:
heights = [3, 1, 6, 4, 5, 2]  # Пример высот заборов
print(max_rectangle_area(heights))  # Выводит площадь максимального прямоугольника

heights = list(map(int, '2 4 3 2 1 4 1'.split()))
print(max_rectangle_area(heights))  # Выводит площадь максимального прямоугольника