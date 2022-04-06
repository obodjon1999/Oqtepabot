#1-masala
# Lug’atni qiymatlari bo’yicha saralang.
# thislist={"brand":"ford",
#           "modeli":"mustang",
#           "yili":1996
# }
# print(thislist.values())
#1-masala
# thislist={"brand":"ford",
#           "modeli":"mustang",
#           "yili":1996,
# }
# for i in thislist.values():
#     print(i)

#2-masala
#lugatni kalitlar bo’yicha saralang
# thislist={"brand":"ford",
#           "modeli":"mustang",
#           "yili":1996,
# }
# for i in thislist.keys():
#     print(i)
#
#3. Lug’atga yangi kalit va qiymat qo’shing.
# this={"markasi":"inamarka",
#       "rangi":"qora",
#       "yili":2002
# }
# this["narxi"]="1200$"
# print(this)

#3
# this={"markasi":"inamarka",
#       "rangi":"qora",
#       "yili":2002
# }
# this["davlati"]="angilya"
# print(this)

#4-masala
#Berilgan uchta lug’atni birlashtiruvchi dastur tuzung
# a={"ism":"Obod",
#    "familiya":"Ochilov"
# }
# b={"yil":1999,
#    "boyi":175
# }
# c={"student":"TATU",
#    "work":"zako"
# }
# a.update(b)
# a.update(c)
# print(a)

#5-masalaBerilgan qiymati Lug’atda bor yoki yo’qligini tekshiruvchi funksiya yarating.
# fruit={"olma":12000,
#        "banan":18000,
#        "uzum":"8000"
# }
# a=input('a ni kirit')
# if a in fruit.values():
#     print("siz kiritgan qiymat mevalar royhatida bor")
# else:
#     print('siz kiritgan qiymat mevalar royhatida yoq')

#6. n butun soni berilgan. {1: 1, 2: 4, 3: 9, …, n: n2} ko’rinishidagi
#lug’at hosil qiling.
# n=int(input('n='))
# new={}
# for i in range(1,n+1):
#     new[i]=i**2
# print(new)

#7-masala
#Berilgan lug’atdagi qiymatlar yig’indisini hisoblang.
# n=int(input('n='))
# lis={}
# for i in range(1,n+1):
#     lis[i]=i**2
# print(sum(lis.values()))


#7-masala
# n=int(input('n='))
# lis={}
# for i in range(1,n+1):
#     lis[i]=i**2
#     sum=0
# for i in lis.values():
#     sum+=i
# print(sum)

#8-masala
#lug’atdan berilgan kalit bo’yicha qiymati o’chiradigan dastur tuzing.
# n=int(input('n='))
# k=int(input('k-sonni kirit='))
# lis={}
# for i in range(1,n+1):
#     lis[i]=i**2
# del lis[k]
# print(lis)
# from math import pi
# f=open('juftlar','w')
# f.write(str(pi))







