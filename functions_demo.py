from random import randint


def is_not_negative(number):
    return number >= 0
print(is_not_negative(-10))

if __name__ == "__main__":
    
print ("""
VÉGE
""")

def get_circle_area(number):
    return number ** 2 * 3.14
print(get_circle_area(2))

print ("""
VÉGE
""")

def get_rectangle_area(A, B):
    return A * B
print(get_rectangle_area(5, 4))

print ("""
VÉGE
""")

def absolute(number):
    if number > 0:
        return number
    elif number < 0:
        return number * -1
    else:
        return 0
print(absolute(-564))

print ("""
VÉGE
""")

def sum_numbers(list):
    sum = 0
    for n in list:
        sum += n
    return sum
list = [1, 2, 3, -4, -5, 6, 7, 8, 9]
print(sum_numbers(list))

print ("""
VÉGE
""")

def roll_dice():
    return randint(1,6)
print(roll_dice())

print ("""
VÉGE
""")

def count_positive_numbers(list):
    sum = 0
    for n in list:
        if n > 0:
            sum += 1
    return sum
list = [-1, -2, -3, 4, 5, -6, -7, 8, -9]
print(count_positive_numbers(list))
