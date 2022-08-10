#Tam bölme (//) virgüllü göstermiyor sadece sayıyı gösteriyor vigülü görmek için normal bölme yapman gerekiyor
print(100//9)
print(" ")

# % işlemi ile sadece kalanı elde ediyorsun
print(100%9)
print(" ")

#int(input("...")) komutuyla kod kişiden bir değer ister ve değere isim verir.
x=int(input("Gün sayısını gir"))
yıl=x//365
kalan=x%365

ay=kalan//30
gün=kalan%30

print("yıl=",yıl,ay,gün)
print(" ")

#del komutu değişkenleri veya diğer şeylerin değerlerini silmeye yarayan komut.
x=93
del x
print(" ")

#round komutu sayıyı tama yuvarlar.
x=23.31231231
print(round(x))
print(" ")

#Daire alan hesaplama
r=int(input("Yarı çapı gir"))
pi=3.14
alan= pi*r**2
çevre=2*pi*r

print("********Dairenin alanını ve çevresini hesaplama*****")
print(" ")
print("Yarıçap=",r)
print("Alan=",alan)
print("Çevre=",çevre)
print("____________________________________________________")
print(" ")

