names = ["Gergő", "Kinga", "Karsa", "Helka", "Hajna"]
line = ""
for name in names:
    line += name + ", "
print(line)
print("END")

names = ["Gergő", "Kinga", "Karsa", "Helka", "Hajna"]
line = ""
for name in names:
    if line == "":
        line += name
    else:
        line = line +", " + name
print(line)
print("END")

names = ["Gergő", "Kinga", "Karsa", "Helka", "Hajna"]
line = ""
i = 0
for name in names:
    i += 1
    if i != 1:
        line += ", "
    line += name
print(line)
print("END")