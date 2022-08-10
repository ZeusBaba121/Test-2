#Değişken Kuralları
#(1) Değişken adı rakam ile başlamaz.
1isim="Ahmet"
print(isim) #Yanlış

isim="Ahmet"
print(isim) #Doğru

#(2) Değişken adları özel sembol içermez (_ hariç)
x+isim="Ali"
print(x+isim)  #Yanlış

xisim="Ali"
print(xisim)

#(3) Değişken isimlerinde boşluk kullanılmaz

ad soyad=ahmet adam
print(ad soyad) #Yanlış

ad_soyad=ahmet adam

#(4) Değişken adlarında özel anlam ifade eden kelimeler kullanılmaz.(Yazılım komutları etc.)
True=5
#Böle bişi yapılamaz çünki "True" bir komut
    #Python büyük küçük hafre duyarlı ve ikisini farklı değerler olarak verebiliyorsun.
    #Komutları büyük küçük harfleri değiştirerek değişken olarak kullanabiliyorsun
x=55
X=66
print(x+X)

true=5
And=37
print(true+And)

#import keyword     import komutu ile pythondaki kütüphaneleri gösterebilyorsun
#keyword.kwlist      <- örnek

#Farklı değişkenlere tek satırda aynı değeri verebiliyorsun
a=b=c=6
print(a*c+b)

#Duruma göre çift veya tek tırnak kullanılabiliniyor