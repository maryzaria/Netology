import os
from dotenv import load_dotenv
import psycopg2


def create_db(cur):
    cur.execute("""
    DROP TABLE telephone;
    DROP TABLE client;
    """)
    cur.execute("""
    CREATE TABLE IF NOT EXISTS client (
        client_id SERIAL PRIMARY KEY,
        first_name VARCHAR(40) NOT NULL,
        last_name VARCHAR(40) UNIQUE NOT NULL,
        email VARCHAR(40) UNIQUE NOT NULL
    );
    """)
    cur.execute("""
    CREATE TABLE IF NOT EXISTS telephone (
        id SERIAL PRIMARY KEY,
        number VARCHAR(20) UNIQUE NOT NULL,
        client_id INTEGER REFERENCES client(client_id)
    );
    """)


def add_client(cur, first_name, last_name, email, phones=None):
    cur.execute("""
    INSERT INTO client (first_name, last_name, email) VALUES (%s, %s, %s) RETURNING client_id;
    """, (first_name, last_name, email))
    client_id = cur.fetchone()[0]
    if phones is not None:
        if isinstance(phones, (tuple, list)):
            for phone in phones:
                add_phone(cur, client_id, phone)
        elif isinstance(phones, (str, int)):
            add_phone(cur, client_id, str(phones))


def add_phone(cur, client_id, phone_number):
    cur.execute("""
    INSERT INTO telephone (number, client_id) VALUES (%s, %s);
    """, (phone_number, client_id))


def change_client(cur, client_id, first_name=None, last_name=None, email=None, phone=None):
    if first_name is not None:
        cur.execute("""
        UPDATE client SET first_name=%s WHERE client_id=%S;
        """, (first_name, client_id))
    if last_name is not None:
        cur.execute("""
        UPDATE client SET last_name=%s WHERE client_id=%S;
        """, (last_name, client_id))
    if email is not None:
        cur.execute("""
        UPDATE client SET email=%s WHERE client_id=%S;
        """, (email, client_id))
    if phone is not None:
        cur.execute("""
        SELECT number FROM telephone
        WHERE client_id=%s;
        """, (client_id,))
        old_phone = cur.fetchone()[0]
        delete_phone(cur, client_id, old_phone)
        add_phone(cur, client_id, phone)


def delete_phone(cur, client_id, phone):
    cur.execute("""
    DELETE FROM telephone WHERE client_id=%s AND number=%s;
    """, (client_id, phone))


def delete_client(cur, client_id):
    cur.execute("""
    DELETE FROM telephone WHERE client_id=%s;
    DELETE FROM client WHERE client_id=%s;
    """, (client_id, client_id))


def find_client(cur, first_name=None, last_name=None, email=None, phone=None):
    if any([first_name, last_name, email]):
        cur.execute("""
        SELECT client_id FROM client
        WHERE first_name=%s OR first_name=%s OR email=%s;
        """, (first_name, last_name, email))
    elif phone:
        cur.execute("""
        SELECT client_id FROM telephone
        WHERE number=%s
        """, (phone,))
    res = cur.fetchall()
    if len(res) == 1:
        return f'client id: {res[0][0]}'
    return f'clients id: {", ".join([str(r[0]) for r in res])}'


if __name__ == '__main__':
    load_dotenv()
    user_password = os.getenv('USER_PASSWORD')
    # перед созданием подключения необходимо создать БД createdb -U postgres clients_db
    with psycopg2.connect(database='clients_db', user='postgres', password=user_password) as conn:
        with conn.cursor() as cursor:
            create_db(cursor)
            add_client(cursor, 'Мария', 'Зарипова', 'zaripova@gmail.com', '350288')
            change_client(cursor, 1, phone='261029')
            add_client(cursor, 'Гвидо', 'ван Россум', 'Gvido@gmail.com')
            add_phone(cursor, 2, '5555555')
            add_phone(cursor, 1, '599806')
            add_client(cursor, 'Илон', 'Маск', 'go_to_mars@gmail.com', '20232033')
            add_client(cursor, 'Мария', 'Склодовская-Кюри', 'radiation_is_top@gmail.com')
            print(find_client(cursor, email='go_to_mars@gmail.com'))
            print(find_client(cursor, phone='261029'))
            print(find_client(cursor, 'Мария'))
            print(find_client(cursor, phone='5555555'))
            delete_client(cursor, 1)
            print(find_client(cursor, 'Мария'))
    conn.close()


