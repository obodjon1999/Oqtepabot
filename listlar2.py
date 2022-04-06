# 1. n (n>0) butun son berilgan. Dastlabki n ta musbat toq sonlarni saqlaydigan n o‘lchamli butun
#sonli massiv tashkil etilsin
# n=int(input('n='))
# list=[]
# for i in range(n):
#     a=int(input(f'{i+1}-sonni kiriting='))
#     list.append(a)
# print(list)
#2-masala
# n=int(input('n='))
# listlar=[]
# a=int(input('a='))
# for i in range(1,n+1):
#     k=a**i
#     listlar.append(k)
# print(listlar)
#
#3-masala
# n=int(input('n='))
# a=int(input('a='))
# d=int(input('d='))
# yigindi=(list(range(a,n*d,d)))
# print(yigindi)
#4-masala
# n=int(input('n='))
# b=int(input('b='))
# q=int(input('q='))
# sum=b
# listlar=[]
# for i in range(n):
#     listlar.append(sum)
#     sum*=q
# print(listlar)
#5-masala
# n=int(input('n='))
# f1=int(input('f1='))
# f2=int(input('f2='))
# listlar=[]
# listlar.append(f1)
# listlar.append(f2)
# for i in range(n-2):
#     f=f1+f2
#     f1=f2
#     f2=f
#     listlar.append(f)
# print(listlar)
#6-masala
# n=int(input('n='))
# a=int(input('a='))
# b=int(input('b='))
# sum=3+4
# listlar=[]
# listlar.append(a)
# listlar.append(b)
# for i in range(n-2):
#     sum*=2
#     listlar.append(sum)
# print(listlar)

#7-masala
# n=int(input('n='))
# listlar=[]
# for i in range(n):
#     a=int(input(f'{i+1}-sonni kiriting'))
#     listlar.append(a)
# print(listlar)
# newlist=[]
# for i in range(len(listlar)):
#     newlist.append(listlar[i])
#     newlist.reverse()
# print(newlist)

#8-masala
# n=int(input('n='))
# listlar=[]
# for i in  range(n):
#     a=int(input(f'{i+1}-sonni kiriting'))
#     listlar.append(a)
# print(listlar)
# newlist=[]
# son=0
# for i in range(2,len(listlar)+2,2):
#     newlist.append(i)
#     newlist.sort(reverse=True)
#     son+=1
# print(newlist)
# print(son)

#9-masala
# n=int(input('n='))
# list=[]
# for i in range(n):
#     a=int(input(f'{i+1}-sonni kiriting'))
#     list.append(a)
# print(list)
# newlist=[]
# son=0
# for i in list:
#     if i%2==1:
#         newlist.append(i)
#         son+=1
# print(newlist)
# print(son)

#10-masala
# n=int(input('n='))
# list=[]
# for i in range(n):
#     a=int(input(f'{i+1}-sonni kiriting='))
#     list.append(a)
# print(list)
# juft=[]
# toq=[]
# for i in range(0,len(list)):
#     if list[i]%2==0:
#         juft.append(i)
#     else:
#         toq.append(i)
# toq.reverse()
# print(juft)
# print(toq)
#11-masala
# n=int(input('n='))
# list=[]
# k=int(input('k='))
# for i in range(n):
#     a=int(input(f'{i+1}-sonni kiriting'))
#     list.append(a)

#12-masa
# n=int(input('n='))
# list=[]
# for i in range(n):
#     a=int(input(f'{i+1}-sonni kiriting'))
#     list.append(a)
# print(list)
# newlist=[]
# for i in range(2,len(list)+2,2):
#     newlist.append(i)
# print(newlist)
#

#

#13-masala
# n=int(input('n='))
# list=[]
# for i in range(n):
#     a=int(input(f'{i+1}-sonni kiriting'))
#     list.append(a)
# print(list)
# newlist=[]
# for i in range(1,len(list)+1,2):
#     newlist.append(i)
#     newlist.sort(reverse=True)
#
# print(newlist)

#14-masala
# n=int(input('n='))
# listlar=[]
# for i in range(n):
#     a=int(input(f'{i+1}-sonni kiriting'))
#     listlar.append(a)
# print(listlar)
# juft=[]
# toq=[]
# for i in listlar:
#     if i%2==0:
#         juft.append(i)
#     else:
#         toq.append(i)
# print(juft)
# print(toq)

#15-masala
# n=int(input('n='))
# listlar=[]
# for i in range(n):
#     a=int(input(f'{i+1}-sonni kiriting'))
#     listlar.append(a)
# print(listlar)
# toq=[]
# juft=[]
# for i in listlar:
#     if i%2==1:
#         toq.append(i)
#     else:
#         juft.append(i)
# print(toq)
# print(juft)

#16-masala
# n=int(input('n='))
# list=[]
# newlist=[]
# for i in range(n):
#     list.append(int(input(f'{i+1}-sonni kiriting=')))
# for i in range(int(len(list)/2)):
#     newlist.append(list[i])
#     newlist.append(list[len(list)-i-1])
# print(newlist)

#17-masala
# n=int(
# # for i in range(n):
# #     a=int(input(f'{i+1}-sonni kiriting='))
# #     list.append(a)
# # bool=True
# # for i in range(len(list)):
# #     while len(list)>0:
# #         if bool:
# #             print(list[0],list[1],end=" ")
# #             list.pop(0)
# #             list.pop(0)
# #             bool=False
# #         else:
# #             print(list[-1],list[-2],end=" ")
# #             list.pop(-1)
# #             list.pop(-1)
# #             bool=True
# #
# # fac=1
# # for i in range(2,1):input('n='))
# list=[]
#     fac=fac*i
# print(fac)pi=(1,2,3)
#massivlar.
# m,n=int(input('m=')),int(input('n='))
# list=[]
# for i in range(1,m+1):
#     res=[]
#     for j in range(n):
#
#         res.append(10*i)
#     list.append(res)
# for i in range(m):
#     for j in range(n):
#         print(list[i][j], end=' ')
#     print('')
# n=int(input('n='))
# listlar=[]
# for i in range(1,n+1):
#     a=int(input(f"{i}-sonni kiriting="))
#     listlar.append(a)
# print(listlar)
# toq=[]
# juft=[]
# for i in listlar:
#     if i%2==1:
#         toq.append(i)
#     else:
#         juft.append(i)
# print(toq)
# print(juft)








    
