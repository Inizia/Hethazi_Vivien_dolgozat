def beker():
    beker = int(input("Adj meg egy páros számot!:"))
    i = 0
    while beker % 2 != 0:
       beker = int(input(f"Ez nem páros! Páros számot kérek!"))

    szam = int(input("Kérem az 1. páros számot!: "))
    while szam % 2 != 0:
        szam = int(input(f"Ez nem páros! Kérem a 1. páros számot!"))


    szam2 = int(input(f"Kérem a 2. páros számot!"))
    while szam2 % 2 != 0:
        szam2 = int(input(f"Ez nem páros! Kérem a 2. páros számot!"))

    szam3 = int(input(f"Ez nem páros! Kérem a 3. páros számot!"))
    while szam3 % 2 != 0:
        szam3 = int(input(f"Ez nem páros! Kérem a 3. páros számot!"))


    bekert_szamok = []
    i = 0
    bekert_szamok.append(szam)
    bekert_szamok.append(szam2)
    bekert_szamok.append(szam3)



import random
def szandomszamok():
    i = 1
    randomlista = []
    while (i < 13):
        vel = int(random.random() * 190) - 40
        randomlista.append(vel)
        i += 1
    print(randomlista)
