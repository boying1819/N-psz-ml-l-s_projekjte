nepesseg = []
adott_megyek = []
telepulesek_szama = 0
osszlakosok = 0
ossz_varos_lakok = 0

with open("lakossag_2025.csv", "r", encoding="UTF-8") as forrasfajl:
    forrasfajl.readline()

    for sor in forrasfajl:
        adatok = sor.strip().split(';')

        n = {
            "megye": adatok[0],
            "telepules": adatok[1],
            "tipus": adatok[2],
            "ferfi": int(adatok[3].replace(" ", "")),
            "no": int(adatok[4].replace(" ", ""))
        }

        nepesseg.append(n)

while True:
    telepules = input(
        "[1] Megye adatai\n"
        "[2] Település típusok\n"
        "[X] Kilépés\n"
        "\nVálasztás: "
    ).lower()

    if telepules == "1":
        bekert_megye = input("Adjon meg egy megyét (PL: HAJ): ").upper()
        for i in nepesseg:
            if i["megye"] == bekert_megye:
                telepulesek_szama += 1
                adott_megyek.append(i)
        for i in adott_megyek:
            x = int(i["ferfi"]) + int(i["no"])
            osszlakosok += x
            if i["tipus"] == "város":
                x = int(i["ferfi"]) + int(i["no"])
                ossz_varos_lakok += x

        print(f"Ebben a megyében {telepulesek_szama} település található.")
        print(f"{osszlakosok} lakik itt.")
        print(f"{ossz_varos_lakok} ember lakik ebből városokban.")

    elif telepules == "2":
        tipusok = []
        for i in nepesseg:
            if i["tipus"] not in tipusok:
                tipusok.append(i["tipus"])

        print("\nTelepüléstípusok:")

        for sorszam, tipus in enumerate(tipusok, 1):
            print(f"[{sorszam}] {tipus}")

        valasztas = int(input("\nVálasszon egy településtípust: "))
        bekert_tipus = tipusok[valasztas - 1]
        kozseg_tipusok = []

        for i in nepesseg:
            if i["tipus"] == bekert_tipus:
                kozseg_tipusok.append(i)

        oldal = 0
        oldal_meret = 10

        while True:
            kezdet = oldal * oldal_meret
            veg = kezdet + oldal_meret

            print("\nTelepülések:")

            for i in kozseg_tipusok[kezdet:veg]:
                lakossag = i["ferfi"] + i["no"]
                print(f'{i["telepules"]} - {lakossag} fő')


            print(f"\nOldal: {oldal + 1} / {(len(kozseg_tipusok) + oldal_meret - 1) // oldal_meret}")

            print("\n[N] Következő oldal")
            print("[B] Előző oldal")
            print("[Q] Vissza a főmenübe")

            valasztas = input("Választás: ").lower()


            if valasztas == "n".lower():
                if veg < len(kozseg_tipusok):
                    oldal += 1
                else:
                    print("Ez az utolsó oldal!")

            elif valasztas == "b".lower():
                if oldal > 0:
                    oldal -= 1
                else:
                    print("Ez az első oldal!")

            elif valasztas == "q".lower():
                break      

    elif telepules == "x".lower():
        print("A program vége!")
        break              
