class InvalidInputError(Exception):
    pass

def input_string(msg):
    l = str(input(msg))
    arr = l.split(" ")
    return arr

def check(arr):
    count_symbol = 0
    count_number = 0
    print(arr)
    for i in arr:
        if not (i == '+' or i == '-' or i == '*' or i == '/' or i.isdigit()):
            raise InvalidInputError("Вы ввели недопустимое значение: {}".format(i))
        if i in ['+', '-', '*', '/']:
            count_symbol += 1
        elif i.isdigit():
            count_number += 1
    c = count_number - count_symbol
    if c > 1:
        raise InvalidInputError("Операторов больше на: {}".format(c+1))
    elif c < 1:
        raise InvalidInputError("Операторов меньше на: {}".format(c+1))

    return

def to_infix(arr):
    stack = []
    for x in reversed(arr):
        if x.isdigit():
            stack.append(x)
        elif x in ['+', '-', '*', '/']:
            operand1 = stack.pop()
            operand2 = stack.pop()
            res = f"({operand1} {x} {operand2})"
            stack.append(res)
    if len(stack) != 1:
        raise InvalidInputError("Ошибка при обработке выражения")
    return stack[0]