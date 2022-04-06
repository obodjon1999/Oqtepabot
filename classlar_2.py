#1-masala
# class Misollar:
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
# son=Misollar(10,4)
# print(son.yigindi())
# print((son.ayirma()))
# print((son.kopaytma()))
# print((son.bolinma()))

#2-masala
# class Uchburchak:
#     def __init__(self,a,b,c):
#         self.a=a
#         self.b=b
#         self.c=c
#     def uchyuz(self):
#         return (self.a*self.b)/2
#     def uchper(self):
#         return (self.a+self.b+self.c)
# son=Uchburchak(3,4,5)
# print(son.uchyuz())
# print(son.uchper())

#3-masala.
# class max_min:
#     def __init__(self,a,b):
#         self.a=a
#         self.b=b
#     def katta(self):
#         if self.a>self.b:
#             return (self.a)
#         else:
#             return (self.b)
#     def kichchik(self):
#         if self.b>self.a:
#             return (self.a)
#         else:
#             return (self.b)
# son=max_min(12,20)
# print(son.katta())
# print(son.kichchik())


#5-masala
# n=int(input('n='))
# sum=0
# kop=1
# for i in range(1,n+1):
#     sum+=i
#     kop*=i
# print(sum)
# print(kop)

#6-masala.. 1·1+2·2+3·3+...+n·n yig’indini hisoblang.
# n=int(input('n='))
# sum=0
# for i in range(1,n+1):
#     sum+=i**2
# print(sum)

#7-masala.7. 1·n+2·(n ‒1)+3·(n ‒2)+...+n·1 yig’indini hisoblang.
# n=int(input('n='))
# sum=0
# for i in range(0,n+1):
#     sum+=(i+1)*(n-i)
# print(sum)

#8-masala
# n=int(input('n='))
# f1=int(input('f1='))
# f2=int(input('f2='))
# list=[]
# for i in range(n):
#     f=f1+f2
#     f1=f2
#     f2=f
#     list.append(f)
# print(list)


#9. Berilgan K soniga karrali bo’lgan birinchi N ta sonni
#toping.
# k=int(input('k='))
# n=int(input('n='))
# son=0
# for i in range(1,n+1):
#     if k%i==0:
#         son+=1
# print(son)
#10-masala. Berilgan K soniga qoldiqsiz bo’linadigan birinchi N
#ta sonni toping.
# k=int(input('k='))
# n=int(input('n='))
# son=0
# for i in range(1,n+1):
#     if k%i==0:
#         son+=1
# print(son)

#11-masala



















