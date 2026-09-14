nepesseg = []

with open("lakossag_2025.csv", "r", encoding="UTF-8") as forrasfajl:
    forrasfajl.readline()

    for sor in forrasfajl:
        adatok = sor.strip().split(';')

        n = {
            "megye": adatok[0],
            "telepules": adatok[1],
            "tipus": adatok[2],
            "ferfi": adatok[3].replace(" ", ""),
            "no": adatok[4].replace(" ", "")
        }

        nepesseg.append(n)


telepules = int(input(
    "[1] Nyomja meg az 1-es gombot a megye adatai lekéréséhez\n"
    "[2] Nyomja meg a 2-es gombot a település típusainak lekéréséhez: "
))

telepulesek_szama = 0
adott_megyek = []
osszlakosok = 0
ossz_varos_lakok = 0

if telepules == 1:
    bekert_megye = input("Adjon meg egy megyét (PL: HAJ): ")

    for i in nepesseg:
        if i["megye"].lower() == bekert_megye.lower():
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