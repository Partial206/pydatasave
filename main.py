import time as t
import pyautogui as pyauto

while True:
    print(
    "1-Veri Kaydet \n"
    "2-Veri Sil \n"
    "3-Verileri göster"
    )
    a = int(input("Bir Seçenecek Seç : "))

    if a == 3:
     file = open("veriler.txt", "r")
     print(file.read())
     file.close()
    elif a == 1:
     text = str(input("Kaydedilecek bir veri yaz : "))
     file = open("veriler.txt","a")
     file.write(text + "\n")
     print(text, "Yazıldı")
     file.close()
    elif a == 2: 
      pass 
