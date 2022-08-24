import sqlite3

conn = sqlite3.connect('forca_data_base.db')

c = conn.cursor()

def create_table():
    c.execute("""CREATE TABLE database (
        name text,
        nivel text,
        fases text
        )""")

def drop_table():
    c.execute("DROP TABLE database")
    conn.commit()

def insert_many(person_list):
    with conn:
        c.executemany("INSERT INTO database VALUES (?,?,?)", person_list)

def insert_one(person):
    with conn:
        c.execute("INSERT INTO database VALUES (:name, :nivel, :fases)", person)

def get_by_name(person_name):
    c.execute("SELECT * FROM database WHERE name = :name", {'name': person_name})
    return c.fetchall()

def delete_person(person_name):
    with conn:
        c.execute("DELETE from database WHERE name = :name", {'name': person_name})

def get_all():
    with conn:
        c.execute("SELECT * FROM database")
        return c.fetchall()
