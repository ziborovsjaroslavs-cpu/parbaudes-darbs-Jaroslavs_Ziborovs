skaits = {}

with open("sistema.log", encoding="utf-8") as f:
    for rinda in f:
        limenis = rinda.split()[2]
        skaits[limenis] = skaits.get(limenis, 0) + 1

print("Limenu kopsavilkumss")
for limenis in sorted(skaits, key=skaits.get, reverse=True):
    print(limenis, skaits[limenis])
