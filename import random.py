import random

def tas_kagit_makas_FATMA_KAÇAR():
    print("Taş, Kağıt, Makas oyununa hoş geldiniz!")
    print("Oyunun kuralları:")
    print("Taş, Kağıt, Makas seçeneklerinden birini seçin.")
    print("İlk iki turu kazanan oyunu kazanır.")
    print("Oyundan çıkmak için 'q' tuşuna basabilirsiniz.")
    
    secenekler = ["taş", "kağıt", "makas"]
    oynanan_oyun_sayisi = 0
    oyuncu_galibiyetleri = 0
    bilgisayar_galibiyetleri = 0
    
    while True:
        oyuncu_tur_galibiyetleri = 0
        bilgisayar_tur_galibiyetleri = 0
        oynanan_oyun_sayisi += 1
        
        while oyuncu_tur_galibiyetleri < 2 and bilgisayar_tur_galibiyetleri < 2:
            oyuncu_secimi = input("Taş, kağıt veya makas seçin: ").lower()
            
            if oyuncu_secimi == 'q':
                print("Oyundan çıktınız.")
                return
            
            if oyuncu_secimi not in secenekler:
                print("Geçersiz bir seçenek girdiniz. Lütfen tekrar deneyin.")
                continue
            
            bilgisayar_secimi = random.choice(secenekler)
            print(f"Bilgisayarın seçimi: {bilgisayar_secimi}")
            
            if oyuncu_secimi == bilgisayar_secimi:
                print("Beraberlik!")
            elif (oyuncu_secimi == "taş" and bilgisayar_secimi == "makas") or \
                 (oyuncu_secimi == "kağıt" and bilgisayar_secimi == "taş") or \
                 (oyuncu_secimi == "makas" and bilgisayar_secimi == "kağıt"):
                print("Oyuncu kazandı!")
                oyuncu_tur_galibiyetleri += 1
            else:
                print("Bilgisayar kazandı!")
                bilgisayar_tur_galibiyetleri += 1
        
        if oyuncu_tur_galibiyetleri == 2:
            oyuncu_galibiyetleri += 1
            print("Oyuncu oyunu kazandı!")
        else:
            bilgisayar_galibiyetleri += 1
            print("Bilgisayar oyunu kazandı!")
        
        devam = input("Başka bir oyun oynamak ister misiniz? (e/h): ").lower()
        if devam != 'e':
            break

    print(f"Oynanan oyun sayısı: {oynanan_oyun_sayisi}")
    print(f"Toplam oyuncu galibiyetleri: {oyuncu_galibiyetleri}")
    print(f"Toplam bilgisayar galibiyetleri: {bilgisayar_galibiyetleri}")
    print("Oyun bitti. Teşekkürler!")

# Fonksiyonu çalıştırmak için aşağıdaki satırı kullanın
tas_kagit_makas_FATMA_KAÇAR()