import pyautogui as pyauto

while True:
    a = int(pyauto.prompt(text="1-Veri Kaydet \n""2-Veri Sil \n""3-Verileri göster", title='Seçenekler', default='Bir sayı seç!'))
    
    if a == 3:
        file = open("veriler.txt", "r")
        pyauto.alert(text=file.read(), title="Uyarı")
        file.close()
    elif a == 1:
        text = str(pyauto.prompt(text="Kaydedilecek bir veri yaz", title='Seçenekler', default='Yaz...'))
        file = open("veriler.txt", "a")
        file.write(text + "\n")
        file.close()
        pyauto.alert(text="Veri Kaydedildi", title="Uyarı")
    elif a == 2: 
        pass
