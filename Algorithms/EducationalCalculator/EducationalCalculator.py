# Not completed

Operations = {
    "+": lambda x, y: x+y,
    "-": lambda x, y: x-y,
}
Open = '('
Close = ')'


def find_closing(start, equation):
    stack = []
    stack.append(equation[start])
    def valid(): return len(stack) == 0
    while not valid():
        start += 1
        if equation[start] == Open:
            stack.append(start)
        if equation[start] == Close:
            stack.pop()
    return start


def number_it(equation):
    left = right = 0
    while left < len(equation):
        if equation[left] == Open:
            right = find_closing(left, equation)
            sub_problem = equation[left+1: right]
            yield calculate(sub_problem)
            left = right = right + 1
            continue
        while right < len(equation) and equation[right] not in Operations:
            right += 1
        print(equation, left, right)
        yield int(equation[left:right])
        while not equation[right].isdigit():
            right += 1
            left = right


def sign_it(equation):
    ind = 0
    while ind < len(equation):
        if equation[ind] in Operations:
            yield equation[ind]
        if equation[ind] == Close:
            ind = find_closing(ind, equation) + 1
        ind += 1


def calculate(equation):
    print(equation)
    numbers = number_it(equation)
    signs = sign_it(equation)
    result = next(numbers, None)
    if result == None:
        return 0
    for number in numbers:
        sign = next(signs)
        operator = Operations[sign]
        result = operator(result, number)
        print(result)
    return result


# print(calculate("((24))"))
print('---------')
print("Expect", 21)
print(calculate("5+16-((9-6)-(4-2))+1"))


# print('---------')
# print("Expect", 20)
# print(calculate("22+(2-4)"))
# print('---------')
# print("Expect", 3)
# print(calculate("6+9-12"))
# print('---------')
# print("Expect", 1024)
# print(calculate("((1024))"))
# print('---------')
# print(calculate("1+(2+3)-(4-5)+6"))
# print("Expect", 13)
# print('---------')
# print(calculate("255"))
# print("Expect", 255)
