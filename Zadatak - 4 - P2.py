#DZ - Zadatak 2: Napiši program koji će učitati datum rođenja u bilo kojem obliku koji vam padne na pamet (jedan string)
#i onda vratiti koji je dan bio na taj datum.




import datetime as dt 

datum_unos = input("Unesite dan, mjesec i godinu rođenja u formatu DD-MM-YYYY: ")


datum_rođenja = dt.datetime.strptime(datum_unos, "%d-%m-%Y")


dan_string = datum_rođenja.strftime('%A')

print("Rođeni ste na " , dan_string , "!")
