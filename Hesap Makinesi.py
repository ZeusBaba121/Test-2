r=int(input("Bir Sayı Giriniz  "))
print(" ")
print("Lütfen yapmak istediğiniz işlemi giriniz")
islem=int(input("Toplama için 1\n Çıkartma için 2\n Çarpma için 3\n Bölme için 4e tıklayınız  "))
print(" ")
t=int(input("İkinci bir sayı giriniz  "))
print(" ")
if islem==1:
    print("İşlem sonucu=",r+t)
if islem==2:
    print("İşlem Sonucu=",r-t)
if islem==3:
    print("İşlem Sonucu=",r*t)
if islem==4:
    print("İşlem Sonucu=",r/t)
