# lista pitanja
# spremi odgovore
# odaberi "random" pitanja
# pitaj pitanje
# pregledaj jel točno
# prati rezultat (score)
# reci korisniku njegov rezultat (score)

import random

pitanja = {
    "Koja je ključna riječ za definiciju u Python-u?": "def",
    "Sta moramo staviti ako želimo odgovor u formatu True or False?": "bool",
    "Koji simbol je potrebno staviti da bi napravili komentar u Pythonu-u?": "#",
    "Sa kojom funkcijom postavljamo pitanje korisniku,a korisnik unosi odgovor na isto?": "input",
    "Koji je odgovor za 3 ** 8 u Python-u?": "8",
    "Koji je rezultat za 10 // 3 u Python-u?": "3",
    "Sa čime dajemo do znanja monitoru da nešto ispiše?": "print" 
}

def python_igra_pogađanja():
    pitanja_lista = list(pitanja.keys())
    sva_pitanja = 5
    rezultat = 0

    odabrana_pitanja = random.sample(pitanja_lista, sva_pitanja)

    # ["a", "b", "c"]
    #   0    1    2
    for index, pitanje in enumerate(odabrana_pitanja):
        print(f"{index + 1}. {pitanje}")
        odgovor_korisnika = input("Tvoj odgovor: ").lower().strip() #.lower() -> sve u mala slova, #.strip() -> miče razmake

        točan_odgovor = pitanja[pitanje]
        if odgovor_korisnika == točan_odgovor.lower():
            print("Točan odgovor!\n")
            rezultat += 1
        else:
            print(f"Netočan odgovor. Točan odgovor je: {točan_odgovor}.\n")

    print(f"Igra gotova! Tvoj prosjek točnih odgovora je: {rezultat}/{sva_pitanja}. ")