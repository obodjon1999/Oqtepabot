#1-masala.
# class Massiv:
#     def __init__(self,list,):
#         self.list = list
#         self.yigindilar=0
#         self.kopaytmalar = 1
#     def kopaytma(self):
#         for i in self.list:
#             self.kopaytmalar *= i
#         return self.kopaytmalar
#     def yigindi(self):
#         for i in self.list:
#             self.yigindilar += i
#         return self.yigindilar
# list=[2,4,3,5]
# A = Massiv(list)
# print(A.kopaytma())
# print(A.yigindi())

#2-masala
# from random import randint
# n = int(input('n = '))
# massiv = []
# for i in range(n):
#     massiv.append(randint(1, 12))
# print(massiv)
# class Massiv:
#     def init(self,A):
#         self.massiv = A
#     def max_index(self):
#         maxindex = 0
#         for i in range(1, len(self.massiv)):
#             if self.massiv[i]>self.massiv[maxindex]:
#                 maxindex = i
#         return maxindex
# massiva=Massiv(massiv)
# print(massiva.max_index())
#3-masala

# class Massiv:
#     def __init__(self,list):
#         self.list=list
#     def mus(self):
#         mus=[]
#         for i in range(len(self.list)):
#             if self.list[i]>0:
#                 mus.append(list[i])
#         return mus
#     def man(self):
#         man=[]
#         for i in range(len(self.list)):
#             if self.list[i]<0:
#                 man.append(list[i])
#         return man
# list=[12,2,3,4,-2,-4,-5,-6]
# son=Massiv(list)
# print(son.man())
# print(son.mus())
#.True
# class Massiv:
#     def __init__(self,massiv):
#         self.massiv=massiv
#     def mus_son(self):
#         mus=[]
#
#         for i in range(len(self.massiv)):
#             if self.massiv[i]>0:
#                 mus.append(self.massiv[i])
#             return mus
#     def man_son(self):
#         man=[]
#         for i in range(len(self.massiv)):
#             if self.massiv[i]<0:
#                 man.append(self.massiv[i])
#             return man
#
# massiv=[1,2,3,4,-1,-2,-3,-4]
# son=Massiv([1,2,3,4,-1,-2,-3,-4])
# print(son.mus_son())
# print(son.man_son())




#4-masala
# class Sonlar:
#     def __init__(self,massiv):
#         self.massiv=massiv
#     def mus(self):
#         n=0
#         for i in range(len(self.massiv)):
#             if self.massiv[i]>0:
#                 n+=1
#         return n
#     def man(self):
#         k=0
#         for i in range(len(self.massiv)):
#             if self.massiv[i]<0:
#                 k+=1
#         return k
# list=[-1,-2,-4,-8,2,3,4,6,7,9]
# son=Sonlar(list)
# print(son.mus())
# print(son.man())

#5-masala




#8-masala
# A=[8,12,5,6,9,7]
# B=[9000,1500,40000,2800,32000,55000]
# S=[4,6,1,3,8,7]
# class Supermarket:
#     def __init__(self,A,B,S):
#         self.A=A
#         self.B=B
#         self.S=S
#     def sotilgan(self):
#         summa=0
#         for i in range(len(A)):
#             summa+=self.B[i]*self.S[i]
#         return summa
#
#     def qolgani(self):
#         qolgani=[]
#         for i in range(len(A)):
#             qolgani.append(self.A[i]-self.S[i])
#         return qolgani
# market=Supermarket(A, B, S)
# print(market.sotilgan())
# print(market.qolgani())

#9-masala
# class Nodamdoira:
#     def init(self, N, K):
#         self.odam_soni = N
#         self.k = K
#
#     def odam_result(self):
#         odamlar = []
#         for i in range(1, self.odam_soni+1):
#             odamlar.append(i)
#
#         a = self.k
#         aylanish = 0
#         while len(odamlar)>1:
#             for i in range(aylanish,len(odamlar)):
#                 a-=1
#                 if a==0:
#                     print(odamlar[i], end='  ')
#                     odamlar.pop(i)
#                     a = self.k
#                     aylanish = i
#                     print(aylanish+1)
#             aylanish = 0
#
#         return odamlar[0]

#
# uyin1 = Nodamdoira(4, 3)
# print('Natija', uyin1.odam_result())


#10-masala
# class teskari_sonlar:
#     def __init__(self,massiv):
#         self.massiv=massiv
#     def teskari(self):
#         son=[]
#         for i in range(len(self.massiv)):
#             son.append(self.massiv[i])
#             son.reverse()
#
#         return son
# list=[1,2,3,4,5,6]
# tek=teskari_sonlar(list)
# print(tek.teskari())









# class Fan:
#     def __init__(self,nomi,uqituvchisi,talaba):
#         self.nomi=nomi
#         self.uqituvchisi=uqituvchisi
#         self.talaba=talaba
# class Talaba:
#     def __init__(self,first_name,last_name,year,manzil):
#         self.first_name=first_name
#         self.last_name=last_name
#         self.year=year
#         self.manzil=manzil
# class Manzil:
#     def __init__(self,viloyati,tumani,mahallasi,uy_nomeri):
#         self.viloyati=viloyati
#         self.tumani=tumani
#         self.mahallasi=mahallasi
#         self.uy_nomeri=uy_nomeri
# manzil1=Manzil("navoiy",'nurota','istiqlol','123A_uy')
# talaba1=Talaba('obodjon','ochilov',1999,manzil1)
# matem=Fan('ona_tilki','Olimov',talaba1)
# print(matem.talaba.manzil.viloyati)



# class Talaba:
#     """Talaba nomli klass yaratamiz"""
#
#     def __init__(self, ism, familiya, tyil):
#         """Talabaning xususiyatlari"""
#         self.ism = ism
#         self.familiya = familiya
#         self.tyil = tyil
#     def ismi(self):
#         return self.ism
#     def tanishtir(self):
#         print(f"Ismim {self.ism} {self.familiya}. {self.tyil} yilda tu'gilganman")
#     def get_info(self):
#         print(f"Salom {self.ism}")
#
# talaba4 = Talaba("Hasan","Akbarov",2004)
# print(talaba4.get_info())

#masala
# class Talaba:
#     def __init__(self,isim,familiya,tyil):
#         self.isim=isim
#         self.familiya=familiya
#         self.tyil=tyil
#     def otchestva(self):
#         return self.familiya
#     def name(self):
#         return self.isim
#     def toliq(self):
#         print(f"mening ismim {self.isim}  familiyam {self.familiya} {self.tyil}-yilda tugulganman")
# talaba1=Talaba('Obod','Ochilov','2002')
# print(talaba1.toliq())
# print(talaba1.name())

#masala
# class Talaba:
#     """Talaba nomli klass yaratamiz"""
#
#     def __init__(self, ism, familiya, tyil):
#         """Talabaning xususiyatlari"""
#         self.ism = ism
#         self.familiya = familiya
#         self.tyil = tyil
#
#     def get_name(self):
#         """Talabaning ismini qaytaradi"""
#         return self.ism
#
#     def get_lastname(self):
#         """Talabaning familiyasini qaytaradi"""
#         return self.familiya
#
#     def get_fullname(self):
#         """Talabaning ism-familiyasini qaytaradi"""
#         return f"{self.ism} {self.familiya}"
#
#     def tanishtir(self):
#         print(f"Ismim {self.ism} {self.familiya}. {self.tyil} yilda tu'gilganman")
#
#
# talaba1 = Talaba("Alijon", "Valiyev", 2000)
# print(talaba1.get_fullname())


#masala
# class Talaba:
#     """Talaba nomli klass yaratamiz"""
#
#     def __init__(self, ism, familiya, tyil):
#         """Talabaning xususiyatlari"""
#         self.ism = ism
#         self.familiya = familiya
#         self.tyil = tyil
#
#     def get_name(self):
#         """Talabaning ismini qaytaradi"""
#         return self.ism
#
#     def get_lastname(self):
#         """Talabaning familiyasini qaytaradi"""
#         return self.familiya
#
#     def get_fullname(self):
#         """Talabaning ism-familiyasini qaytaradi"""
#         return f"{self.ism} {self.familiya}"
#
#     def get_age(self, yil):
#         """Talabaning yoshini qaytaradi"""
#         return yil - self.tyil
#
#     def tanishtir(self):
#         print(f"Ismim {self.ism} {self.familiya}. {self.tyil} yilda tu'gilganman")
# talaba1=Talaba('Jabbor','jalolov',2002)
# print(talaba1.get_age(2022))

#masala
# class Inson:
#     def __init__(self,viloyati,tumani,qishologi,tyil):
#         self.viloyati=viloyati
#         self.tumani=tumani
#         self.qishlogi=qishologi
#         self.tyili=tyil
#     def region(self):
#         return self.viloyati
#     def discrit(self):
#         return self.tumani
#     def village(self):
#         return self.qishlogi
#     def get_age(self,yil):
#         return yil-self.tyili
#     def uzgar(self,year):
#         self.tyili=year
#     def year(self):
#         return self.tyili
#     def tanishtir(self):
#         print(f"viloyati {self.viloyati}   tumani {self.tumani}   qishlogi {self.qishlogi}   {self.tyili}-yilda tugilgan")
# Elyor=Inson('jizzax','Dashtobod','zarb',1998)
# (Elyor.tanishtir())
# print(Elyor.get_age(2022))
# (Elyor.uzgar(1995))
# print(Elyor.year())

#masala.
# class Talaba:
#     """Talaba nomli klass yaratamiz"""
#
#     def __init__(self, ism, familiya, tyil):
#         """Talabaning xususiyatlari"""
#         self.ism = ism
#         self.familiya = familiya
#         self.tyil = tyil
#         self.bosqich = 1
#
#     def get_info(self):
#         """Talaba haqida ma'lumot"""
#         return f"{self.ism} {self.familiya}. {self.bosqich}-bosqich talabasi "
#
#     def set_bosqich(self, newbosqich):
#         """Talabaning kursini yangilovchi metod"""
#         self.bosqich = newbosqich
# talaba1=Talaba('Obodjon','Ochilov',1999)
# print(talaba1.set_bosqich(3))
# print(talaba1.get_info())

#8-masala.
# A=[5,6,12,8,9,18]
# B=[6000,9000,28000,35000,40000,58000]
# S=[3,1,0,7,9,1]
# class Supermarket:
#     def __init__(self,A,B,S):
#         self.A=A
#         self.B=B
#         self.S=S
#         pass
#     def kunlik_savdo(self,):
#         summa=0
#         for i in range(len(self.A)):
#             summa+=self.B[i]*self.S[i]
#         return summa
#     def qoldiq(self):
#         qolgani=[]
#         for i in range(len(self.A)):
#             qolgani.append(self.A[i]-self.S[i])
#         return qolgani
# market=Supermarket(A,B,S)
# print(market.qoldiq())
# print(market.kunlik_savdo())


# masalalar
# class Salon:
#     def __init__(self,markasi,narxi,yili,rangi,ykm):
#         self.markasi=markasi
#         self.narxi=narxi
#         self.yili=yili
#         self.rangi=rangi
#         self.ykm=ykm
#     def marka(self):
#         return self.markasi
#     def sum(self):
#         return self.narxi
#     def year(self):
#         return self.yili
#     def __mul__(self,other):
#         return self.ykm*other.ykm
#     def __truediv__(self, other):
#         return self.yili/other.yili
#     def __mul__(self, other):
#         return self.narxi*other.narxi
#     def __mod__(self, other):
#         return self.narxi%other.narxi
#     def __eq__(self, other):
#         return self.narxi==other.narxi
#     def toliqmalum(self):
#         print(f'yangi {self.markasi} narxi {self.narxi}  rangi {self.rangi}')
# mashina1=Salon('cobalt',10000,2022,'sariq',250)
# mashina2=Salon('Gentra',14000,2022,'oq',300)
# mashina3=Salon('nexia2',7000,2022,'qora',400)
# # print(mashina1.toliqmalum())
# # print(mashina2.toliqmalum())
# # print(mashina3.toliqmalum())
# # print(mashina3*mashina2)
# # print(mashina1*mashina3)
# # print(mashina1/mashina3)
# # print(mashina3%mashina2)
# print(mashina1==mashina2)






