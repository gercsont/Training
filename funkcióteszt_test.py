from functions_demo import is_not_negative, absolute


def test_with_negative_number():
    number = -10
    result = is_not_negative(number)
    assert result == False

def test_with_positive_number():
    number = 10
    result = is_not_negative(number)
    assert result == True

def test_with_zero():
    number = 0
    result = is_not_negative(number)
    assert result == True

def test_absolute_with_positive():
    number = 5
    result = absolute(number)
    assert result == 5

def test_absolute_with_negative():
    number = -5
    result = absolute(number)
    assert result == 5