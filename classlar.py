#1. Ixtiyoriy ikkita son berilgan. Ularning yig„indisini,
# #ayirmasini, ko’paytmasini va nisbatini toping.
# class Amallar:
#     def __init__(self,a,b):
#         self.a=a
#         self.b=b
#     def yigindi(self):
#         return (self.a+self.b)
#     def ayirma(self):
#         return (self.a-self.b)
#     def kopaytma(self):
#         return (self.a*self.b)
#     def bolinma(self):
#         return (self.a/self.b)
# son=Amallar(4,6)
# print(son.yigindi())
# print(son.ayirma())
# print(son.kopaytma())
# print(son.bolinma())

#2. To’g„ri burchakli uchburchakning katetlari a va b.
#Uchburchakning yuzi va perimetrini toping.
# class Uchburchak:
#     def __init__(self,a,b,):
#         self.a=a
#         self.b=b
#
#     def uchyuz(self):
#         return ((self.a*self.b)/2)
#     def uchper(self):
#         return self.a+self.b+(self.a**2+self.b**2)**(1/2)
# son=Uchburchak(3,4)
# print(son.uchyuz())
# print(son.uchper())

#3-masala3. Radiusi R bo’lgan aylananing uzunligini va doiraning
#yuzini toping
# from math import pi
# class Peri:
#     def __init__(self,r):
#         self.r=r
#     def uzunligi(self):
#         return (2*pi*self.r)
#     def yuzi(self):
#         return (pi*(self.r)**2)
# son=Peri(4)
# print(son.uzunligi())
# print(son.yuzi())

#4-msala  Doiraning yuzi S. Uning radiusini toping.
# from math import pi
# class Doira:
#     def __init__(self,s):
#         self.s=s
#     def radius(self):
#         return (self.s/pi)**1/2
# son=Doira(3.14)
# print(son.radius())

#5-masala
# class Kordinata:
#     def __init__(self,x1,y1,x2,y2):
#         self.x1=x1
#         self.y1=y1
#         self.x2=x2
#         self.y2=y2
#     def masofa(self):
#         return ((self.x1-self.y1)**2+(self.x2-self.y2)**2)**(1/2)
# son=Kordinata(4,1,6,2)
# print(son.masofa())
#6-masala
# class Yuza:
#     def __init__(self,x1,y1,x2,y2,x3,y3):
#         self.x1=x1
#         self.x2=x2
#         self.x3=x3
#         self.y1=y1
#         self.y2=y2
#         self.y3=y3
#     def yuzi(self):
#         return ((((self.x1-self.x2)**2+(self.y1-self.y2)**2)**(1/2))*(((self.x2-self.x3)**2+(self.y2-self.y3)**2))**(1/2))*(1/2)
# son=Yuza(1,4,1,1,1,5)
# print(son.yuzi())


#7-masala
# class Amallar:
#     def __init__(self,a,b):
#         self.a=a
#         self.b=b
#     def orta_arifmetik(self):
#         return (self.a+self.b)/2
#     def orta_geometrik(self):
#         return (self.a*self.b)**1/2
# son=Amallar(8,16)
# print(son.orta_arifmetik())
# print(son.orta_geometrik())

#8-masala
# To’g’ri to’rtburchak diagonali uchlarining
#koordinatalari berilgan. Uning yuzini toping.
# class Diagonal:
#     def __init__(self,d1,d2):
#         self.d1=d1
#         self.d2=d2
#     def yuza(self):
#         return (self.d1*self.d2)/2
# son=Diagonal(6,4)
# print((son.yuza()))


#9. Uch xonali butun son berilgan. Bu son raqamlarining
#yig’indisini va ko’paytmasini toping.
# class uchxonali_son:
#     def __init__(self,a,b,c):
#         self.a=a
#         self.b=b
#         self.c=c
#     def yigindi(self):
#         return (self.a+self.b+self.c)
#     def kopaytma(self):
#         return (self.a*self.b*self.c)
# son=uchxonali_son(3,4,5)
# print(son.yigindi())
# print(son.kopaytma())


#10-masala
# class Odam:
#     def __init__(self,yoshi,ismi,viloyati,familiyasi,jinsi):
#         self.yoshi=yoshi
#         self.ismi=ismi
#         self.viloyati=viloyati
#         self.familiyasi=familiyasi
#         self.jinsi=jinsi
#     def get_info(self):
#         return f"{self.yoshi} {self.ismi} {self.viloyati} {self.familiyasi} {self.jinsi}"
# Obod=Odam(23,'Obod','Navoiy','Ochilov','erkak')
# print(Obod.familiyasi)
# print(Obod.get_info())

#11-masala
# class Amallar:
#     def __init__(self,a,b):
#         self.a=a
#         self.b=b
#     def orta_arifmetik(self):
#         return (self.a+self.b)/2
#     def orta_geometrik(self):
#         return (self.a*self.b)**1/2
# son=Amallar(8,16)
# print(son.orta_arifmetik())
# print(son.orta_geometrik())

# son=[1,2,3,4,5,6]
# son.reverse()
# print(son)

# class Shaxs:
#     def __init__(self,ismi,familiyasi,tyili,):
#         self.ismi=ismi
#         self.familiyasi=familiyasi
#         self.tyili=tyili
#     def get_info(self):
#         return f"ismi {self.ismi} familiyasi {self.familiyasi} {self.tyili} yilda tugulgan"
#     def get_age(self,yil):
#         return yil-self.tyili
# class Talaba(Shaxs):
#     def __init__(self,ismi,familiyasi,tyili,idkarta):
#         super(Talaba, self).__init__(ismi, familiyasi, tyili)
#         self.idkarta=idkarta
#     def idkart(self):
#         return self.idkarta
#
#     def get_info(self):
#         return f"ismi {self.ismi} familiyasi {self.familiyasi} {self.tyili} yilda tugulgan  aydi kartasi {self.idkarta}"
# talaba1=Talaba('Obodjon','Ochilov',1999,'ahjs1234')
# print(talaba1.get_info())
# print(talaba1.get_age(2022))

#9-masala
# class Turtburchak:
#     def __init__(self,tomonlar=[]):
#         self.tomonlar=tomonlar
#     def yuza(self):
#         pass
# class Romb(Turtburchak):
#     def __init__(self,d1,d2):
#         self.d1=d1
#         self.d2=d2
#     def yuza(self):
#         return (self.d1*self.d2)//2
# class Kvadrat(Turtburchak):
#     def __init__(self,tomonlari=[]):
#         super().__init__(tomonlari)
#     def yuza(self):
#         return self.tomonlar[0]**2
# class Tortbur(Turtburchak):
#     def __init__(self,tomonlari):
#         super().__init__(tomonlari)
#     def yuza(self):
#         return self.tomonlar[0]*self.tomonlar[1]
# class Trapetsiya(Turtburchak):
#     def __init__(self,tomonlari,h):
#         super().__init__(tomonlari)
#         self.h=h
#     def yuza(self):
#         return (self.tomonlar[0]+self.tomonlar[1])//2*(self.h)
# tra=Trapetsiya([4,20],8)
# print(tra.yuza())
# tor=Tortbur([4,6])
# print(tor.yuza())
# kvadrat=Kvadrat([4])
# print(kvadrat.yuza())
# romb=Romb(4,6)
# print(romb.yuza())


# class SHaxs:
#     def __init__(self,ism,familiya,passport,tyili):
#         self.ism=ism
#         self.familiya=familiya
#         self.passport=passport
#         self.tyili=tyili
#     def get_info(self):
#         return f"ismi {self.ism} familiyasi {self.familiya} pasport seriyasi {self.passport} {self.tyili}-yilda tugulgan"
#
#     def get_age(self,yil):
#         return yil-self.tyili

#talaba=SHaxs('oybek','Hamrayev','AB01893',1993)
# print(talaba.get_age(2022))
# print(talaba.get_info())

# class Talaba(SHaxs):
#     def __init__(self,ism,familiya,passport,tyili,idkarta,bosqichi):
#         super().__init__(ism,familiya,passport,tyili)
#         self.idkarta=idkarta
#         self.bosqichi=1
#
#     def get_id(self):
#         return self.idkarta
#
#     def get_bosqich(self):
#         return self.bosqichi
#
#     def get_info(self):
#         return f"ismi {self.ism} familiyasi {self.familiya} pasport seriyasi {self.passport} {self.tyili}-yilda tugulgan {self.idkarta} {self.bosqichi}-bosqich talabasi"
#
#
# talaba1=Talaba('Hasan','Husanov','AC001023',1995,'kas6581',1)
# print(talaba1.get_info())
# print(talaba1.get_age(2022))

#
# class Avto:
#     Num_avto=0
#     def __init__(self,make,model,rangi,yili,narxi,km):
#         self.make=make
#         self.modeli=model
#         self.rangi=rangi
#         self.yili=yili
#         self.narxi=narxi
#         self.__km=km
#         Avto.Num_avto+=1
#     def get_km(self):
#         return self.__km
#
#     def get_make(self):
#         return self.make
#
#     def get_modeli(self):
#         return self.modeli
#
#     def get_rangi(self):
#         return self.rangi
#
#     def get_narxi(self):
#         return self.narxi
#
#     def add_km(self,km):
#
#         if km>=0:
#             self.__km+=km
#         else:
#             print("mashinaning km ni kamaytirib bolmaydi")
# avto1=Avto('GM','malibu','qora',2019,3500,1000)
# avto2=Avto('GM','Captiva','oq',2015,18000,30000)
# avto3=Avto('GM','Gentra','mokrasvalt',2020,14000,2500)
# print(avto3.Num_avto)

# print(avto1.add_km(2500))
# print(avto1.get_km())
# print(avto2.add_km(1000))
# print(avto2.get_km())


# class Universitet:
#     def __init__(self,rektori,kafedra,oqituchilar_soni,talabalar_soni,yili):
#         self.rektori=rektori
#         self.kafedra=kafedra
#         self.oqituchilar_soniga=oqituchilar_soni
#         self.talabalar_soniga=talabalar_soni
#         self.yiliga=yili
#







