
# 1. **Hallo Welt ausgeben:**
   
print("Hallo Welt")

# 2. **Benutzereingabe:**

name = input("Gib deinen Namen ein: ")
print("Hallo, " + name + "!")

# 3. **Zahlen addieren:**

num1 = float(input("Gib die erste Zahl ein: "))
num2 = float(input("Gib die zweite Zahl ein: "))
summe = num1 + num2
print("Die Summe ist:", summe)

# 4. **Quadratzahlen:**

zahl = float(input("Gib eine Zahl ein: "))
quadrat = zahl ** 2
print("Das Quadrat der Zahl ist:", quadrat)

# 5. **Bedingungen:**

alter = int(input("Gib dein Alter ein: "))
if alter >= 18:
    print("Du bist volljährig.")
else:
    print("Du bist minderjährig.")

# 6. **Schleifen:**
# xs = [1,2,3,4,5,...]
# range is its own data type and can be casted to a list with a list() function
for zahl in list(range(1, 11)):
    print(zahl)

# 7. **Listen:**

tiere = ["Hund", "Katze", "Maus", "Elefant", "Löwe"]
for tier in tiere:
    print(tier)

# 8. **Schleifen und Listen:**

zahlen = [5, 8, 12, 3, 7]
summe = 0
for zahl in zahlen:
    summe += zahl
print("Die Summe der Zahlen ist:", summe)

# 9. **Funktionen:**

def addiere(zahl1, zahl2):
    return zahl1 + zahl2

zahl1 = float(input("Gib die erste Zahl ein: "))
zahl2 = float(input("Gib die zweite Zahl ein: "))
ergebnis = addiere(zahl1, zahl2)
print("Die Summe ist:", ergebnis)

# 10. **Schreiben in eine Datei:**

name = input("Gib deinen Namen ein: ")
with open("name.txt", "w") as datei:
    datei.write(name)