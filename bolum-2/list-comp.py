sayilar = []  # sayilar adında boş bir liste tanımladık

for i in range(5):  # 0-4 arası sayıları listeye eklemek için döngü
    sayilar.append(i) # i değerini listeye ekleme
print(sayilar)     # güncel listeyi yazdırma

#sayilar.append(i*2) desek iki katını alarak eklemiş olurduk.

sayilar2 = [i for i in range(5)]  # liste üretim yöntemi ile 0-4 arası sayılar

print(sayilar2)                    # sayilar2 listesini yazdırma


kurum="Btk Akademi"

for i in kurum:   #kurum içerisindeki her bir i değeri bir karaktere denk gelir.
    print(i)   #tek tek stringimizin harflerini yazdırır.

    print(i.upper()) #alt satırında büyük harf halini yazar.

sonuc=[i for i in kurum] #liste içerisinde / i.upper() deseydin her bir karakterin büyük harfle yazılmasını sağlardın.
print(sonuc) #değerler liste içerisinde gösterilir.

 