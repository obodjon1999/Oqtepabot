import psycopg2
import datetime
def creat_table():
    conn = psycopg2.connect(
    host="127.0.0.1",
    database="DATA",
    user="postgres",
    password="5",
    port="5432"
    )
    cursor = conn.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS talabalar(
    talaba_id  BIGSERIAL PRIMARY KEY,
    first_name varchar(60),
    last_name varchar(60),
    birth_date TIMESTAMP,
    university_id INTEGER)
    
    """)

    conn.commit()
#creat_table()

def add_talabalar(first_name,last_name,birth_date,university_id):
    conn = psycopg2.connect(
    host="127.0.0.1",
    database="DATA",
    user="postgres",
    password="5",
    port="5432"
    )
    cursor = conn.cursor()
    cursor.execute("""
    INSERT INTO talabalar (first_name,last_name,birth_date,university_id)
    VALUES  (%s,%s,%s,%s)
    """,(first_name,last_name,birth_date,university_id))
    conn.commit()
# add_talabalar('Jahongir','Bahodirov',datetime.datetime(1999,8,12),4)



def get_all_talabalar():
    conn = psycopg2.connect(
    host="127.0.0.1",
    database="DATA",
    user="postgres",
    password="5",
    port="5432"
    )
    cursor = conn.cursor()
    cursor.execute("""
    select*from talabalar
    """)
    data=cursor.fetchall()
    return data
malumotlar=get_all_talabalar()
print(malumotlar)

def update_talabalar(first_name,last_name,talaba_id):
    conn = psycopg2.connect(
    host="127.0.0.1",
    database="DATA",
    user="postgres",
    password="5",
    port="5432"
    )
    cursor = conn.cursor()
    cursor.execute(f"""
    UPDATE talabalar
    SET first_name='{first_name}',last_name='{last_name}'
    WHERE talaba_id={talaba_id}
    """)
    conn.commit()
# update_talabalar('chori','yoriyev',3)


def del_talabalar(talaba_id):
    conn = psycopg2.connect(
    host="127.0.0.1",
    database="DATA",
    user="postgres",
    password="5",
    port="5432"
    )
    cursor = conn.cursor()

    cursor.execute(f"""
    DELETE FROM talabalar
    WHERE talaba_id={talaba_id}
    """)
    conn.commit()
#del_talabalar(1)



























