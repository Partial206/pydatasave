import pyautogui as pyauto
import json

def load_data():
    try:
        with open("veriler.json", "r") as json_file:
            return json.load(json_file)
    except (FileNotFoundError, json.decoder.JSONDecodeError):
        return []

def save_data(data):
    with open("veriler.json", "w") as json_file:
        json.dump(data, json_file, indent=2)

while True:
    try:
        a = int(pyauto.prompt(text="1-Veri Kaydet \n2-Veri Sil \n3-Verileri Göster", title='Seçenekler', default='Bir sayı seç!'))
    except ValueError:
        pyauto.alert(text="Value Error, Çıkış yapıldı", title="Uyarı")
        exit()

    if a == 3:
        data = load_data()
        pyauto.alert(text=json.dumps(data, indent=2), title="Uyarı")
    elif a == 1:
        data = load_data()
        text = str(pyauto.prompt(text="Kaydedilecek bir veri yaz", title='Seçenekler', default='Yaz...'))
        if text not in data:
            data.append(text)
            save_data(data)
            pyauto.alert(text="Veri Kaydedildi", title="Uyarı")
        else:
            pyauto.alert(text="Veri Kaydedilemedi, Çıkış yapıldı", title="Uyarı")
    elif a == 2:
        data = load_data()
        text_to_delete = str(pyauto.prompt(text="Silinicek veriyi yaz", title='Seçenekler', default='Yaz...'))
        data = [item for item in data if item != text_to_delete]
        save_data(data)
        pyauto.alert(text="Veri Silindi", title="Uyarı")
    else:
        pyauto.alert(text="Geçersiz seçenek, Çıkış yapıldı", title="Uyarı")
        exit()
