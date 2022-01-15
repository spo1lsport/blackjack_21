import random # Rastgele kart dağıtmak için gerekli olan kütüphane.

def GetData(veri): # İstediğiniz veriyi "example.txt" şeklinde listeye çekebilmeye yarar.
    veri_ndx = open(f"{veri}","r")
    veriler = veri_ndx.readlines()
    verilerIR = veriler[0].split(",")
    veri_ndx.close()
    return verilerIR
def UyeOl(): # Üye olma fonksiyonu(Kullanıcı adı, Şifre, Bakiye(Otomatik 1000 bakiye ekler.) bilgilerini txt'ye yazar.).
    def kullaniciAdiEkle(kullanici_adi):
        kullanicilar = open("usernames.txt","a")
        yeni_kullanici = "," + kullanici_adi
        kullanicilar.writelines(yeni_kullanici)
        kullanicilar.close()
    def sifreKaydet(sifre):
        sifreler = open("passwords.txt","a")
        sifreIR = "," + sifre
        sifreler.writelines(sifreIR)
        sifreler.close()
    def bakiyeOlustur(kullanici_adi):
        bakiyeler = open("balance.txt","a")
        yeni_bakiye = "," + "1000"
        bakiyeler.writelines(yeni_bakiye)
        bakiyeler.close()

    kullanici_adi = input("Kullanıcı adı giriniz:")
    while kullaniciAdiKontrol(kullanici_adi) == True:
        print("Bu ad kullanılıyor, lütfen bir daha deneyiniz.")
        kullanici_adi = input("Kullanıcı adı giriniz:")
    kullaniciAdiEkle(kullanici_adi)

    sifre = input("Şifrenizi giriniz:")
    while len(sifre) <8 or len(sifre) >16:
        if len(sifre) <8:
            print("Şifreniz en az 8 karakter uzunluğunda olmalıdır.")
            sifre = input("Şifrenizi giriniz:")
        if len(sifre) >16:
            print("Şifreniz en fazla 16 karakter uzunluğunda olmalıdır.")
            sifre = input("Şifrenizi giriniz:")
    sifreKaydet(sifre)
    bakiyeOlustur(kullanici_adi)
def kullaniciAdiKontrol(kullanici_adi): # Kullanıcı adının sistemde kayıtlı olup olmadığını kontrol eder.
    kullanicilar = GetData("usernames.txt")
    if kullanici_adi in kullanicilar:
        return True
    else:
        return False
def sifreKontrol(kullanici_adi,sifre): # Kullanıcının girdiği ad ve şifrenin sistemde birbiriyle eşleşiğ eşleşmediğini kontrol eder.
    kullanicilar = GetData("usernames.txt")
    sifreler = GetData("passwords.txt")
    if sifre in sifreler:
        kullanici_adı_yeri = kullanicilar.index(kullanici_adi)
        sifre_yeri = sifreler.index(sifre)
        if sifre_yeri == kullanici_adı_yeri:
            return True
        else:
            return False
    else:
        return False
def GirisYap(): # Sisteme giriş yapma fonksiyonu. Giriş yapan kullanıcının adını return eder.
    kullanici_adi = input("Kullanıcı adınızı giriniz:")
    while kullaniciAdiKontrol(kullanici_adi) == False:
        print("Kullanıcı adı sistemde bulunamadı.Lütfen tekrar deneyiniz.")
        kullanici_adi = input("Kullanıcı adınızı giriniz:")
    if kullaniciAdiKontrol(kullanici_adi) == True:
        sifre = input("Şifrenizi giriniz:")
        if sifreKontrol(kullanici_adi,sifre) == True:
            print("Başarıyla giriş yaptınız.")
            print("Tekrar hoşgeldiniz, " + kullanici_adi + ".")
            print("Hesabınızdaki toplam bakiyeniz: " + bakiyeKontrol(kullanici_adi))
            print("Blackjack oyununa hoşgeldiniz.")
            print("-Kurpiyer 16 veya daha az sayıda kart çekmektedir. \n")
            print("-Kurpiyer 17 veya daha yüksek bir sayıda elini saklamaktadır. \n")
            print("-Kazanan kişi bahis yaptığı miktarın 3 katını kazanır. \n")
            return kullanici_adi
        if sifreKontrol(kullanici_adi,sifre) == False:
            while sifreKontrol(kullanici_adi,sifre) == False:
                print("Yanlış şifre girdiniz.")
                sifre = input("Şifrenizi giriniz:")
            print("Başarıyla giriş yaptınız.")
            print("Tekrar hoşgeldiniz, " + kullanici_adi + ".")
            print("Hesabınızdaki toplam bakiyeniz: " + bakiyeKontrol(kullanici_adi))
            print("Blackjack oyununa hoşgeldiniz.")
            print("-Kurpiyer 16 veya daha az sayıda kart çekmektedir. \n")
            print("-Kurpiyer 17 veya daha yüksek bir sayıda elini saklamaktadır. \n")
            print("-Kazanan kişi bahis yaptığı miktarın 3 katını kazanır. \n")
            return kullanici_adi
def uyelikVarMi(): # Kullanıcıya sisteme üyeliğinin olup olmadığını sorar; varsa giriş yapma modulüne gönderir, yoksa üye olma modülüne gönderir. Giriş yapan kullanıcının adını return eder.
    while True:
        try:
            uyelik_var_mi = int(input("Üyeliğiniz varsa 1, yoksa 2 tuşlayınız."))
            if uyelik_var_mi == 2:
                print("Lütfen üye olunuz.")
                UyeOl()
                print("Başarıyla kayıt oldunuz." + "\n" + "Lütfen giriş yapınız.")
                return GirisYap()
                break
            elif uyelik_var_mi == 1:
                print("Lütfen giriş yapınız")
                return GirisYap()
                break
            else:
                print("Yanlış tuşlama yaptınız. Tekrar deneyiniz.")
                pass
        except ValueError:
            print("Yanlış tuşlama yaptınız. Tekrar deneyiniz.")
def bakiyeKontrol(kullanici_adi): # Kullanıcının sistemde kayıtlı olan güncel bakiyesini sorgular.
    bakiyeler = GetData("balance.txt")
    kullanicilar = GetData("usernames.txt")
    kullanici_adı_yeri = kullanicilar.index(kullanici_adi)
    bakiye = bakiyeler[kullanici_adı_yeri]
    return bakiye
def bahis(kullanici_adi): # Kullanıcıdan bahis miktarı alır ve return eder.
    bakiye = int(bakiyeKontrol(kullanici_adi))
    if bakiye < 100:
        bakiyeGuncelleme(kullanici_adi,1000)
        print("Bahis yapacak yeterli bakiyeniz bulunmadığından dolayı bakiyeniz otomatik olarak 1000'e çekilmiştir.")
    while True:
        try:
            print("Ne kadar bahis yapmak istersiniz?")
            bahis_miktari = int(input(f"Bahis miktarınızı giriniz(Güncel bakiyeniz:{bakiyeKontrol(kullanici_adi)} ):"))
            if bahis_miktari > int(bakiyeKontrol(kullanici_adi)):
                print("Yeterli bakiyeniz bulunmamaktadır. Lütfen tekrar deneyiniz.")
            elif bahis_miktari < 100:
                print("Minimum bahis miktarı 100'dür. Lütfen tekrar deneyiniz.")
            elif bahis_miktari <= int(bakiyeKontrol(kullanici_adi)):
                print("Başarıyla bahis yaptınız.")
                return bahis_miktari
        except ValueError:
            print("Sayı olarak miktar belirtmelisiniz. Lütfen yeniden deneyiniz.")
def bakiyeGuncelleme(kullanici_adi,yeni_bakiye): # Bakiye güncellemeye yarar.
    bakiyeler = GetData("balance.txt")
    kullanicilar = GetData("usernames.txt")
    kullanici_adı_yeri = kullanicilar.index(kullanici_adi)
    bakiyeler[kullanici_adı_yeri] = str(yeni_bakiye)
    bakiye_ndx = open("balance.txt","w")
    bakiye_ndx.writelines(",".join(bakiyeler))
    bakiye_ndx.close
def blackjack(): # Oyunun kendisi.
    def kartKontrol(value): # Eldeki kartların toplamını verir.
        toplam = 0
        for numara in value:
            if numara == "J" or numara == "Q" or numara == "K":
                toplam = toplam + 10
            elif numara == "A":
                if toplam + 11 > 21:
                    toplam = toplam + 1
                else:
                    toplam = toplam + 11
            else:
                toplam = toplam + numara
        return toplam
    def kartDagit(value): # Rastgele kart dağıtır.
        random_kart = random.choice(deste)
        deste.remove(random_kart)
        value.append(random_kart)

    deste = [2,3,4,5,6,7,8,9,10,2,3,4,5,6,7,8,9,10,2,3,4,5,6,7,8,9,10,2,3,4,5,6,7,8,9,10,"J","Q","K","A","J","Q","K","A","J","Q","K","A","J","Q","K","A"]

    oyuncu = []
    kurpiyer = []

    for kart in range(2): # Oyunun başında hem oyuncuya hem kurpiyere 2'şer tane kart dağıtır.
        kartDagit(oyuncu)
        kartDagit(kurpiyer)

    print(f"Kurpiyerin elindeki kartlar: {kurpiyer[0]}, X")
    print(f"Elinizdeki kartlar: {oyuncu} Toplam sayınız: {kartKontrol(oyuncu)}")

    if kartKontrol(oyuncu) == 21: # Oyuncunun maç başında Blackjack yapma ihtimaline karşın yazıldı.
        print("Kazandınız.")
        return True
    elif kartKontrol(kurpiyer) == 21: # Kurpiyerin maç başında Blackjack yapma ihtimaline karşın yazıldı.
        print(f"Kurpiyerin elindeki kartlar: {kurpiyer} Toplam sayı: {kartKontrol(kurpiyer)} ")
        print("Kaybettiniz.")
        return False     
    else: # Oyun devam eder, diğer olasılıkları içerir.
        while True:
            try:
                print("Lütfen seçim yapınız.")
                secim = int(input("Kart çekmek isterseniz 1, elinizi saklamak isterseniz 2 tuşlayınız: "))
                if secim == 1:
                    kartDagit(oyuncu)
                    print(f"Elinizdeki kartlar: {oyuncu} Toplam sayınız: {kartKontrol(oyuncu)}")
                    if kartKontrol(oyuncu) > 21:
                        print("Kaybettiniz.")
                        return False
                    elif kartKontrol(oyuncu) == 21:
                        print("Kazandınız.")
                        return True
                    else:
                        continue
                elif secim == 2:
                    if kartKontrol(kurpiyer) <= 16:
                        while kartKontrol(kurpiyer) <= 21 or kartKontrol(kurpiyer) < kartKontrol(oyuncu):
                            kartDagit(kurpiyer)
                            print(f"Kurpiyerin elindeki kartlar: {kurpiyer} Toplam sayı: {kartKontrol(kurpiyer)} ")
                        if kartKontrol(kurpiyer) > 21:
                            print("Kazandınız.")
                            return True
                        elif kartKontrol(kurpiyer) > kartKontrol(oyuncu):
                            print("Kaybettiniz")
                            return False
                        elif kartKontrol(kurpiyer) < kartKontrol(oyuncu):
                            print("Kazandınız")
                            return True
                        elif kartKontrol(kurpiyer) == 21:
                            print("Kaybettiniz")
                            return False
                    elif kartKontrol(kurpiyer) >= 17:
                        if kartKontrol(kurpiyer) > 21:
                            print(f"Kurpiyerin elindeki kartlar: {kurpiyer} Toplam sayı: {kartKontrol(kurpiyer)} ")
                            print("Kazandınız.")
                            return True
                        elif kartKontrol(kurpiyer) > kartKontrol(oyuncu):
                            print(f"Kurpiyerin elindeki kartlar: {kurpiyer} Toplam sayı: {kartKontrol(kurpiyer)} ")
                            print("Kaybettiniz")
                            return False
                        elif kartKontrol(kurpiyer) < kartKontrol(oyuncu):
                            print(f"Kurpiyerin elindeki kartlar: {kurpiyer} Toplam sayı: {kartKontrol(kurpiyer)} ")
                            print("Kazandınız")
                            return True
                else:
                    print("Yanlış tuşlama yaptınız. Lütfen tekrar deneyiniz.")
            except ValueError:
                print("Yanlış tuşlama yaptınız. Lütfen tekrar deneyiniz.")
def bahisKontrol(value): # Bahisten sonra oluşan yeni bakiyeyi hesaplayıp txt dosyasına kaydeder.
    if value == True:
        yeni_bakiye = int(bakiyeKontrol(giris_yapan_kullanici)) + bahis_miktari*2
        bakiyeGuncelleme(giris_yapan_kullanici,yeni_bakiye)
    else:
        yeni_bakiye = int(bakiyeKontrol(giris_yapan_kullanici)) - bahis_miktari
        bakiyeGuncelleme(giris_yapan_kullanici,yeni_bakiye)
def tekrarOyna(): # Kullanıcıya tekrar oynamak isteyip istemediğini sorar sonuca göre devam eder.
    while True:
        try:
            secim = int(input("Bir daha oynamak için 1, çıkmak için 2 tuşlayınız."))
            if secim == 1:
                sonuc = blackjack()
                bahisKontrol(sonuc)
            elif secim == 2:
                break
            else:
                print("Yanlış tuşlama yaptınız. Tekrar deneyiniz.")
        except ValueError:
            print("Yanlış tuşlama yaptınız. Tekrar deneyiniz.")

giris_yapan_kullanici = uyelikVarMi() # Kimin giriş yaptıgı bilgisini saklamak amacıyla yazıldı.

bahis_miktari = bahis(giris_yapan_kullanici) # Bahis almak ve  miktar bilgisini saklamak amacıyla yazıldı.

sonuc = blackjack() # Oyunu başlatır ve oyun sonucunu kaydeder.

bahisKontrol(sonuc) # Bahisten sonra oluşan yeni bakiyeyi hesaplayıp txt dosyasına kaydeder.

tekrarOyna() # Kullanıcıya tekrar oynamak isteyip istemediğini sorar sonuca göre devam eder.