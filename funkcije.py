def je_li_paran(broj):
    if broj % 2 == 0:
        return True
    else:
        return False
    
je_li_paran(2)

# from funkcije import je_li_paran

# unos = int(input("Unesi broj: "))

# if je_li_paran(unos):  # Ako funkcija vrati True
#     print("Broj je paran")
# else:
#     print("Broj je neparan")
 


def input_int(prompt='unesi cijeli broj'):
    while True:
        broj = input(prompt)
        if broj.isnumeric():
            broj = int(broj)
            break
    return broj

def kvadrat(broj):
    return broj ** 2  # Vraća broj na kvadrat

# Pozivanje funkcije
print(kvadrat(4))  # Output: 16
print(kvadrat(7))  # Output: 49
