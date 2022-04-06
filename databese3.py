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
   
    CREATE TABLE IF NOT EXISTS students(
    student_id BIGSERIAL PRIMARY KEY,
    first_name VARCHAR(60),
    last_name VARCHAR(60),
    birth_date TIMESTAMP ,
    university_id integer
     )
    """)
    conn.commit()

def add_students(first_name,last_name,birth_date,university_id,):
    conn=psycopg2.connect(
        host="127.0.0.1",
        database="DATA",
        user="postgres",
        password="5",
        port="5432"

    )
    cursor=conn.cursor()
    cursor.execute("""
    INSERT INTO students (first_name,last_name,birth_date,university_id)
    VALUES (%s,%s,%s,%s)
    """,(first_name,last_name,birth_date,university_id))
    conn.commit()


#add_students("Ochilov","Obodjon",datetime.datetime(1999,1,4),2)
def get_all_students():
    conn=psycopg2.connect(
        host="127.0.0.1",
        database="DATA",
        user="postgres",
        password="5",
        port="5432"

    )
    cursor=conn.cursor()
    cursor.execute("""
    select*from students

    """)
    data=cursor.fetchall()
    return data
malumotlar=get_all_students()
#print(malumotlar):


def del_students(student_id):
    conn=psycopg2.connect(
        host="127.0.0.1",
        database="DATA",
        user="postgres",
        password="5",
        port="5432"

    )
    cursor=conn.cursor()
    cursor.execute("""
    DELETE FROM students
    where student_id={student_id}
     """)
    conn.commit()
#del_students(1)











