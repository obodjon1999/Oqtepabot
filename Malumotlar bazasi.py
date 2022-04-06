import sqlite3
conn=sqlite3.connect("new_fayl.db")
cursor=conn.cursor()

# cursor.execute("""
# CREATE TABLE  IF NOT EXISTS projects(
# id integer PRIMARY KEY,
# ism text,
# familiyasi CHAR(120),
# t_yil integer)
# """)
# def add_data_project(ism,familiya,t_yili):
#     cursor.execute(f"INSERT INTO projects (ism,familiyasi,t_yil) VALUES ('{ism}','{familiya}',{t_yili})")
#     conn.commit()
# ism=input('ismini kiriting')
# familiyasi=input('familiyasini kiriting')
# yili=int(input('tugilgan yilini kiriting'))
# add_data_project(ism, familiyasi, yili)


#1-MASALA.VAZIFA.
# cursor.execute("""
# CREATE TABLE  IF NOT EXISTS Insitut(
# id integer PRIMARY KEY,
# name text,
# found_year integer,
# talabalar_soni integer)
# """)
# def Insitut(ism,year,son):
#     cursor.execute(f"INSERT INTO Insitut(name,found_year,talabalar_soni) VALUES ('{ism}',{year},{son})")
#     conn.commit()
# ism=input('universitet nomini kiriting:')
# year=int(input('yilini kiriting'))
# son=int(input('talabalar sonini kiriting:'))
# Insitut(ism,year,son)

# cursor.execute("""
# SELECT*from Insitut;
# """)
# data=cursor.fetchall()
# print(data)


# cursor.execute("""
# SELECT id,found_year from Insitut;
# """)
# data=cursor.fetchall()
# print(data)

# cursor.execute("""
# SELECT*from Insitut;
# """)
# data=cursor.fetchone()
# print(data)


#2-MASALA.VAZIFA.
# cursor.execute("""
# CREATE TABLE  IF NOT EXISTS kafedra(
# id integer PRIMARY KEY,
# nome text,
# kafedra_soni integer,
# muduri CHAR(120))
# """)

# def kafedra(ismi,count,mudur):
#     cursor.execute(f"INSERT INTO kafedra(nome,kafedra_soni,muduri) VALUES ('{ismi}',{count},'{mudur}')")
#     conn.commit()
# ismi=input('kafedra nomini kiriting:')
# count=int(input('kafedralar sonini kiriting:'))
# mudur=input('mudur ismini kiriting:')
# kafedra(ismi,count,mudur)

# cursor.execute("""
# SELECT*from kafedra;
# """)
# data=cursor.fetchall()
# print(data)



# cursor.execute("""
# SELECT muduri,kafedra_soni from kafedra;
# """)
# data=cursor.fetchall()
# print(data)


# cursor.execute("""
# SELECT*from kafedra;
# """)
# data=cursor.fetchone()
# print(data)

#3-MASALA.VAZIFA
# cursor.execute("""
# CREATE TABLE  IF NOT EXISTS talaba(
# id integer PRIMARY KEY,
# ismi text,
# familiyasi CHAR(150),
# viloyati text,
# yoshi integer)
# """)
# def talaba(ism,familiya,viloyat,yosh):
#     cursor.execute(f"INSERT INTO talaba(ismi,familiyasi,viloyati,yoshi) VALUES ('{ism}','{familiya}','{viloyat}',{yosh})")
#     conn.commit()
# ism=input('ismini kiriting:')
# familliya=input('familiyasini kiritig:')
# viloyati=input('viloyatini kiriting:')
# yoshi=int(input('yoshini kiriting:'))
# talaba(ism,familliya,viloyati,yoshi,)


# cursor.execute("""
# SELECT*from talaba;
# """)
# data=cursor.fetchall()
# print(data)

# cursor.execute("""
# SELECT ismi,viloyati from talaba;
# """)
# data=cursor.fetchall()
# print(data)


# cursor.execute("""
# SELECT*from talaba;
# """)
# data=cursor.fetchone()
# print(data)









