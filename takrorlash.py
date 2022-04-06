# n=int(input('n='))
# k=n//10
# t=n%10
# print(k,t)
# n=int(input('n='))
# k=n//100
# print(k)
# a=int(input('a='))
# k=a>0
# print(k)
# a,b=int(input('a=')),int(input('b='))
# k=a>2 and b<=3
# print(k)
# a,b,c=int(input('a=')),int(input('b=')),int(input('c='))
# k=a<b<c
# print(k)
#9-masala a,b=int(input('a=')),int(input('b='))
# k=(a%2==1 and b%2==0) or (a%2==0 and b%2==1)
# print(k)
# a,b=int(input('a=')),int(input('b='))
# k=(a%2==0 and b%2==0) or (a%2==1 and b%2==1)
# print(k)

#34-masala
# a,b=int(input('a=')),int(input('b='))
# k=(a+b)%2==0
# print(k)

#35-masala
# n=int(input('n='))
# k=n>9 and n%2==0
# print(k)

# a,b,c=int(input('a=')),int(input('b=')),int(input('c='))
# if a>0 and b>0 and c>0:
#     print(3)
# elif (a>0 and b<0 and c<0) or (b>0 and a<0 and c<0) or (c>0 and a<0 and b<0):
#     print(1)
# elif (a>0 and b>0 and c<0) or (b>0 and c>0 and a<0) or (a>0 and c>0 and b<0):
#     print(2)

#Ikkita son berilgan. Ulardan kichigining tartib raqami chiqarilsin
# a,b=int(input('a=')),int(input('b='))
# if a>b:
#     print(2)
# else:
#     print(1)


# a,b=int(input('a=')),int(input('b='))
# if a>b:
#     print(a,b)
# else:
#     print(b,a)

# a,b=int(input('a=')),int(input('b='))
# if a!=b:
#     print(a+b)
# else:
#     print(0, 0)

# a,b=int(input('a=')),int(input('b='))
# if a!=b and (a>b):
#     print(a, a)
# elif a!=b and (a<b):
#     print(b, b)
# elif a==b:
#     print(0, 0)

# Uchta son berilgan Ular orasidan eng kichigi topilsin.
# a,b,c=int(input('a=')),int(input('b=')),int(input('c='))
# if a<b<c or a<c<b:
#     print(a)
# elif b<a<c or b<c<a:
#     print(b)
# elif c<a<b or c<b<a:
#     print(c)

# a,b,c=int(input('a=')),int(input('b=')),int(input('c='))
# if a<b<c or c<b<a:
#     print(b)
# elif b<c<a or a<c<b:
#     print(c)
# elif b<a<c or c<a<b:
#     print(a)

# a,b,c=int(input('a=')),int(input('b=')),int(input('c='))
# if a<b<c:
#     print(a, c)
# elif a<c<b:
#     print(a, b)
# elif b<c<a:
#     print(b, a)
# elif b<a<c:
#     print(b, c)
# elif c<b<a:
#     print(c, a)
# elif c<a<b:
#     print(c, b)

# k,n=int(input('k=')),int(input('n='))
# for i in range(n):
#  print(k,end=" ")

# a,b=int(input('a=')),int(input('b='))
# k=0
# for i in range(a,b+1):
#  print(i,end=" ")
#  k+=1
# print(k)

# a,b=int(input('a=')),int(input('b='))
# n=0
# for i in range(b,a,-1):
#   print(i,end=" ")
#   n+=1
# print(n)

# x=int(input('x='))
# n=int(input('n='))
# for i in range(1,n+1):
#  k=x*i
#  print(f"{i} kg ining narxi",k,"som")

# n=int(input('n='))
# x=int(input('x='))
# for i in range(12,n+1,2):
#  k=x*i//10
#  print(f"{i}kg i ning narxi",k,"som")

# a,b=int(input('a=')),int(input('b='))
# sum=0
# for i in range(a,b+1):
#  sum+=i
# print(sum)

# list=[2,3,4,5,]
# print(sum(list))

# a,b=int(input('a=')),int(input('b='))
# kop=1
# for i in range(a,b+1):
#  kop*=i
# print(kop)

# a,b=int(input('a=')),int(input('b='))
# sum=0
# for i in range(a,b+1):
#  sum+=i**2
# print(sum)

# n=int(input('n='))
# sum=0
# for i in range(1,n+1):
#  sum=sum+1/i
# print(sum)


# n=int(input('n='))
# sum=0
# for i in range(n,2*n+1):
#  sum+=i**3
# print(sum,end=" ")


# n=int(input('n='))
# sum=1
# for i in range(1,n+1):
#  sum*=1+i/10
# print(sum)

# n=int(input('n='))
# for i in range(1,n+1):
#  k=i**2
#  print(k,end=" ")


# n=int(input('n='))
# a=float(input('a='))
# print(a**n)

# a,n=int(input('a=')),int(input('n='))
# for i in range(1,n+1):
#  k=a**i
#  print(k,end=" ")

# a,n=int(input('a=')),int(input('n='))
# sum=0
# for i in range(n+1):
#  sum=sum+a**i
# print(sum)

# a,n=int(input('a=')),int(input('n='))
# sum=0
# for i in range(n+1):
#  sum=sum+(-1)**i*(a)**i
# print(sum)

# n=int(input('n='))
# fac=1
# for i in range(1,n+1):
#  fac=fac*i
# print(fac)

# from math import factorial
# print(factorial(5))

# n=int(input('n='))
# fac=1
# sum=0
# for i in range(1,n+1):
#  sum=sum+i
#  fac=fac*i
#  k=sum+fac
# print(k)

# n=int(input('n='))
# sum=1
# fac=1
# for i in range(1,n+1):
#  sum+=1/i
#  fac*=1/i
#  k=sum+fac
# print(k)

# n=int(input('n='))
# x=float(input('x='))
# sum=1
# fac=1
# for i in range(1,n+1):
#  fac=fac*i
#  sum=sum+(x**i)/fac
# print(sum)

# from  math import  factorial
# x,n=int(input('x=')),int(input('n='))
# sum=0
# for i in range(1,n+1):
#  sum=sum-((-1)**i)*((x)*(2*i-1))
# print(sum/factorial(2*1-1))
# a,b,c=int(input('a=')),int(input('b=')),int(input('c='))
# n=int(input('n='))
# for i in range(1,n+1):
#     if a>b:
#         print(b+c)
#     else:
#         print(a+c)



# mevalar={
#     'olma':12000,
#     'shaftoli':25000,
#     'anor':12000,
# }
#
# for i in mevalar.items():
#     print(f"{i} so`m")

# bozorlik=['olma','anor','behi','baliq']
# mevalar={
#     'olma':12000,
#     'shaftoli':25000,
#     'anor':12000,
# }
# for meva in mevalar:
#     if meva in bozorlik:
#         print(meva)


# for meva in  mevalar:
#     if meva not in bozorlik:
#         print(f"iltimos dokonga {meva} mahsulotidan ham olib keling")
#


# def salom_ber(ism):
#     print(f"assalomu alekum xurmatli {ism.title()}")
# salom_ber("olim")
# salom_ber("otabek")


# def yosh_hisobla(joriy_yil,tugulgan_yil,ism):
#     print(f"siz {joriy_yil-tugulgan_yil} yoshdasiz {ism}")
# yosh_hisobla(2022,1999,"Obodjon")
# yosh_hisobla(2022,2000,"Shahobiddin")


# def oraliq(min,max):
#
#     sonlar=[]
#     while min<max:
#         sonlar.append(min)
#         min+=1
#     return sonlar
# print(oraliq(0,11))
# print(oraliq(10,21))


# class Talaba:
#     def __init__(self,universiteti,kursi,ismi,familiyasi):
#         self.universiteti=universiteti
#         self.kursi=kursi
#         self.ismi=ismi
#         self.familiyasi=familiyasi
#     def get_univer(self):
#         return self.universiteti
#
#     def get_info(self):
#         info=f"{self.universiteti} da {self.kursi}-kurs talabasi {self.ismi} {self.familiyasi}"
#         return info
#
#
# class Talaba1(Talaba):
#     def __init__(self,universitet,kursi,ismi,familiyasi,pasport_seriyasi,ID_raqami):
#         super().__init__(universitet,kursi,ismi,familiyasi)
#         self.pasport_seriyasi=pasport_seriyasi
#         self.ID_raqam=ID_raqami
#
#     def id_raqam(self):
#         return self.ID_raqam
#     def get_info(self):
#         info=f"{self.universiteti} da {self.kursi}-kurs talabasi {self.ismi} {self.familiyasi} passport seriyasi, {self.pasport_seriyasi} ID raqami {self.ID_raqam}"
#         return info
#
#
#     def pass_seriya(self):
#         return self.pasport_seriyasi
# talaba1=Talaba1('TASHMI',3,"G`ofur",'Murodov','AB015987','ID256130')
# print(talaba1.get_info())


# class Avtasalon():
#     def __init__(self,markasi,karopka,rangi,yili,km):
#         self.markasi=markasi
#         self.karopka=karopka
#         self.rangi=rangi
#         self.yili=yili
#         self.__km=km
#
#
#     def mark(self):
#         return self.markasi
#
#     def karopka(self):
#         return self.karopka
#
#     def get_km(self):
#         return self.__km
#
#     def get_update(self,km):
#         if km>=0:
#             self.__km+=km
#         else:
#             return ("mashinaning km ni manfiyga utqazib bolmaydi")
#     def get_info(self):
#         info=f"mashinaning markasi {self.markasi} karopkasi esa {self.karopka} rangi {self.rangi} yili {self.yili} yurgan masofasi {self.get_km()}"
#         return info
#
# avto1=Avtasalon("GM","Avtomat","oq",2022,15000)
# print(avto1.get_update(25000))
# print(avto1.get_info())
# print(avto1.markasi)



class Talabalar:
    def __init__(self,ism,familiyasi,t_yili,viloyati,universiteti):
        self.ism=ism
        self.familiyasi=familiyasi
        self.t_yili=t_yili
        self.viloyati=viloyati
        self.universiteti=universiteti
    def get_info(self):
        info=f"mening ismim {self.ism},familiyam {self.familiyasi} {self.t_yili}-yilda tugulganman {self.viloyati} viloyatidanman men {self.universiteti} universitetida uqiyman"
        return info

talaba1=Talabalar('Obodjon','Ochilov',1999,'Navoiy','TATU')
print(talaba1.get_info())











