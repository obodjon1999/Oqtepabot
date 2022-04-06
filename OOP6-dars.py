# class  PROGRESSIYA:
#     def __init__(self,a1,d,n):
#         self.a1=a1
#         self.d=d
#         self.n=n
#     def creat_progress(self):
#         pass
#
#     def sum_progress(self):
#         pass
# class Arifm_Progres(PROGRESSIYA):
#     def __init__(self,a1,d,n):
#         super().__init__(a1,d,n)
#     def creat_progress(self):
#         self.progress=[]
#         for i in range(self.n):
#             self.progress.append(self.a1+i*self.d)
#         return self.progress
#     def sum_progress(self):
#         return sum(self.progress)
# class Geom_Progres(PROGRESSIYA):
#     def __init__(self,a1,d,n):
#         super().__init__(a1,d,n)
#     def creat_progress(self):
#         self.list=[]
#         for i in range(1,self.n):
#             self.list.append(self.a1*i*self.d)
#         return self.list
#     def sum_progress(self):
#         return sum(self.list)
# geom=Geom_Progres(3,2,6)
# print(geom.creat_progress())
# print(geom.sum_progress())
# arif=Arifm_Progres(4,2,9)
# print(arif.creat_progress())
# print(arif.sum_progress())

#2-masala
# class TURTBURCHAK:
#     def __init__(self,tomonlari=[]):
#         self.tomonlari=tomonlari
#     def YUZA(self):
#         pass
# class Romb(TURTBURCHAK):
#     def __init__(self,d1,d2):
#         super().__init__()
#         self.d1=d1
#         self.d2=d2
#     def YUZA(self):
#         return (self.d1*self.d2)//2
# class Kvadrat(TURTBURCHAK):
#     def __init__(self,tomonlari):
#         super().__init__(tomonlari)
#     def YUZA(self):
#         return self.tomonlari[0]**(2)
# class Tortburchak(TURTBURCHAK):
#     def __init__(self,tomonlar):
#         super().__init__(tomonlar)
#     def YUZA(self):
#         return self.tomonlari[0]*self.tomonlari[1]
#
#
# class TRAPETSIYA(TURTBURCHAK):
#     def __init__(self,tomonlari,h):
#         super().__init__(tomonlari)
#         self.h=h
#     def YUZA(self):
#         return (self.tomonlari[0]+self.tomonlari[1])*self.h//2
# class PARALLELOGRAM(TURTBURCHAK):
#     def __init__(self,tomonlari,sina):
#         super().__init__(tomonlari)
#         self.sina=sina
#     def YUZA(self):
#         return ((self.tomonlari[0])*(self.tomonlari[1])*(self.sina))//2
# parel=PARALLELOGRAM([8,6],1/2)
# print(parel.YUZA())
# trap=TRAPETSIYA([8,12],4)
# print(trap.YUZA())
# turtbur=Tortburchak([4,6])
# print(turtbur.YUZA())
# kvadrat=Kvadrat([6])
# print(kvadrat.YUZA())
# romb=Romb(4,5)
# print(romb.YUZA())

#3-masala
# class KVADRAT:
#     def __init__(self,a,b,c):
#         self.a=a
#         self.b=b
#         self.c=c
#     def diskrm(self):
#         pass
#
#     def KV_ILDIZ(self):
#         pass
#
# class BIKVADRAT(KVADRAT):
#     def __init__(self,a,b,c,):
#         super().__init__(a,b,c)
#
#     def KV_ILDIZ(self):
#         D=(self.b**2-4*self.a*self.c)/2*self.a
#         return D
# sonlar=BIKVADRAT(4,3,4)
# print(sonlar.KV_ILDIZ())











