print("--------------------------Solucan Klası-------------------------")
class Solucan:
    def __init__(self, sinif, cins):      #iki değişken oluşturuyoruz.
        self.sinifi = sinif
        self.cinsi = cins
    def __str__(self):           #__str__ ile print fonksiyonunu yazıyoruz.
        return "Solucanlar; Yassı, Yuvarlak, Halkalı olarak ayrılırlar."
    def tanit(self):    #kendimiz fonksiyonlar oluşturuyoruz.
        print(f"{self.cinsi}, hayvanlar aleminin {self.sinifi} sınıfında bulunur.")
    def ozellik_ver(self):
        print("Ömrü 2-6 yıl kadardır.")
    def solucana_isim_ver(self):
        solucanismi = str(input("Solucana isim ver: "))
        print("Solucanın ismi:",solucanismi)
        

#Kodun çalıştırılması       
solucan1 = Solucan("Omurgasızlar","Yassı Solucan")
print(solucan1.sinifi)    #özellikleri çağırırken parantez kullanmıyoruz.
print(solucan1.cinsi)
print(solucan1)
solucan1.tanit()        #fonksiyonları çağırırken parantez kullanıyoruz.
solucan1.ozellik_ver()
solucan1.solucana_isim_ver()


print("--------------------------Kurbağa Klası-------------------------")
class Kurbaga(Solucan): #İçerisine Solucan yazarak Solucan class'ından miras alıyoruz.
    def __str__(self):  #__str__ fonksiyonunu override ediyoruz. Artık Solucan class'ındaki yerine bu geçerli olacak.
        return """Kurbağalar: Hayvanlar aleminin Omurgalılar sınıfında bulunurlar. Toplam 33 familyaya dağılmış yaklaşık 5250 türü bulunur."""
    def ozellik_ver(self):
        print("Amfibi (ikiyaşamlı) canlılardır.")
    def puan_ver(self):
        puan = int(input("Kurbağalara 10 üzerinden kaç puan verirdiniz? : "))
        if puan <10:
            print("Yanlış! Doğru cevap 10 puan olacaktı.")
        else:
            print("Çok doğru!")
        

#Kodun çalıştırılması
kurbaga1 = Kurbaga("Omurgalılar", "Toprak Kurbağası")
print(kurbaga1.sinifi)
print(kurbaga1.cinsi)
print(kurbaga1)
kurbaga1.tanit()
kurbaga1.ozellik_ver()
kurbaga1.puan_ver()


print("--------------------------Balık Klası-------------------------")
class Balik():
    def __init__(self,sinif, cins):
        self.sinifi = sinif
        self.cinsi = cins
    def ornek_ver(self):
        balik_listesi = ["Yılan Balığı","Vatoz Balığı", "Somon", "Orkinos"]
        if self in balik_listesi:
            balik_listesi.remove(self)
        else:
            print("Balıklara örnekler:\n", balik_listesi)
    def pop_quiz(self):
        cevap = input("Balık yemeyenlere ne denir? : ")
        if cevap.lower() == "pesketaryen":
            print("Doğru!")
        else:
            print("Yanlış! Doğru cevap Pesketaryen olmalıydı.")
    
    
#Kodun çalışması
balik1 = Balik("Omurgalılar", "Levrek")
print(balik1.sinifi)
print(balik1.cinsi)
balik1.ornek_ver()
balik1.pop_quiz()


print("--------------------------Sünger Klası-------------------------")

class Sunger():
    def __init__(self,sinif,cins):
        self.sinifi = sinif
        self.cinsi = cins
    def __len__(self):         #normalde listelerde çalışan len() fonksiyonunu biz tanımlıyoruz.
        print("Tanımlanmış yaklaşık 5000 türü vardır.")
    def soru_sor(self):
        cvp = input("En ünlü sünger kimdir? : ")
        if cvp.lower() == "süngerbob":
            print("Doğru cevap!!")
        else:
            print("Yanlış! Doğru cevap SüngerBob olacaktı...")
    def bilgi_ver(self):
        print("Süngerler, en ilkel çok hücreli canlı gruplarındandır.")

#Kodun çalışması
sunger1 = Sunger("Omurgasızlar", "Deniz süngeri")
print(sunger1.sinifi)
print(sunger1.cinsi)
sunger1.__len__()
sunger1.bilgi_ver()
sunger1.soru_sor()


print("--------------------------Eklem Bacaklılar Klası-------------------------")
class Eklembacak():
    def __init__(self,sinif,cins):
        self.sinifi = sinif
        self.cinsi = cins
    def __len__(self):
        print("Tanımlanmış yaklaşık 1 milyon türü vardır.")
    
    def bilgi_ver(self):
        print("Eklembacaklılar, omurgasızların en büyük grubudur.")
    
    def ornek_ver(self):
        print("Karada örümcekler, akrepler ve böcekler; denizlerdeyse yengeçler ve karidesler eklembacaklılara örnektir.")
    def en_korkunc_eklem_bacakli(self):
        bocek = str(input("En korkunç böcek nedir? : "))
        if bocek.lower() == "örümcek":
            print("Doğru cevap!!")
        else:
            print("O da korkunç ama en korkuncu örümcek... 🕷🕷🕷")
        
    
#Kodun çalışması
eklembacak1 = Eklembacak("Omurgasızlar", "Örümcek")
print(eklembacak1.sinifi)
print(eklembacak1.cinsi)
eklembacak1.bilgi_ver() 
eklembacak1.ornek_ver()
eklembacak1.en_korkunc_eklem_bacakli()


print("--------------------------Kedi Klası-------------------------")

class Kedi:
    def __init__(self, cins, goz_renk, tuy_renk):
        self.cins = cins
        self.goz_renk = goz_renk
        self.tuy_renk = tuy_renk
    def miyavla(self):
        print("Miyaaaav")
    def insan_yasi_karsiligi(self, kedi_yasi):
        if kedi_yasi == 1:
            print("1 yaşındaki kedinin insan yaşı: 15")
        elif kedi_yasi == 2:
            print("2 yaşındaki kedinin insan yaşı: 24")
        else:
            print(f"{kedi_yasi} yaşındaki kedinin yaşı:")
            kedi_yasi = 24 + (kedi_yasi-2)*4
            print(kedi_yasi)
    def en_guzel_kedi_rengi(self):
        renk = str(input("En güzel kedi rengi nedir? : "))
        if renk.lower() == "turuncu":
            print("Aynen öyle!")
        else:
            print("Hayır, bence turuncu.")


#Kodun çalışması
kedi1 = Kedi("Scottish","Mavi","Beyaz")
print("Yaren'in kedisinin göz rengi :" , kedi1.goz_renk)
print("Kedinin tüy rengi : " , kedi1.tuy_renk)
print("Yaren'in kedisinin cinsi :" , kedi1.cins)
print("Kedi şöyle ses çıkarır : " )
kedi1.miyavla()
kedi1.en_guzel_kedi_rengi()


print("--------------------------Köpek Klası-------------------------")

class Kopek:
        def __init__(self,cins= "",cinsiyet="",yas="1"):  #kullanıcı verileri girmeyince attribute'ların alacağı değerleri belirliyoruz.
            self.cinsi = cins
            self.cinsiyeti = cinsiyet
            self.yasi = yas
        def ses_cikar(self):
            print("Kızgın köpek ne der? : Havhavhav")
        def insan_yasina_cevir(self):
            x = int(input("Sizin evcil hayvanınızın yaşı kaç ? : "))
            if x == 1:
                print("evcil hayvanınızın insan yaşı: 15")
            elif x == 2:
                print("evcil hayvanınızın insan yaşı: 24")
            else:
                insan_yasi = 24 + ((x-2)*5)
                print(f'{x} yaşındaki evcil hayvanınızın insan yaşı: {insan_yasi}')
                
            #Operator overloading: Python'da var olan bir operator fonksiyonun bizim class'ımızda çalışması için tekrar yazmak. 
            #Mesela __add__(self,other) => toplama, __sub__(self,other) => çıkarma , __mul__(self,other) =>çarpma
        def __add__(self,other): #Operator overloading yapıyoruz.
            return self.yasi + other.yasi   #burada other dediğimiz toplayacağımız diğer class elemanı
        def en_guzel_kopek_cinsi(self):
            cinss = str(input("En güzel köpek cinsi nedir? : "))
            if cinss.lower() == "golden":
                print("🐶 Doğru! 🐶")
            else:
                print("🐶 Hayır bence golden.🐶")
        

#kodun çalışması     
kopek1 = Kopek("Labrador","Erkek",4)   
kopek2 = Kopek("Poodle","Dişi",2)
print("Benim köpeğimin cinsi :" , kopek1.cinsi)
print("Benim köpeğimin cinsiyeti :" , kopek1.cinsiyeti)
print("Benim köpeğimin yaşı :" , kopek1.yasi)
print("Benim 2.köpeğimin yaşı :" , kopek2.yasi)
kopek2.ses_cikar()
kopek1.insan_yasina_cevir()

print("Birinci ve ikinci kopeklerimin yaşları toplamı :",kopek1 + kopek2)  #__add__ fonksiyonumuzla 2 köpeğin yaşlarını topluyoruz.
kopek1.en_guzel_kopek_cinsi()

print("--------------------------Papağan Klası-------------------------")
class Papagan(Kopek):   #miras
    def ses_cikar(self):     #override
        x = input("Papağan ne diye ses çıkarır? : ")
        print("Papağan sen ne söylersen onu söyler! Yani:",x)
        

#kodun çalışması         
papagan1 = Papagan("Sultan","Erkek",12)
papagan2 = Papagan("Afrika Gri","Dişi",17)  
print("1 numaralı papağanın cinsi:" , papagan1.cinsi)
print("2 numaralı papağanın cinsi:" , papagan2.cinsiyeti)
print("1 numaralı papağanın yaşı:" , papagan1.yasi)
print("2 numaralı papağanın yaşı:" , papagan2.yasi)
print("Birinci ve ikinci papağanın yaşları toplamı:",papagan1 + papagan2) #__add__ fonksiyonunu çağırabiliyoruz çünkü Kopek class'ından miras aldık.

papagan1.ses_cikar()
papagan1.insan_yasina_cevir()

