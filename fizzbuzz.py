for szam in range(1, 1001):
    if szam % 15 == 0:
        print("FIZZ-BUZZ")
    elif szam % 5 == 0:
        print("BUZZ")
    elif szam % 3 == 0:
        print("FIZZ")
    else:
        print(szam)
print("END")