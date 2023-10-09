import sys
from prefix import check, to_infix

print("\n\n  Добро пожаловать, здесь вы можете перевести входную строку \
префиксной нотации в инфиксную запись. \
\n\tВы можете вводить только бинарные операторы: +  -  *  / \n \
\tВ качестве операндов беззнаковые числа. Разделитель - пробел\n\n")

input_str = str(input("Введите строку: ")).split(" ")
print(input_str)

try:
    check(input_str)
except ValueError as e:
    print(e)
    sys.exit()

res = to_infix(input_str)

print("Result: ", res)