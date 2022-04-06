import psycopg2
import datetime


def creat_table():
    conn = psycopg2.connect(
        host="127.0.0.1",
        database="oqtepa",
        user="postgres",
        password="5",
        port="5432"
    )
    cursor = conn.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users(
    id  BIGSERIAL PRIMARY KEY,
    telegram_id integer,
    full_name varchar(60),
    phone_nomer varchar(25)
    )

    """)

    conn.commit()
def creat_table_category():
    conn = psycopg2.connect(
        host="127.0.0.1",
        database="oqtepa",
        user="postgres",
        password="5",
        port="5432"
    )
    cursor = conn.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS category(
    category_id  BIGSERIAL PRIMARY KEY,
    name Varchar(255)
    )

    """)

    conn.commit()

def creat_table_product():
    conn = psycopg2.connect(
        host="127.0.0.1",
        database="oqtepa",
        user="postgres",
        password="5",
        port="5432"
    )
    cursor = conn.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS product(
    product_id  BIGSERIAL PRIMARY KEY,
    name Varchar(255),
    ctegory_id integer,
    image Varchar(255)
    )

    """)

    conn.commit()



def creat_table_savatcha():
    conn = psycopg2.connect(
        host="127.0.0.1",
        database="oqtepa",
        user="postgres",
        password="5",
        port="5432"
    )
    cursor = conn.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS savatcha(
    savatcha_id  BIGSERIAL PRIMARY KEY,
    product_id integer,
    user_id integer,
    soni integer,
    status VARCHAR(25)
    )

    """)

    conn.commit()
def add_savatcha(user_id,product_id,soni,status):
    conn = psycopg2.connect(
    host="127.0.0.1",
    database="oqtepa",
    user="postgres",
    password="5",
    port="5432"
    )
    cursor = conn.cursor()
    cursor.execute("""
    INSERT INTO savatcha (product_id,user_id,soni,status)
    VALUES  (%s,%s,%s,%s)
    """,(product_id,user_id,soni,status))
    conn.commit()


def add_product(product_name,narxi,category):
    conn = psycopg2.connect(
    host="127.0.0.1",
    database="oqtepa",
    user="postgres",
    password="5",
    port="5432"
    )
    cursor = conn.cursor()
    cursor.execute(f"""
    INSERT INTO product (name,price,ctegory_id)
    VALUES  (%s,%s,(select category_id from category
where name='{category}'))
    """,(product_name,narxi))
    conn.commit()


def get_savatcha(user_id,status):
    conn = psycopg2.connect(
    host="127.0.0.1",
    database="oqtepa",
    user="postgres",
    password="5",
    port="5432"
    )
    cursor = conn.cursor()
    cursor.execute(f"""
        select savatcha_id,soni,product.name,product.price from savatcha
        join product on savatcha.product_id=product.product_id
        where savatcha.status='{status}' and user_id={user_id}
        ORDER BY savatcha_id
        """)
    data=cursor.fetchall()
    return data


def minus_savatcha(savatcha_id):
    conn = psycopg2.connect(
    host="127.0.0.1",
    database="oqtepa",
    user="postgres",
    password="5",
    port="5432"
    )
    cursor = conn.cursor()
    cursor.execute(f"""
        update savatcha
        set soni=soni-1
        where savatcha_id={savatcha_id}
        """)
    conn.commit()

def get_savatcha_quantity(savatcha_id):
    conn = psycopg2.connect(
    host="127.0.0.1",
    database="oqtepa",
    user="postgres",
    password="5",
    port="5432"
    )
    cursor = conn.cursor()
    cursor.execute(f"""
        select soni from savatcha
        where savatcha_id={savatcha_id}
        """)
    data=cursor.fetchone()
    return data

def delete_savatcha(savatcha_id):
    conn = psycopg2.connect(
    host="127.0.0.1",
    database="oqtepa",
    user="postgres",
    password="5",
    port="5432"
    )
    cursor = conn.cursor()
    cursor.execute(f"""
        delete from savatcha
        where savatcha_id={savatcha_id}
        """)
    conn.commit()
def change_savatcha_status(savatcha_id):
    conn = psycopg2.connect(
    host="127.0.0.1",
    database="oqtepa",
    user="postgres",
    password="5",
    port="5432"
    )
    cursor = conn.cursor()
    cursor.execute(f"""
        update savatcha
        set status='zakas'
        where savatcha_id={savatcha_id}
        """)
    conn.commit()


def plus_savatcha(savatcha_id):
    conn = psycopg2.connect(
    host="127.0.0.1",
    database="oqtepa",
    user="postgres",
    password="5",
    port="5432"
    )
    cursor = conn.cursor()
    cursor.execute(f"""
        update savatcha
        set soni=soni+1
        where savatcha_id={savatcha_id}
        """)
    conn.commit()


def get_product(ctegory_id):
    conn = psycopg2.connect(
    host="127.0.0.1",
    database="oqtepa",
    user="postgres",
    password="5",

    port="5432"
    )

    cursor = conn.cursor()

    cursor.execute(f"""
    select * from product
    where ctegory_id = {ctegory_id}
    """)
    data = cursor.fetchall()
    print(data)
    return data

def get_producty (product_id):
    conn = psycopg2.connect(
    host="127.0.0.1",
    database="oqtepa",
    user="postgres",
    password="5",

    port="5432"
    )

    cursor = conn.cursor()

    cursor.execute(f"""
    select * from product
    where product_id = {product_id}
    """)
    data = cursor.fetchone()
    print(data)
    return data


def add_users(full_name,phone_nomer,telegram_id):
    conn = psycopg2.connect(
    host="127.0.0.1",
    database="oqtepa",
    user="postgres",
    password="5",
    port="5432"
    )
    cursor = conn.cursor()
    cursor.execute("""
    INSERT INTO users (full_name,phone_nomer,telegram_id)
    VALUES  (%s,%s,%s)
    """,(full_name,phone_nomer,telegram_id))
    conn.commit()

def add_category(name):
    conn = psycopg2.connect(
    host="127.0.0.1",
    database="oqtepa",
    user="postgres",
    password="5",
    port="5432"
    )
    cursor = conn.cursor()
    cursor.execute("""
    INSERT INTO category (name)
    VALUES  (%s)
    """,(name,))
    conn.commit()

def get_category():
    conn = psycopg2.connect(
    host="127.0.0.1",
    database="oqtepa",
    user="postgres",
    password="5",
    port="5432"
    )
    cursor = conn.cursor()
    cursor.execute("""
    SELECT*FROM category
    """)
    data=cursor.fetchall()
    return data
    
    


def check_users(telegram_id):
    conn = psycopg2.connect(
    host="127.0.0.1",
    database="oqtepa",
    user="postgres",
    password="5",
    port="5432"
    )
    cursor = conn.cursor()
    cursor.execute(f"""
    SELECT*FROM users
    WHERE telegram_id={telegram_id}
    
    """)
    data=cursor.fetchone()
    if data:
        return True
    else:
        return False


def check_admin(telegram_id):
    conn = psycopg2.connect(
        host="127.0.0.1",
        database="oqtepa",
        user="postgres",
        password="5",
        port="5432"
    )
    cursor = conn.cursor()
    cursor.execute(f"""
    SELECT status from users
    WHERE telegram_id={telegram_id}

    """)
    data = cursor.fetchone()
    if data[0]=='admin':
        return True
    else:
        return False


def check_category(name):
    conn = psycopg2.connect(
        host="127.0.0.1",
        database="oqtepa",
        user="postgres",
        password="5",
        port="5432"
    )
    cursor = conn.cursor()
    cursor.execute(f"""
    SELECT name from category
    WHERE name='{name}'

    """)
    data = cursor.fetchone()
    if data:
        return True
    else:
        return False

def get_user(telegram_id):
    conn = psycopg2.connect(
        host="127.0.0.1",
        database="oqtepa",
        user="postgres",
        password="5",
        port="5432"
    )
    cursor = conn.cursor()
    cursor.execute(f"""
    SELECT*FROM users
    WHERE telegram_id={telegram_id}

    """)
    data = cursor.fetchone()
    return data


def add_achko(telegram_id):
    conn = psycopg2.connect(
        host="127.0.0.1",
        database="oqtepa",
        user="postgres",
        password="5",
        port="5433"
    )

    cursor = conn.cursor()

    cursor.execute(f"""
        update users
        set achko = achko+1
        where telegram_id = {telegram_id}
        """)
    conn.commit()
def get_achko(telegram_id):
    conn = psycopg2.connect(
        host="127.0.0.1",
        database="oqtepa",
        user="postgres",
        password="5",

        port="5432"
    )

    cursor = conn.cursor()

    cursor.execute(f"""
    select achko from users
    where telegram_id = {telegram_id}
        """)
    data = cursor.fetchone()
    print(data)
    return data
