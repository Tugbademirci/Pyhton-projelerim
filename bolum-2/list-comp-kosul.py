        #GENEL KULLANIMI:
#for item in liste:
#   if (kosul):   #liste içerisindeki elemanlara koşul koyma
#   expression  #eğer koşul doğruysa expression(ifade)yazabiliyoruz.

#[expression for item in liste] aynısını comprehension ile yazma şeklidir.ancak tüm liste elemanlarını istemiyorsak;
#[expression for item in liste if koşul] diyerek bir koşul ekleyebiliriz.Koşul en sona eklenir!


        #ÖRNEKLER

sayilar=[3,5,7,6,56,34] #kendi oluşturduğumuz liste elemanları
sonuc=[] #filtrelenen değerlerimizi alcağımız değişken tanımı

for sayi in sayilar: #sayilar listesindeki tüm elemanlara ulaş
    if(sayi %2 == 0 ): #listedeki sadece çift olanlar
        sonuc.append(sayi)  #sonuç içerisine ekleme

#print(sonuc)        #6,56,36 yani çift olanlar ekrane gelir 

sonuc = [sayi  for sayi in sayilar if sayi %2 == 0 ]   # comprehension kullanma amacı işleri biraz daha kolaylaştırmaktır.Üstteki üç satır kodu tek satıra indirgemiş olduk.Liste elemanlarını direkt filtreledik.


sonuc =[sayi if sayi %  2 ==0 else "tek sayi" for sayi in sayilar  ] #for döngüsü olduğu gibi yazılır ve dönecek sayıyı doğrudan sonuç değişkenine almadan önce ekstra koşul yazmış olduk.Sayı çiftse değişkene ata ama tekse geri dönecek sayı değişkenini tek sayıya at demiş olduk.Tüm değerler geldi gelen değerlere göre tek çift ayırması yapmış olduk.İlkinde tek değerleri direkt göz ardı etmiştik.   

#print(sonuc)  #ekrana ['tek sayı', 'tek sayı', 'tek sayı', 6, 56, 34 ] yazılmış olur.





urun_fiyatlari = [3000,1000,4000,0,5000] #farklı bir liste daha oluşturduk.
vergiler =[]

for fiyat in urun_fiyatlari: #her gelen ürün fiyatı üzerinde;
    if(fiyat > 0):   #eğer fiyat 0'dan büyük ise
          vergiler.append(fiyat * 1.20) #her gelen fiyat üzerinde %20 oranında vergiyi hesaplayıp o şekilde vergiler listesine atamış olacağız.
#print(vergiler)       #güncellenmiş yani vergili ürün fiyatlarını görüntülemiş olduk.[3600.0, 1200.0, 4800.0, 6000.0]




#yukarıdaki kodların comprehension kullanılmış hali:
vergiler=[fiyat * 1.20  for fiyat in urun_fiyatlari if fiyat > 0] #doğrudan fiyatın 0'dan büyük olması sonucunda baştaki çarpım işlemi gerçekleştirilir.
vergiler=[fiyat if fiyat > 0 else "vergi hesaplanmadi" for fiyat in urun_fiyatlari] #0 olan değer içinde ekrana 'vergi hesaplanmadı' yazılmasını sağlamış olduk.

print(vergiler) #yine aynı vergili sonuçları elde etmiş olduk