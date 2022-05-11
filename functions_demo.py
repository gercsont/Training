from random import randint


def is_not_negative(number):
    return number >= 0

def get_circle_area(number):
    return number ** 2 * 3.14

def get_rectangle_area(A, B):
    return A * B

def absolute(number):
    if number > 0:
        return number
    elif number < 0:
        return number * -1
    else:
        return 0

def sum_numbers(list):
    sum = 0
    for n in list:
        sum += n
    return sum


def roll_dice():
    return randint(1,6)

def count_positive_numbers(list):
    sum = 0
    for n in list:
        if n > 0:
            sum += 1
    return sum


if __name__ == "__main__":

    print(is_not_negative(10))

    print(get_circle_area(10))

    print(get_rectangle_area(200, 50))

    print(absolute(-789))
    
    list = [5, 25, 50, 150]
    print(sum_numbers(list))

    print(roll_dice())
    
    list = [1, 5, 5, -6, -8]
    print(count_positive_numbers(list))