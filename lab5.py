from flask import Blueprint, render_template, request, session
import psycopg2

lab5 = Blueprint('lab5', __name__)

def dbConnect ():
    conn = psycopg2.connect (
        host="127.0.0.1",
        database="knowledge_base_for_gritchin_georgiy", 
        user="gritchin_georgiy_knowledge_base",
        password="0407")

    return conn

def dbClose (cursor, connection):
    # Закрываем курсор и соединение
    # Порядок важен!
    cursor. close ()
    connection.close ()

@lab5.route ("/lab5")
def main ():
    conn = dbConnect ()
    cur = conn.cursor ()

    cur.execute ("SELECT * FROM users;")

    result = cur. fetchall ()

    print (result)

    # Не забывайте закрывать соединение
    dbClose (cur, conn)
    return "go to console"

#Вывод имен пользователей таблицы "Users"
@lab5.route ("/lab5/users")
def users ():
    conn = dbConnect ()
    cur = conn.cursor ()

    cur.execute ("SELECT username FROM users;")

    result = cur. fetchall ()

    print (result)

    # Не забывайте закрывать соединение
    dbClose (cur, conn)
    return result