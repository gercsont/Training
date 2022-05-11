should_input = True
sum = 0
while should_input:
    number = int(input("Adj meg egy egész számot: "))
    if not number == 0:
        print("A te számod:", number)
        sum += number
    else:
        should_input = False
        print("Az eddigi számaid összege: ", sum)
print("Itt a vége!")