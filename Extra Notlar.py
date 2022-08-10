#String kullanırken eğer tek tırnak işareti ile almak istiyorsan fakat cümlenin içinde de tek tırnak işareti varsa, o tırnak işaretinden önce \ koyup onun stringi bitiren tırnak işareti olmadığını belirtebiliyorsun.
print('Ali\'nin topu') #örnek
print(" ")

#print komutunu kullanırken alt satıra geçmeden öyle yazdırmasını işteniliyorsa kelimeler arasına \n yazılır.
print("Merhaba\nDünya")
print(" ")

#print komutunu kullanırken yazdığının belirli bir harfiniveya kısmını yazdırmak istersen eğer yazdığın stringeden sonra köşeli parantez içine kaçıncı harf veya kaçıncı harften kaçıncı harfe almak istediğini yazıyon.
print("Hello World"[4:9])
print(" ")

#ilk iki kısmı boş bırakıp 3. kısma bi sayı yazarsan hep o sayıncı olan harfleri yazdırır.
print("Ali topu bana at."[::3])
print(" ")

#Eğer değere negatif bir sayı verirsen 3. kısımda tersten yazdırır.
print("Ali topu bana at."[::-1])
print(" ")

#Stringeden sonras ".upper()" yazdığında stringin tamamını büyük yazdırır.
print("Hello World".upper())
print(" ")
#(Aynı şekilde ".lower()" stringi küçültür.)

#print(title()) çümledenki bütün kelimelerinin ilk harfini büyültüyor.
#print(capitalize()) cümlenin ilk harfini büyültür.
#print(swapcase()) büyük küçük şeysilerini tersine çevirir.
#print(replace()) ile harfleri veya kelimeleri başka şeylerle değişebiliyon
#print(count()) harfleri sayar.