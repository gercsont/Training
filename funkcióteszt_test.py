from functions_demo import is_not_negative


def test_with_negative_number():
    number = -10
    result = is_not_negative(number)
    assert result == False