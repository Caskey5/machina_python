#DZ - Zadatak 2: Napiši program koji će učitati datum rođenja u bilo kojem obliku koji vam padne na pamet (jedan string)
#i onda vratiti koji je dan bio na taj datum.




from datetime import datetime

dan,mjesec,godina = int(input("Unesite dan, mjesec i godinu rođenja: "))


datum_rođenja = datetime(dan,mjesec,godina)


dan_str = datum_rođenja.strftime('%A')

print("Rođeni ste na " , dan_str , "!")
