print("1-Elma 3$\n 2-Portakal 2.5$\n 3-Patates 1$\n 4-Domates 2$")
x=int(input("Ne satın almak istersiniz?  "))
y=int(input("Kaç kilo olsun?  "))
if x==1:
    print("Tutarınız=",y*3,"$")
if x==2:
    print("Tutarınız=",y*2.5,"$")
if x==3:
    print("Tutarınız=",y*1,"$")
if x==4:
    print("Tutarınız=",y*2,"$")