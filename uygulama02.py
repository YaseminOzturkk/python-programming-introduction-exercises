       # _author_:"Yasemin Öztürk"
       # date: 05.04.2019
       
print("Hadi biraz bilgilerimizi ölçelim!")
print("Başlıyoruz dostum!...")
print("---------------------------------------------------------------------------------------------------")

sorular = ['Türkiye\'nin yüz ölçümü en büyük komşusu hangisidir?',
            'Bir gün kaç saniyedir?',
            '1950\'li yılların sonlarında tahılları yedikleri gerekçesiyle ülkesindeki tüm serçelerin öldürülmesini emreden ünlü dikdatör kimdir?',
            '1972\'de Apollo 17 uzay aracı mürettebatınca çekilen ve yerküreyi bütün olarak gösteren ünlü fotoğrafın adı nedir?',
            'Hangisi daha önce gerçekleşmiştir?']
cevaplar = ['A', 'C', 'B', 'B', 'D']
cevapA = ['İran', '86000', 'Josef Stalin', 'Mavi Boncuk', 'Fransız İhtilali']
cevapB = ['Suriye', '88600', 'Mao Zedong', 'Mavi Bilye', 'Birinci Dünya Savaşı']
cevapC = ['Yunanistan', '86400', 'Adolf Hitler', 'Mavi Gezegen', 'NATO\'nun kurulması']
cevapD = ['Irak', '86800', 'Benito Mussolini', 'Apollo Mavi', 'Amerika\'nın Keşfi']
puan = 0
for i in range(len(sorular)):
    print("Soru " + str(i+1)+":"+sorular[i])
    print("A) " + cevapA[i])
    print("B) " + cevapB[i])
    print("C) " + cevapC[i])
    print("D) " + cevapD[i])
    cevap = input("Cevabınızı Giriniz: ")
    if cevaplar[i] == cevap.upper():
        puan +=1
print("Tebrikler,testi tamamladınız!")
print("Aldığınız not: " +str(int((puan/len(sorular))*100)))
input()
