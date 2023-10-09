import pytest
from prefix import check, to_infix

@pytest.mark.parametrize("arr", [
    ["+", "1", "2"],
    ["-", "*", "1", "4", "70"],
])
def test_check_valid_input(arr):
    check(arr)

@pytest.mark.parametrize("arr", [
    ["-"],
    ["*", "6", "b"],
    ["&", "/", "c"],
    ["-", "4", "1", "5"],
    ["-", "-", "1", "2"],
])
def test_check_invalid_input(arr):
    with pytest.raises(ValueError):
        check(arr)

@pytest.mark.parametrize("arr, expected", [
    (["+", "-", "13", "4", "55"], "((13 - 4) + 55)"),
    (["+", "2", "*", "2", "-", "2", "1"], "(2 + (2 * (2 - 1)))"),
    (["+", "+", "10", "20", "30"], "((10 + 20) + 30)"),
    (["/", "+", "3", "10", "*", "+", "2", "3", "-", "3", "5"], "((3 + 10) / ((2 + 3) * (3 - 5)))"),
])
def test_to_infix(arr, expected):
    assert to_infix(arr) == expected