def anahtar_dogrula(anahtar):
    anahtar = anahtar.lower()
    if len(anahtar) != 26:
        return "HATA: Anahtar 26 karakter içermelidir."
    if not anahtar.isalpha():
        return "HATA: Anahtar sadece alfabetik karakterler içermelidir."
    if len(set(anahtar)) != 26:
        return "HATA: Anahtar tekrar eden karakterler içermemelidir."
    return None


def yedekleme_sozluk_olustur(anahtar, cozme=False):
    alfabe = 'abcdefghijklmnopqrstuvwxyz'
    yedekleme_sozlugu = {}

    if cozme:
        for a, k in zip(alfabe, anahtar):
            yedekleme_sozlugu[k] = a
    else:
        for a, k in zip(alfabe, anahtar):
            yedekleme_sozlugu[a] = k

    return yedekleme_sozlugu


def mesaj_yedekle(mesaj, yedekleme_sozlugu):
    sonuc = []
    for karakter in mesaj:
        if karakter.isalpha():
            if karakter.islower() and karakter in yedekleme_sozlugu:
                sonuc.append(yedekleme_sozlugu[karakter])
            elif karakter.upper() in yedekleme_sozlugu:
                sonuc.append(yedekleme_sozlugu[karakter.upper()].lower())
            else:
                sonuc.append(karakter)
        else:
            sonuc.append(karakter)
    return ''.join(sonuc)


def ana_menu():
    anahtar = None

    print("============================")
    print("||                        ||")
    print("||  ŞİFRELEME MAKİNESİ    ||")
    print("||       sürüm 1.0        ||")
    print("||                        ||")
    print("============================")

    while True:
        print("****** ANA MENÜ ******")
        print("[1] Anahtar gir")
        print("[2] Mesaj şifrele")
        print("[3] Mesaj çöz")
        print("[4] Çık")
        secim = input("Seçiminizi girin: ").strip()

        if secim == '1':
            anahtar = input("Lütfen anahtarı girin: ").strip()
            hata = anahtar_dogrula(anahtar)
            if hata:
                print(hata)
                anahtar = None
            else:
                print("Anahtar kabul edildi.")

        elif secim == '2':
            if anahtar is None:
                print("HATA: Lütfen önce anahtarı girin.")
            else:
                duz_metin = input("Bir düz metin girin (maksimum 100 karakter): ").strip()
                yedekleme_sozlugu = yedekleme_sozluk_olustur(anahtar)
                sifreli_metin = mesaj_yedekle(duz_metin, yedekleme_sozlugu)
                print(f"Şifreli metin: {sifreli_metin}")

        elif secim == '3':
            if anahtar is None:
                print("HATA: Lütfen önce anahtarı girin.")
            else:
                sifreli_metin = input("Bir şifreli metin girin (maksimum 100 karakter): ").strip()
                yedekleme_sozlugu = yedekleme_sozluk_olustur(anahtar, cozme=True)
                duz_metin = mesaj_yedekle(sifreli_metin, yedekleme_sozlugu)
                print(f"Düz metin: {duz_metin}")

        elif secim == '4':
            print("Programdan çıkılıyor..")
            break

        else:
            print("Geçersiz seçim. Lütfen 1, 2, 3 veya 4 girin.")


if __name__ == "__main__":
    ana_menu()
