# 1-masala
# fayl_nomi=input('faylnominikiriting')
# if '//'or '*' or '?' or '<' or '>' or '|' or '/' in fayl_nomi:
#     print(False)
# else:
#     f=open(fayl_nomi,'a')
# 1-masala
# fayl=input('fayl nomini kiriting=')
# try:
#     fayl=open(fayl, 'a')
#     fayl.write('mening oilam')
#
#     fayl.close()
#
# except Exception as e:
#     print(e)
#     print(False)


# 2-masala
# 2. s fayl nomi va n(n>1) butun soni berilgan. Butun son joylashadigan s nomli fayl tuzilsin va
# unga n gacha bo‘lgan juft musbat sonlar ketma-ketligi yozilsin. (n ham kiradi )
# s=input('fayl nomini kiriting')
# n=int(input('n='))
# try:
#     f=open(s,'w')
#     for i in range(2,n+1,2):
#         f.write(str(i)+' ')
#
#
# except Exception as e:
#     print(e)
#     print(False)


# 3. s fayl nomi va haqiqiy a, d sonlari berilgan. Tashqi faylga 1-hadi a ga ayirmasi d ga teng bo‘lgan
# arifmetik progressiyaning dastlabki 10 ta hadining qiymatlari yozilsin
# s,a,d=input('faylni kiriiting'),int(input('a=')),int(input('d='))
# try:
#     fayl=open(s, 'w')
#     for i in range(a,a+9*d+1,d):
#         fayl.write(str(i)+' ')
#
# except Exception as e:
#     print(e)
#     print(False)

# 4-masala
# s0,s1,s2,s3=input('s0'),input('s1'),input('s2'),input('s3')
# k=0
# try:
#     f0=open(s0,'a')
#     f1=open(s1,'a')
#     f2=open(s2,'a')
#     f3=open(s3,'a')
#     f0.write()

# 5-masala
# 5. Butun sonli fayl nomi berilgan. Fayldagi elementlar soni topilsin. Agar bunday nomdagi fayl
# topilmasa – 1 chiqarilsin.
# s=input('sonni kiriting')
# try:
#     f=open(s,'w')
#     f.write('obodjon')
#     list=[]
#
#     for x in f:
#         list.append(x)
#     print(len(list[0]))
# except Exception as e:
#     print(e)
#     print(-1)

#6-masala
# k=int(input('k='))
# name=input('fayl nommini kiriting')
# try:
#     f=open(name,'w')
#     for i in range(10):
#         f.write(str(i))
#     f.close()
# except Exception as e:
#     print(e)

# 6-masala
# k=int(input('k='))
# f = open('name', "r")
# for x in f:
#     sonlar = x
# bol = True
# for i in range(len(sonlar)):
#     if k==i:
#         print(sonlar[i])
#         bol = False
# if bol:
#     print(-1)


# 7-masala

# f=open('name','r')
# list=[]
# for x in f:
#     sonlar=x
# for i in sonlar:
#     list.append(i)
# print(list)
# bool=True
# while list:
#     if bool:
#         print(list[0], end=" ")
#         print(list[1], end=" ")
#         list.pop(0)
#         list.pop(0)
#         bool=False
#     else:
#         print(list[-1],end=" ")
#         print(list[-2],end=" ")
#         list.pop(-1)
#         list.pop(-1)
#         bool=True


# # f = open("salom", "a")
# # f.write("salomdunyo")
# # f.close()
#
# f = open("salom", "r")
# list = []
# for x in f:
#     name = x
# for i in name:
#     list.append(i)
# bol = True
# while list:
#     if bol:
#         print(list[0], end=" ")
#         print(list[1], end=" ")
#         list.pop(0)
#         list.pop(0)
#         bol = False
#     else:
#         print(list[-2], end=" ")
#         print(list[-1], end=" ")
#         list.pop()
#         list.pop()
#         bol = True
#
# 8-masala
# f=open('salom','r')
# for x in f:
#     string=x
# f=open("nom","a")
# f.write(string[0])
# f.write(string[-1])
# f.close()
# f = open("nom","r")
# print(f.read())

#9-masala
# s=input('fayl nomini kiriting')
# f=open(s,'r')
# for x in f:
#     string=x
# f=open('salom','w')
# for i in range(len(string)):
#     f.write(string[0])
#     f.write(string[-1])
# f=open('salom','r')
# print(f.read())

# 10-masala
# f = open('maktab', 'r')
# for x in f:
#     string = x
# f = open('men', 'w')
# for i in range(len(string) - 1, -1, -1):
#     f.write((string[i]))
# f.close()
# f = open('men', 'r')
# print(f.read())

# 2. s fayl nomi va n(n>1) butun soni berilgan. Butun son joylashadigan s nomli fayl tuzilsin va
# unga n gacha bo‘lgan juft musbat sonlar ketma-ketligi yozilsin. (n ham kiradi )
# s=input('fayl nomini kirit')
# n=int(input('n='))
# try:
#     f=open(s,'a')
#     for i in range(n):
#         f.write(str(i))
#
#     f=open(s,'r')
#     print(f.read())
# except Exception as e:
#     print(e)
#     print(False)
#
# f=open('salom','r')
# print(f.read())


#11-masala
# f=open('maktab','w')
# for i in range(15):
#     f.write(str(i))
# f=open('maktab','r')
# for x in f:
#     string=x
# juft=[]
# toq=[]
# for i in string:
#     if int(i)%2==0:
#         juft.append(str(i))
#     else:
#         toq.append(str(i))
# f=open('juftlar','a')
# for i in juft:
#     f.write(i)
# f.close()
# f=open('toqlar','a')
# for i in toq:
#     f.write(i)
# f.close()

#12-misol
# f=open('nom','w')
# for i in range(14):
#     f.write(str(i))
# f=open('nom','r')
# for x in f:
#     string=x
# juft=[]
# toq=[]
# for i in string:
#     if int(i)%2==0:
#         juft.append(str(i))
#     else:
#         toq.append(str(i))
# f=open('juftlar','a')
# for i in juft:
#     f.write(i)
# f.close()
# f=open('toqlar','a')
# for i in toq:
#     f.write(i)
#
# f.close()

#13-masala
# f=open('maktab','w')
# for i in range(10):
#     f.write(str(i))
# f=open('maktab','r')
# for x in f:
#     string=x

# k=int(input('k='))
# f=open('toqlar','r')
# for x in f:
#     string=x
# bool=True
# for i in range(len(string)):
#
#      if k==i:
#         print(string[i])
#         bool=False
#
# if bool:
#     print(-1)
#
#
#13-masala

# f=open('maktab','w')
# for i in range(-5,5):
#     f.write((str(i)))
# f=open('maktab','r')
# for x in f:
#     string=x
# mus=[]
# man=[]
# for i in range(len(string)):
#     if int(i)>0:
#         mus.append(i)
#     else:
#         man.append(i)
# f=open('musbat','a')
# for i in mus:
#     f.write(i)
# f.close()
# f=open('manfiy','a')
# for i in man:
#     f.write(i)
#     f.close()

#14-masala
# list=[]
# f=open('maktab','w')
# for i in range(10):
#     f.write(str(i))
# f=open('maktab','r')
# for x in f:
#     string=x
# list=string.split(' ')
# yigindi=0
# for i in range(len(list)):
#     yigindi+=float(i)
# orta=yigindi/len(list)
# print(orta)

#13-masala
# list=[]
# f=open('maktab','r')
# for x in f:
#     string=x
# list=string.split(' ')
# mus=[]
# man=[]
# for i in list:
#     if float(i)>0:
#         mus.append(i)
#     else:
#         man.append(i)
# f=open('musbatlar','a')
# for i in mus:
#     f.write(i)
# f=open('manfiylar','a')
# for i in man:
#     f.write(i)
#-14-masala
# list=[]
# f=open('maktab','r')
# for x in f:
#     string=x
# list=string.split()
# sum=0
# for i in list:
#     sum+=int(i)
#     otraa=sum//len(list)
# print(otraa)
#
#15-masala
# list=[]
# f=open('maktab','r')
# for x in f:
#     string=x
# list=string.split()
# sum=0
# for i in range(0,len(list),2):
#     sum+=(i)
# print(sum,)

#16-masala
# f=open('yoq','w')
# for i in range(1,4):
#     f.write(str(i))
# f.close()
#
#
# list=[]
# f=open('maktab','r')
# for x in f:
#     string=x
# f=open('name','w')
# for i in range(len(string)):
#     list.append(str(i))
# print(list)




















