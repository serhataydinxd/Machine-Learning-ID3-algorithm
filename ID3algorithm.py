# 152120221118, Serhat Aydın
# ID3 Algorithm
while True:
    calisma = int(input("Çalışma saati giriniz: (0:Düşük 1:Yüksek) "))
    if calisma:
        print("Geçti \n")
    else:
        zorluk = int(input("Dersin zorluk derecesi giriniz: (0:Düşük 1:Yüksek) "))
        if zorluk:
            devam = int(input("Dersin devam durumu giriniz: (0:Düşük 1:Yüksek) "))
            if devam:
                ortalama = int(input("Geçmiş ortalama notunu giriniz: (0:Düşük 1:Yüksek) "))
                if ortalama:
                    print("Geçti \n")
                else:
                    print("Kaldı \n")
            else:
                print("Kaldı \n")
        else:
            devam = int(input("Dersin devam durumu giriniz: (0:Düşük 1:Yüksek) "))
            if devam:
                ortalama = int(input("Geçmiş ortalama notunu giriniz: (0:Düşük 1:Yüksek) "))
                if ortalama:
                    print("Geçti \n")
                else:
                    print("Kaldı \n")
            else:
                ortalama = int(input("Geçmiş ortalama notunu giriniz: (0:Düşük 1:Yüksek) "))
                if ortalama:
                    print("Geçti \n")
                else:
                    print("Kaldı \n")
