import random
import time

print("Akıldan sayı tutma oyununa hoşgeldiniz\nAma önce Oyuna kayıt olmanız gerek.")
time.sleep(3)

name = input("İsminizi giriniz : ")

print(f"Hoşgeldin {name} Oyun başlatılıyor Lütfen bekle!")
time.sleep(3)

sayi = random.randint(1,100)
tahmin_hakki = 10

while True:
    tahmin = int(input("Tahmin Ettiğiniz Sayıyı giriniz : "))

    if tahmin == sayi:
        print("Sayınız Kontrol Ediliyor...")
        time.sleep(3)
        print(f"Tebrikler {name}! Oyunu Kazandın")
        break
    
    elif tahmin > sayi:
        print("Sayınız sorgulanıyor Lütfen Bekle!")
        time.sleep(3)
        tahmin_hakki -= 1
        print(f"Daha küçük bir sayı gir {name}.")
        print(f"Kalan hakkın : {tahmin_hakki}")

    else:
        print("Sayınız sorgulanıyor Lütfen Bekle!")
        time.sleep(3)
        tahmin_hakki -= 1
        print(f"Daha büyük bir sayı gir {name}.")
        print(f"Kalan hakkın : {tahmin_hakki}")
    if tahmin_hakki == 0:
        print(f"Tahmin hakkın bitti {name}")
        print(f"Bulunacak sayı : {sayi}")
        break