import json

with open("vitser1.json", encoding="utf-8") as fil:
    vitser1 = json.load(fil)
with open("vitser2.json", encoding="utf-8") as fil:
    vitser2 = json.load(fil)

countjoke_vitser1 = len(vitser1)

print()
print("Vitser1:")
print(vitser1["1"])
print()
print(vitser1["11"])
print()
print(f"Det er {countjoke_vitser1} vitser i vitser1.json.")
print()
print("Strukturen i vitser1.json er at hele filen består av bare ett objekt med de 11 vitsene inni seg. Filen innholderingen ingen lister.")



print()
print("Vitser2:")
print(vitser2["jokes"][0]["joke"])
print()
print(vitser2["jokes"][10]["joke"])
print()
print("Det er 11 vitser i vitser2.json.")
print()
print("")
# Etter å kommet til hit på denne oppgaven, (nr. 4) så fant jeg ut at vi ikke skulle gjøre noe her. Bare utforske å lære selv. Jeg spurte en lærer.


print()