#2-masala.
# class Complex:
#     def __init__(self,son,complex):
#         self.son=son
#         self.complex=complex
#     def __add__(self, other):
#         son=self.son+other.son
#         complex=self.complex+other.complex
#         if complex>0:
#             return f"{son}+{complex}i"
#         else:
#             return f"{son}{complex}i"
#     def __sub__(self, other):
#         son=self.son-other.son
#         complex=self.complex-other.complex
#         if complex>0:
#             return f"{son}+{complex}i"
#         else:
#             return f"{son}{complex}i"
#     def __mul__(self, other):
#         son=self.son*other.son-self.complex*other.complex
#         complex=self.son*other.complex+self.complex*other.son
#         if complex>0:
#             return f"{son}+{complex}i"
#         else:
#             return f"{son}{complex}i"
# complex1=Complex(3,2)
# complex2=Complex(7,12)
# print(complex1+complex2)
# print(complex1-complex2)
# print(complex1*complex2)

#3-masala
# import random
# class Matritsa:
#     def __init__(self, n):
#         self.n = n
#
#     def create_mat(self):
#         self.matritsa = []
#         for i in range(self.n):
#             res = []
#             for j in range(self.n):
#                 res.append(random.randint(0, 1))
#             self.matritsa.append(res)
#         return self.matritsa
#
#     def max_element(self):
#         maximal = self.matritsa[0][0]
#         for i in self.matritsa:
#             if max(i)>maximal:
#                 maximal=max(i)
#         return maximal
#     def min_element(self):
#         minimal = self.matritsa[0][0]
#         for i in self.matritsa:
#             if max(i)>minimal:
#                 minimal=min(i)
#         return minimal
#
#     def tranponer(self):
#         for i in range(self.n):
#             for j in range(self.n):
#                 print(self.matritsa[i][j], end='  ')
#             print('')
#     def simmetrik(self):
#         for i in range(self.n):
#             for j in range(i+1, self.n):
#                 if self.matritsa[i][j]!=self.matritsa[j][i]:
#                     return False
#         return True
# matritsa = Matritsa(int(input('n = ')))
# print(matritsa.create_mat())
# matritsa.tranponer()
# print(matritsa.simmetrik())
# print(matritsa.max_element())
# print(matritsa.min_element()

#6-masala
# class Kitob:
#     def __init__(self, nomi, aftor, yili, beti):
#         self.nomi = nomi
#         self.beti = beti
#         self.aftor = aftor
#         self.yili = yili
#
#     def __str__(self):
#         return f"{self.nomi}"
#
#
# class Kutubxona:
#     def __init__(self, kitoblar=[]):
#         self.kitoblar = kitoblar
#
#     def add_book(self, kitob):
#         if isinstance(kitob, Kitob):
#             self.kitoblar.append(kitob)
#         else:
#             print("Siz kiritayotgan kitob Kitob sinifiga tegishli emas")
#
#     def remove_book(self, kitob):
#         if isinstance(kitob, Kitob):
#             if kitob in self.kitoblar:
#                 self.kitoblar.remove(kitob)
#             else:
#                 print("Siz chiqarmoqchi bo'lgan kitob kutubxobnada mavjud emas")
#         else:
#             print("Siz kiritayotgan kitob Kitob sinifiga tegishli emas")
#
#     def search_year(self, year):
#         result = []
#         for i in self.kitoblar:
#             if i.yili == year:
#                 result.append(i.nomi)
#         return result
#
#     def search(self, name):
#         result = []
#
#         for i in self.kitoblar:
#             if name in i.nomi:
#                 result.append(i.nomi)
#         return result
#
#
# kitob1 = Kitob('Қўрқма', 'Жавлон Жовлиев', 2005, 245)
# kitob2 = Kitob('Диққат: Чалғитувчи дунёда муваффақият сирлари', 'Жавлон Жовлиев', 2009, 345)
# kitob3 = Kitob('Бепарволикнинг нозик санъати', 'Марк Мэнсон', 2012, 543)
# kitob4 = Kitob('Бепарволикнинг нозик санъати', 'Марк Мэнсон', 2009, 543)
# kitob5 = Kitob('Бепарволикнинг нозик санъати', 'Марк Мэнсон', 2012, 543)
#
# milliy_kutubxona = Kutubxona()
#
# milliy_kutubxona.add_book(kitob1)
# milliy_kutubxona.add_book(kitob2)
# milliy_kutubxona.add_book(kitob3)
# milliy_kutubxona.add_book(kitob4)
# milliy_kutubxona.add_book(kitob5)
#
# print(milliy_kutubxona.search_year(2009))
# print(milliy_kutubxona.search('а'))
#



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

# class Massiv:
#     def __init__(self,A,n):
#         self.massiv=A
#         self.n=n
#     def up_n(self):
#         massiv1=self.massiv[-self.n:]
#         massiv2=self.massiv[:-self.n]
#         return massiv1+massiv2
# massiv=Massiv([0,1,2,3,4,5,6,7,8],3)
# print(massiv.up_n())
# n=int(input('n='))
# list=[]
# for i in range(1,n+1):
#     list.append(i)
# print(list)


