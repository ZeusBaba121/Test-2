x=int(input("Saniye sayısı giriniz  "))
yıl=x//31104000
kalan=x%31104000
ay=kalan//2592000
kalan2=kalan%2592000
gün=kalan2//86400
kalan3=kalan2%86400
saat=kalan3//3600
kalan4=kalan3%3600
dakika=kalan4//60
saniye=kalan4%60
print("yıl=",yıl,"ay=",ay,"gün=",gün,"saat=",saat,"dakika=",dakika,"saniye=",saniye)