print("LOL,Cringe,Pc,Hub,Ethernet,Mod")


modern_kelime_soz = {"LOL":"kahkaha atmak", "cringe":"utandırıcı", "PC":"kişisel bilgisayar","hub":"merkez","ethernet":"internet kablosu","mod":"yönetici"}



cevap = input("hangi kelimenin anlamını öğenmek istiyorsun?")

if cevap in modern_kelime_soz:
    print(modern_kelime_soz[cevap])
else:
    print("kelime sozlukte yok")
