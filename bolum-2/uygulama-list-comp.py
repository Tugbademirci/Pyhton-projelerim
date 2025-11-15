#1- (1-100) arası sayılardan 12'e tam bölünebilen sayı listesi oluşturma 

sonuc=[i for i in range(1,101) if i % 3 == 0 if i %4 == 0] #1 ile 100 arası olan sayılarda dolaşıyoruz,sayı 12 ile bölünüyorsa;
print(sonuc) #1 ile 100 arası 12'ye bölünenler ekrana yazılır.



#2- Verilen text içersindeki rakamları içeren bir liste oluşturma
#text = "Hello 12345 World" => [1,2,3,4,5]

text = "Hello 12345 World"
sonuc = [i for i in text if i.isdigit()] # isdigit():rakamlar için true döndürür.
print(sonuc)



#3-Sicakliklar listesinde bulunan her hava sıcaklık bilgisine göre 4 derecenin altında buzlanma tehlikesi yazın.
#sicakliklar = [20,15,0,-5,-2] => [20,15,"Buzlanma Tehlikesi","Buzlanma Tehlikesi","Buzlanma Tehlikesi"]

sicakliklar = [20,15,0,-5,-2]
sonuc = [i if i>= 4 else "Buzlanma Tehlikesi" for i in sicakliklar ] #if-else tüm değerlere göre filtreleme 
print(sonuc)



#4- ogrenciler ve notlar listelerindeki notu 50 den fazla olan kişileri ekrana dict verisinde yazdırınız
    #ogrenciler = ["ali","ahmet","canan"]
    #notlar = [50,60,80]
    # => "{'ahmet' : 60, 'canan' : 80}"

ogrenciler = ["ali","ahmet","canan"]
notlar = [50,60,80]

#[("ali",50), ("ahmet",60), ("canan",80)]listelemesi isteniyor:
liste =[(ogrenciler[i], notlar[i]) for i in range(0, len(ogrenciler))]  #len(ogrenciler):length'ine ulaşma.ogrenciler(i):listenin i. elemanına ulaşma.
liste_dict = { key:value for (key,value) in liste if value > 50}   #key:ali value:50 gibi.

print(liste_dict)



#5- for döngüsüyle yazılan uygulamayı comprehension ile yazınız.
sonuc  = []
#iç içe döngü mantığı. 0-0 , 0-1 , 0-2, 1-0....

for x in range(3): #0,1,2
    for y in range(3):
        sonuc.append((x,y))

sonuc= [(x,y) for x in range(3) for y in range(3) ]
print(sonuc)



