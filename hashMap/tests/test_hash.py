import pytest
from hashmap.specialdict import SpecialDict
from hashmap.iloc import IlocException
from hashmap.ploc import PlocException, Ploc

@pytest.fixture()
def specialdict_iloc():
    map = SpecialDict()
    map["value1"] = 1
    map["value2"] = 2
    map["value3"] = 3
    map["1"] = 10
    map["2"] = 20
    map["3"] = 30
    map["1, 5"] = 100
    map["5, 5"] = 200
    map["10, 5"] = 300
    return map

@pytest.fixture()
def specialdict_ploc():
    map = SpecialDict()
    map["value1"] = 1
    map["value2"] = 2
    map["value3"] = 3
    map["1"] = 10
    map["2"] = 20
    map["3"] = 30
    map["(1, 5)"] = 100
    map["(5, 5)"] = 200
    map["(10, 5)"] = 300
    map["(1, 5, 3)"] = 400
    map["(5, 5, 4)"] = 500
    map["(10, 5, 5)"] = 600
    return map

class TestSpecialDict:

    def test_iloc_positive_cases(self, specialdict_iloc):
        assert specialdict_iloc.iloc[0] == 10
        assert specialdict_iloc.iloc[2] == 300
        assert specialdict_iloc.iloc[5] == 200
        assert specialdict_iloc.iloc[8] == 3

    def test_iloc_exception(self, specialdict_iloc):
        with pytest.raises(IlocException):
            specialdict_iloc.iloc[10]
    
    def test_ploc_exception(self, specialdict_ploc):
        with pytest.raises(PlocException):
            specialdict_ploc.ploc[">=10, d"]

    def test_ploc_invalid_condition(self, specialdict_ploc):
        with pytest.raises(PlocException):
            specialdict_ploc.ploc[11]

    def test_ploc_bad_condition(self, specialdict_ploc):
        with pytest.raises(PlocException):
            specialdict_ploc.ploc["<5, =>b, =1"]

    def test_ploc_positive_cases(self, specialdict_ploc):
        assert specialdict_ploc.ploc[">=1"] == "{1 = 10, 2 = 20, 3 = 30}"
        assert specialdict_ploc.ploc["<3"] == "{1 = 10, 2 = 20}"
        assert specialdict_ploc.ploc[">0, >0"] == "{(1, 5) = 100, (5, 5) = 200, (10, 5) = 300}"
        assert specialdict_ploc.ploc[">=10, >0"] == "{(10, 5) = 300}"
        assert specialdict_ploc.ploc["<5, >=5, >=3"] == "{(1, 5, 3) = 400}"

    def test_check_valid(self):
        assert Ploc.check_condition("=", "123")
        assert Ploc.check_condition("<", "456")
        assert Ploc.check_condition(">", "789")
        assert Ploc.check_condition("<=", "10")

    def test_ploc_condition_value_not_digit(self, specialdict_ploc):
        with pytest.raises(PlocException):
            specialdict_ploc.ploc["<=5, abc"]

    def test_ploc_condition_invalid_operator(self, specialdict_ploc):
        with pytest.raises(PlocException):
            specialdict_ploc.ploc["<5, ><, =1"]

    def test_ploc_condition_invalid_separator(self, specialdict_ploc):
        with pytest.raises(PlocException):
            specialdict_ploc.ploc["<5, >=b, =1"]

    def test_ploc_condition_valid_negative(self, specialdict_ploc):
        assert specialdict_ploc.ploc["<0"] == "{}"
    
    def test_ploc_condition_invalid(self, specialdict_ploc):
        with pytest.raises(PlocException):
            specialdict_ploc.ploc["<=invalid_condition"]