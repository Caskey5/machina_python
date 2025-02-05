# 8 - 11:30 ili 14:30 do 18:00

vrijeme = input("Unesi vrijeme u obliku HH:MM")
sati, minute = vrijeme.split(':')

sati = int(sati)
minute = int(minute)

if (8 <= sati < 11) or (sati == 11 and minute <= 30) or (sati == 14 and minute > 30) or (15 <= sati < 18):
    print('Radi!')
else:
    print('Ne radi!')