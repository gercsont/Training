should_input = True
while should_input:
    number = int(input("Adj meg egy egész számot: "))
    if not number == 0:
        print("A te számod:", number)
    else:
        should_input = False
print("Itt a vége!")