from random import randint, random 
number = randint(1, 100)
success = False
print("""
Gondoltam egy számot.""")
while not success:
    guess = int(input("""
    Mi a tipped? """))
    if guess > number:
        print("""
        A gondolt szám ennél kisebb.""")
    elif guess < number:
        print("""
        A gondolt szám ennél nagyobb.""")
    else:
        success = True
        print("""
        Eltaláltad!
        """)