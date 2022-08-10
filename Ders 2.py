#Eğer printlerken tırnak işareti konulursa onu özel isim olarak algılar.
#Fakat eğer koyulmazsa onu olduğ gibi kullanır.

y="Ali"
z="Veli"
print(y+" "+"ile"+" "+z)
print(" ")

#Aritmatik Operatörler

#Toplama: +   Üs alma: **
#Çıkarma: -   Tam Bölme: //
#Çarpma: *    Mod alma: %
#Bölme: /

#Eğer işlemleri sayıları tırnak içine alarak yazarsan, sayıları string olarak görür ve sayıları toplamak yerine yanyana koyar.

print(10+20) #int
print("10"+"20") #str
print(" ")

#Stringleri bir sayı ile çarparsan sonuç olarak o stringi veerilen sayı kadar çoğaltır.
print("-"*10)
print("20"*20)
print(" ")

#Karekök alırken 1/2yi parantezsiz yazarsan işlem önceliği nedeni ile o sayıyı sadece 2ye böler.
#1/2 yerine direk 0.5 yazabilirsin

print(25**0.5)
print(25**(1/2))
print(" ")

#print(pow(;;)) yazarak direk virgül ile sayının üssünü veya karekökünü alabilirsin.

print(pow(30,2))
print(" ")

#"e" 10 üssü demek
x=5e3  #= x=5x10^3
print(x)
print(" ")

