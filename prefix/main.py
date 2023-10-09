import sys
from prefix import InvalidInputError, input_string, check, to_infix


print("\n\n  Добро пожаловать, здесь вы можете перевести входную строку \
префиксной нотации в инфиксную запись. \
\n\tВы можете вводить только бинарные операторы: +  -  *  / \n \
\tВ качестве операндов беззнаковые числа. Разделитель - пробел\n\n")

input_str = input_string("Введите строку: ")

try:
    check(input_str)
except InvalidInputError as e:
    print(e)
    sys.exit()

res = to_infix(input_str)

print("Result: ", res)