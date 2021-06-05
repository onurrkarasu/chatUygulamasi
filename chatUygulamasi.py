import kullanici_islemleri
from datetime import date


def kisiselMenu(kullanici_adi):
    while kullanici_islemleri.cevrimici_kullanici:
        print("""
                [1]  Arkadaş Listemi Getir
                [2]  Arkadaş Ekle
                [3]  Direkt Mesaj Gönder
                [4]  Mesaj Kutusu
                [5]  Çıkış        
              """)
        secim=int(input("Seçiminizi girin : "))
        if secim==1:
            arkadasListesi(kullanici_adi)
        elif secim==2:
            arkadas=input("Eklemek istediğiniz arkadaşınızın kullanıcı adını girin : ")
            arkadasEkle(ben=kullanici_adi,arkadas=arkadas)
        elif secim==3:
            arkadas=input("Mesajın gönderileceği arkadaşınızın kullanıcı adını yazın : ")
            mesaj=input("Mesajınızı yazın : ")
            mesajGonder(ben=kullanici_adi,arkadas=arkadas,mesaj=mesaj,tarih=date.today())
        elif secim==4:
            mesajKutusu(kullanici_adi)
        elif secim==5:
            print("Çıkış yapılıyor...")
            kullanici_islemleri.cevrimici_kullanici=False
            input("Kayıt menüsüne dönmek için bir tuşa basın")


def mesajKutusu(kulllanici_adi):
    try:
        mesajVar=False
        dosya=open("mesajlar.txt","r")
        satirlar=dosya.readlines()
        for mesaj in satirlar:
            bolunmus=mesaj.split("||")
            gonderen=bolunmus[0]
            alici=bolunmus[1]
            mesaj=bolunmus[2]
            tarih=bolunmus[3]
            if kulllanici_adi== gonderen or kulllanici_adi==alici:
                print("""
                        Gönderen: {gonderici}   Alıcı:  {alici}   
                        Tarih:  {gonderim_tarihi}
                        Mesaj:  {mesaj}
                    """.format(gonderici=gonderen,alici=alici,gonderim_tarihi=tarih,mesaj=mesaj))
                mesajVar=True
                print("="*100)
        if not mesajVar:
            print("Mesaj Kutunuz Boş")
    except FileNotFoundError:
        print("Hiç mesajınız yok üzülmeyin kimsenin mesajı yok zaten mesajlar dosyası bile yok.")
    input("Devam etmek için bir tuşa basın.")


def mesajGonder(**kwargs):
    dosya=open("mesajlar.txt","a")
    dosya.write(kwargs["ben"].lower())
    dosya.write("||")
    dosya.write(kwargs["arkadas"].lower())
    dosya.write("||")
    dosya.write(kwargs["mesaj"])
    dosya.write("||")
    dosya.write(str(kwargs["tarih"]))
    dosya.write("\n")
    dosya.close()
    print("{ben} adlı kişi {arkadas} kullanıcıya mesaj gönderdi.".format(ben=kwargs["ben"].title(),arkadas=kwargs["arkadas"].title()))
    input("Devam etmek için bir tuşa basınız.")


def arkadasEkle(**kwargs):
    dosya=open("arkadasliklar.txt","a")
    dosya.write(kwargs["ben"].lower())
    dosya.write(" ")
    dosya.write(kwargs["arkadas"].lower())
    dosya.write("\n")
    dosya.close()
    print("{arkadas} isimli kişiyi arkadaş eklediniz".format(arkadas=kwargs["arkadas"].title()))
    input("Devam etmek için bir tuşa basın.")


def arkadasListesi(kullanici_adi):
    try:
        arkadasVar=False
        dosya=open("arkadasliklar.txt","r")
        satirlar=dosya.readlines()
        for arkadasliklar in satirlar:
            bolunmus=arkadasliklar.split()
            ark_1=bolunmus[0]
            ark_2=bolunmus[1]
            if kullanici_adi==ark_1:
                print(ark_2)
                arkadasVar=True
            elif kullanici_adi==ark_2:
                print(ark_1)
                arkadasVar=True
        if not arkadasVar:
            print("Hiç arkadaşın yok ama üzülme senin de olacak.")
    except FileNotFoundError:
        print("Hiç arkadaşın yok üzülme bu programda kayıtlı kimsenin yok, çünkü daha arkadaşlıklar dosyası bile yok!")
    input("Devam etmek için bir tuşa basın.")





if __name__=="__main__":
    while True:
        print("""
                [1] Kayıt Ol
                [2] Giriş Yap
        
            """)

        secim=int(input("Seçiminizi girin : "))

        if secim==1:
            kullanici_islemleri.kayitOl()
        elif secim==2:
            kullanici_islemleri.girisYap()

            if kullanici_islemleri.cevrimici_kullanici:
               kisiselMenu(kullanici_islemleri.cevrimici_kullanici)
