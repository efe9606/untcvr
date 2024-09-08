import time

def sayac():

 sure = int(input("Lütfen süre giriniz: "))
 for x in range(sure, 0, -1):
  
  saniye = x % 60
  dakika = int(x / 60) % 60
  saat = int(x / 3600) 
  
  print(f"{saat:02}.{dakika:02}.{saniye:02}")
  time.sleep(1)
  
 print("SÜRE DOLDU")

print(sayac())
