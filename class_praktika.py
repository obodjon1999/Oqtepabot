# class Avto:
#     def __init__(self,make,model,rang,yil,narx):
#         self.make=make
#         self.model=model
#         self.ranbg=rang
#         self.yil=yil
#         self.narxi=narx
#     def __repr__(self):
#         return f'Avto:{self.make}  {self.model}'
#     def __eq__(self, other):
#         return self.yil==other.yil
#     def __ge__(self, other):
#         return self.narxi>=other.narxi
# class Avtosalon:
#     def __init__(self,name):
#         self.name=name
#         avtolar=[]
#     def __repr__(self):
#         return f"Avtosalon:{self.name} avtosaloni"
# salon1=Avtosalon('Maxavto')
# print(salon1)
#
# avto1=Avto('Gm','Malibu','oq',2000,40000)
# avto2=Avto('Gm','lacetti','qora',1998,20000)
# avto3=Avto('GM','captiva','oq',2022,35000)
# print(avto1==avto2)
# print(avto2>=avto3)

# class Shaxs:
#     def __init__(self,ism,familya,pasport,tyil):
#         self.ism=ism
#         self.familya=familya
#         self.pasport=pasport
#         self.tyil=tyil
#     def get_info(self):
#         print(f"{self.ism} {self.familya} ,{self.pasport}, {self.tyil} ")
#     def get_age(self,yil):
#         return yil-self.tyil
# inson=Shaxs('olim','karimov','AB0074',1999)
# # print(inson.get_info())
# class Talaba(Shaxs):
#     def __init__(self,ism,familya,pasport,tyil,manzil):
#         super().__init__(ism,familya, pasport, tyil)
#         self.manzil=manzil
# talaba=Talaba('Abu','Qudratov','CD1234007',1945,'navoiy')
# (talaba.get_info())
# print(talaba.get_age(2022))


#n-masala
# class Oila:
#     def __init__(self,otasi,onasi,tyili,kasbi):
#         self.otasi=otasi
#         self.onasi=onasi
#
#         self.tyili=tyili
#         self.kasbi=kasbi
#     def get_info(self):
#         return f" otasini ismi {self.otasi}, onasini ismi {self.onasi}, kasblari {self.kasbi}"
#     def get_age(self,yil):
#         return yil-self.tyili
# inson=Oila('Akmal','Munira',1973,'shifokor')
# #print(inson.get_info())
# #print(inson.get_age(2022))
#
# class Oila1(Oila):
#     def __init__(self,otasi,onasi,tyili,kasbi,telnomi):
#         super(Oila1, self).__init__(otasi,onasi, tyili, kasbi,)
#         self.telnomi=telnomi
# inson1=Oila1('Nodir','Mohira',1977,'shafyor','933130742')
# # print(inson1.get_info())
# print(inson1.telnomi)
# # print(inson1.get_age(2024))



#masala
# from uuid import uuid4
# class Avto:
#
#     def __init__(self,make,model,rang,yil,narx,km=0):
#         self.make=make
#         self.model=model
#         self.rang=rang
#         self.yil=yil
#         self.narx=narx
#         self.__km=km
#         self.__id=uuid4()
#     def car__km(self):
#         return self.__km
#     def add_km(self,km):
#         if km>=0:
#             self.__km+=km
#         else:
#             print( "mashinaning km ni kamaytirib bolmaydi")
#
#     def __repr__(self):
#         return f"zavodi {self.make} modeli {self.model} rangi esa {self.rang} yili {self.yil}  narxi {self.narx} yurgan yoli esa {self.add_km(2000)}"
#
# avto1=Avto('GM','Malibu','qora',2022,2000,1000)
# avto2=Avto('GM','Gentra','oq',2019,12000,2000)
# avto3=Avto('GM','lacetti','qora',2018,9000,25000
# print(avto3.car__km())

#oop 3-top.5-masala
# class Massiv:
#     def __init__(self,A,n):
#         self.masssiv=A
#         self.n=n
#     def up_n(self):
#         massiv1=self.masssiv[-self.n:]
#         massiv2=self.masssiv[:-self.n]
#         return massiv1+massiv2
# massiv=Massiv([1,2,3,4,5,6,7,8],3)
# print(massiv.up_n())


#n-masala takrorlash
# list=[1,2,3,4,5,6,7,8]
# print(list[3:])
# print(list[:3])

#oop3-dan 6-si
# class Massiv:
#     def __init__(self,A,n):
#         self.massiv=A
#         self.n=n
#     def up_n(self):
#         massiv1=self.massiv[self.n:]
#         massiv2=self.massiv[:self.n]
#         return massiv1+massiv2
# massiv=Massiv([1,2,3,4,5,6,7,8,],3)
# print(massiv.up_n())














