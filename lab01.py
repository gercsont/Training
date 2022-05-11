# Írd ki egymás után 5x a neved!
for i in range(5):
    print("Gergő")
print("end")

# Írd ki egymás utána a neved 5x, de írj elé sorszámot is. Pl.:
for i in range(5):
    print(i, ". Gergő", sep="")
    print(str(i) +". Gergő")
print("end")

# Írd ki egymás utána a neved 5x, írj elé sorszámot is, de egytől. 
for i in range(5):
    print(i+1, ". Gergő", sep="")
print("end")

# Írd ki az első 10 pozitív egész számot, és mellé annak négyzetét!
i = 1
while i < 11:
    print(i, "négyzete", i ** 2)
    i = i + 1
print("end")

# Hónapok! Írd ki az első 6 hónapra:
hónapok = ["január", "február", "március", "április", "május", "június"]
számoló = 1
for hónap in hónapok:
    print("Az év ", i, ". hónapja ", hónap)
print("end")
# Az év 1. hónapja január.

numbers = [1, -2, 3, -4, 5, -6, 7, -8, 9, -10]
sum = 0
for number in numbers:
    if number > 0:
        sum += number
print(sum)
print("end")

numbers = [1, -2, 3, -4, 5, -6, 7, -8, 9, -10]
sum = 0
for number in numbers:
    if number > 0:
        sum += number
    elif number < 0:
        sum += number * -1
print(sum)

print("end")