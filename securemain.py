import pyautogui as pyauto

password = "topsecret123"

a = str(pyauto.prompt(text="Şifreyi gir", title='Güvenlik', default='...'))

if a == password:
    while True:
     try:
         a = int(pyauto.prompt(text="1-Veri Kaydet \n""2-Veri Sil \n""3-Verileri göster", title='Seçenekler', default='Bir sayı seç!'))
     except TypeError:
          exit()
     except ValueError:
          pyauto.alert(text="Value Error, Kod 4 ile çıkış yapıldı", title="Uyarı")
          exit()


     if a == 3:
        file = open("veriler.txt", "r")
        pyauto.alert(text=file.read(), title="Uyarı")
        file.close()
     elif a == 1:
        file_path = "veriler.txt"
        text = str(pyauto.prompt(text="Kaydedilecek bir veri yaz", title='Seçenekler', default='Yaz...'))
        with open(file_path, "r") as file:
            lines = file.readlines()

        if text + "\n" not in lines:
            with open(file_path, "a") as file:
                file.write(text + "\n")
                pyauto.alert(text="Veri Kaydedildi", title="Uyarı")
        else:
            pyauto.alert(text="Veri Kaydedilemedi, Kod 1 ile çıkış yapıldı", title="Uyarı")
     elif a == 2:
        file_path = "veriler.txt"
        text_to_delete = str(pyauto.prompt(text="Silinicek veriyi yaz", title='Seçenekler', default='Yaz...'))
        
        with open(file_path, "r") as file:
            lines = file.readlines()

        with open(file_path, "w") as file:
            for line in lines:
                if line.strip() != text_to_delete:
                    file.write(line)
     else:
        pyauto.alert(text="Error, Kod 3 ile çıkış yapıldı", title="Uyarı")
else:
    pyauto.alert(text="Şifre yanlış!", title="Uyarı")
