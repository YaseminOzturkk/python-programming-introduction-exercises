#----author:Yasemin Öztürk-----
#----date:24.04.2019-----
#soru1

metin ="Açık bilim, araştırma çıktılarına ve süreçlerine herkesin serbestçe erişmesini, bunların ortak kullanımını, dağıtımını ve üretimini kolaylaştıran bilim uygulamasıdır."
print(metin[:19])

#soru2

liste = ['Açık Bilim', 'Açık Erişim', 'Açık Lisans', 'Açık Eğitim', 'Açık Veri', 'Açık Kültür']

for list in liste:
    print(list)

#soru3

sozluk ={"Elma" : "Ağaçta yetişen bir tür meyve" , "Salatalık" : "Fidan üzerinde büyüyen bir tür sebze"}
girilen= input("Bir kelime giriniz:  ")
girilen=girilen.capitalize()
if girilen in sozluk:
    print(sozluk[girilen])
else:
    print("Başka bir kelime giriniz: ")
