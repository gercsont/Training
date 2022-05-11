menu = (input("""Válassz, hogy mit szeretnél csinálni:
(1) összeadni
(2) kivonni
Választásod: """))
if menu == 1:
    sum = 0
    number = int(input("Add meg az első számot: "))
    sum += number
    number = int(input("Add meg a második számot: "))
    sum += number
    print("Az számaid összege: ", sum)
elif menu == 2:
    sum = 0
    number = int(input("Add meg az első számot: "))
    sum += number
    number = int(input("Add meg a második számot: "))
    sum -= number
    print("Az számaid különbsége: ", sum)
else:
    print("Ismeretlen művelet")
print("Itt a vége!")