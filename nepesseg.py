nepesseg = []

with open("lakossag_2025.csv", "r", encoding="UTF-8") as forrasfajl:
    forrasfajl.readline()

    for sor in forrasfajl:
        adatok = sor.strip().split(';')

        n = {
            "megye": adatok[0],
            "telepules": adatok[1],
            "tipus": adatok[2],
            "ferfi": adatok[3],
            "no": adatok[4]
        }

        nepesseg.append(n)


telepules = int(input(
    "[1] Nyomja meg az 1-es gombot a megye adatai lekéréséhez\n"
    "[2] Nyomja meg a 2-es gombot a település típusainak lekéréséhez: "
))

telepulesek_szama = 0

if telepules == 1:
    bekert_megye = input("Adjon meg egy megyét (PL: HAJ): ")

    for i in nepesseg:
        if i["megye"] == bekert_megye:
            telepulesek_szama += 1

print(telepulesek_szama)
