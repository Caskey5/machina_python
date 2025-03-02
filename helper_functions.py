SLOVA = 'abcdefgh'

def koord_to_tuple(koord_slova: str) -> tuple | None:
    """
    Funkcija koja zamjenjuje klasičan zapis polja ('A1') s jednim koji će biti prikladniji
    za računanje (1, 1).

    Parameters
    ----------
    koord_slova : str
        Klasičan šahovski zapis polja
    
    Returns
    -------
    tuple | None
        Vraća tuple ako je podatak legalan, None ako nije.
    """
    slovo = koord_slova[0].lower()
    broj = koord_slova[1:]

    if slovo in SLOVA:
        koord_1 = SLOVA.index(slovo) + 1  
    else:
        return None

    if broj.isnumeric() and 1 <= int(broj) <= 8:  
        koord_2 = int(broj)
    else:
        return None

    return (koord_1, koord_2)

def tuple_to_koord(koord_tuple: tuple) -> str | None:
    """
    Funkcija koja zamjenjuje zapis polja u obliku brojeva u tupleu (1, 1) s klasičnim šahovskim
    zapisom ('A1').

    Parameters
    ----------
    koord_tuple : tuple
        Tuple zapis polja pomoću samo brojeva.
    
    Returns
    -------
    str | None
        Vraća str ako je podatak legalan, None ako nije.
    """
    koord_1, koord_2 = koord_tuple
    if 1 <= koord_1 <= 8 and 1 <= koord_2 <= 8:  
        slovo = SLOVA[koord_1 - 1].upper()
        broj = str(koord_2)
        return f"{slovo}{broj}"
    return None


