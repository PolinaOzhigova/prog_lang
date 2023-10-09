import pytest
from prefix import InvalidInputError, input_string, check, to_infix

# Тестовый случай для проверки ввода
@pytest.mark.parametrize("input_str, expected", [
    ("+ 3 5", ["+", "3", "5"]),
    ("", []),
    ("invalid input", ["invalid", "input"]),
])
def test_input_string(input_str, expected):
    assert input_string(input_str) == expected

# Тестовый случай для функции check
@pytest.mark.parametrize("arr", [
    ["+", "3", "5"],
    ["-"],
    ["*", "2", "a"],
])
def test_check_valid_input(arr):
    check(arr)

@pytest.mark.parametrize("arr", [
    ["3", "5"],  # Операторов больше на 1
    ["+", "-", "3", "5"],  # Операторов меньше на 1
    ["*", "2", "a", "+"],  # Недопустимое значение "a"
])
def test_check_invalid_input(arr):
    with pytest.raises(InvalidInputError):
        check(arr)

# Тестовый случай для функции to_infix
@pytest.mark.parametrize("arr, expected", [
    (["+", "3", "5"], "(3 + 5)"),
    (["*", "2", "-", "1", "3"], "((2 * 1) - 3)"),
])
def test_to_infix(arr, expected):
    assert to_infix(arr) == expected