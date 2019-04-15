#   ***Adam Asmaca Oyunu***
# author: Yasemin Öztürk
# date:12.04.2019

print("***Merhaba, Adam Asmaca Oyununa hoşgeldiniz!***")
print("Bu oyunda bazı ülkelere ait başkentleri tahmin etmeniz beklenmektedir.Hadi başlayalım!")

import random
wordList = random.choice(["Prag", "Amman", "Monako", "Wellington", "Abuja", "Lizbon", "Madrid", "Stokholm", "Darüsselam", "Abu Dabi"])
wordList = wordList.upper()
canSayisi = 3
words = []
harfSayisi = "_"

for word in wordList:

    words.append(harfSayisi)

print(words)

while canSayisi > 0:

    i = 0

    tahmin = input("\nBir harf giriniz: ")
    tahmin = tahmin.upper()

    if tahmin in wordList:
        for kontrol in wordList:
            if wordList[i] == tahmin:
                words[i] = tahmin
            i += 1

        print("")
        print(words)
        print("\n \"%s\" harfi " %tahmin)

    else:
        canSayisi -= 1
        print("")
        print(words)
        print("\n\"%s\" harfi yanlış. Başka harf gir" % tahmin)
        print("\nKalan can sayısı = " + "[" + canSayisi * " ♥ " + "] = " + str(canSayisi))

    if canSayisi == 0:
        print("Maalesef bilemediniz! Doğru kelime: %s" % wordList)
        break


    if harfSayisi not in words:
        print("\nTebrikler! Doğru kelimeyi buldun")
        break




