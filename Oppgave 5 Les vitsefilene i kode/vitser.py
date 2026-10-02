import json

with open("vitser1.json", encoding="utf-8") as fil:
    vitser1 = json.load(fil)
with open("vitser2.json", encoding="utf-8") as fil:
    vitser2 = json.load(fil)

countjoke_vitser1 = len(vitser1)



def fil_vitser1():
    global vitser1
    print("Velg en vits mellom 1 og 11. (0 = for å gå tilbake)")
    vits_vitser1 = input("Svar: ")
    print()
    if vits_vitser1 == '1':
        print(vitser1["1"])
    elif vits_vitser1 == '2':
        print(vitser1["2"])
    elif vits_vitser1 == '3':
        print(vitser1["3"])
    elif vits_vitser1 == '4':
        print(vitser1["4"])
    elif vits_vitser1 == '5':
        print(vitser1["5"])
    elif vits_vitser1 == '6':
        print(vitser1["6"])
    elif vits_vitser1 == '7':
        print(vitser1["7"])
    elif vits_vitser1 == '8':
        print(vitser1["8"])
    elif vits_vitser1 == '9':
        print(vitser1["9"])
    elif vits_vitser1 == '10':
        print(vitser1["10"])
    elif vits_vitser1 == '11':
        print(vitser1["11"])
    elif vits_vitser1 == '0':
        return
    else:
        print("Du skrev ikke en av de mulige svarene.")
    print()
    fil_vitser1()



def fil_vitser2():
    print("Velg en vits mellom 1 og 11. (0 = for å gå tilbake)")
    vits_vitser2 = input("Svar: ")
    print()
    if vits_vitser2 == '1':
        print(vitser2["jokes"][0]["joke"])
    elif vits_vitser2 == '2':
        print(vitser2["jokes"][1]["joke"])
    elif vits_vitser2 == '3':
        print(vitser2["jokes"][2]["joke"])
    elif vits_vitser2 == '4':
        print(vitser2["jokes"][3]["joke"])
    elif vits_vitser2 == '5':
        print(vitser2["jokes"][4]["joke"])
    elif vits_vitser2 == '6':
        print(vitser2["jokes"][5]["joke"])
    elif vits_vitser2 == '7':
        print(vitser2["jokes"][6]["joke"])
    elif vits_vitser2 == '8':
        print(vitser2["jokes"][7]["joke"])
    elif vits_vitser2 == '9':
        print(vitser2["jokes"][8]["joke"])
    elif vits_vitser2 == '10':
        print(vitser2["jokes"][9]["joke"])
    elif vits_vitser2 == '11':
        print(vitser2["jokes"][10]["joke"])
    elif vits_vitser2 == '0':
        return
    else:
        print("Du skrev ikke en av de mulige svarene.")
    print()
    fil_vitser2()


# START
while True:
    print()
    print("Hvilken av vitser .json filene vil du sjekke?")
    print("[1 = vitser1.json]")
    print("[2 = vitser2.json]")
    sjekke_fil = input("Svar: ")
    print()
    
    if sjekke_fil == '1':
        fil_vitser1()
    elif sjekke_fil == '2':
        fil_vitser2()
    else:
        print("Du skrev ikke en av de mulige svarene.")
        continue