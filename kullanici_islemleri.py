import time,os
cevrimici_kullanici=False

def girisYap():
    global cevrimici_kullanici
    kullanici_adi=input("Kullanıcı adınızı girin  :  ")
    sifre=input("Şifrenizi girin  : ")

    dosya=open("kullanicilar.txt","r")
    satirlar=dosya.readlines()
    cevrimici_kullanici=False
    for kullanici in satirlar:
       bolunmus=kullanici.split()
       bolunmus_k_adi=bolunmus[0]
       bolunmus_k_sifre=bolunmus[1]
       if kullanici_adi == bolunmus_k_adi and sifre==bolunmus_k_sifre:
           cevrimici_kullanici=kullanici_adi
    if cevrimici_kullanici:
        print("Hoşgeldiniz: ",kullanici_adi)
    else:
        print("Bilgilerinizi Kontrol ediniz ve Oturumu tekrar açmayı deneyiniz!!!")
    input("Devam etmek için bir tuşa basın.")




def kayitOl():
    kullanici_adi=input("Kullanıcı adı girin : ")
    mail=input("Mail adresinizi girin : ")
    if not kontrol(kullanici_adi):
        #Kullanici Adi müsait değilse
        print("===========Kullanıcı Adı Zaten Mevcut============")
        time.sleep(1)
        return kayitOl()
    sifre=input("Şifrenizi girin : ")
    sifre_onay = input("Şifrenizi girin : ")

    if sifre!=sifre_onay:
        print("=============Şifreler eşleşmiyor!!!!!!!!!!!!")
        time.sleep(1)
        return kayitOl()

    dosya=open("kullanicilar.txt","a")
    dosya.write(kullanici_adi)
    dosya.write(" ")
    dosya.write(sifre)
    dosya.write(" ")
    dosya.write(mail)
    dosya.write("\n")
    dosya.close()
    print("Kullanıcı Kaydedildi..")
    input("Devam etmek için bir tuşa basın.")



def kontrol(kullanici_adi):
    try:
        if kullanici_adi not in open("kullanicilar.txt","r").read():
            return True
        else:
            return False
    except FileNotFoundError:
        return True



if __name__=="__main__":      # bu şart programın direk çalıştırılıp çalıştırılmadıgını kontrol eder
    while True:
        print("""
                [1] Kayıt Ol
                [2] Giriş Yap
             """)

        secim = int(input("Seçiminizi yapın : "))

        if secim == 1:
            kayitOl()
        elif secim == 2:
            girisYap()








