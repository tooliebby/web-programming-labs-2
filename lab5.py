from werkzeug.security import check_password_hash, generate_password_hash
from flask import Blueprint, render_template, request, make_response, redirect, session
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

#Роут Главной страницы
@lab5.route('/lab5')
def lab():
    visibleUser = "Anon"
    return render_template('lab5.html', username=visibleUser)


#Вывод имен пользователей таблицы "Users"
@lab5.route ("/lab5/users")
def users ():
    conn = dbConnect ()
    cur = conn.cursor ()

    cur.execute ("SELECT username FROM users;")
    result = cur. fetchall ()

    # Не забывайте закрывать соединение
    dbClose (cur, conn)

    username = ""
    for row in result:
        username += f"{row[0]}\n"
    return username

#Роут страницы Регистрации 
@lab5.route('/lab5/register',methods=["GET", "POST"])
def registerPage():
    errors = ''

    if request.method == "GET":
        return render_template("register.html", errors=errors)
    
    username = request.form.get("username")
    password = request.form.get("password")

    if username =='' or password=='':
        errors='Пожалуйста, заполните все поля'
        return render_template("register.html", errors=errors)
    

    hashPassword = generate_password_hash(password)
    
    conn = dbConnect ()
    cur = conn.cursor()

    cur.execute(f"SELECT username FROM users WHERE username = '{username}';")

    if cur.fetchone() is not None:
        errors='Пользователь с данным именем уже существует'
        dbClose(cur, conn)
        return render_template("regiSter.html", errors=errors)
    
    cur.execute(f"INSERT INTO users (username, password) VALUES ('{username}','{hashPassword}');")

    conn.commit()
    dbClose(cur,conn)


    return redirect("/lab5/login")

#Роут страницы Логин
@lab5.route('/lab5/login', methods=['GET','POST'])
def loginPage():
    errors=''

    if request.method=='GET':
        return render_template('login.html',errors=errors)
    
    username=request.form.get('username')
    password=request.form.get('password')

    if username =='' or password == '':
        errors='Пожалуйста, заполните все поля'
        return render_template('login.html',errors=errors)

    conn = dbConnect()
    cur = conn.cursor()

    cur.execute(f"SELECT id, password FROM users WHERE username = '{username}'")

    result = cur.fetchone()

    if not result:
        errors='Неправильный логин или пароль'
        dbClose(cur,conn)
        return render_template('login.html',errors=errors)

    userID, hashPassword = result

    # Сравниваем хэш и пароль
    if check_password_hash(hashPassword,password):
        # Сохраняем id и username в сессию 
        session['id']=userID
        session['username']=username
        dbClose(cur,conn)
        return redirect('/lab5')

    else:
        errors='Неправильный логин или пароль'
        return render_template('login.html',errors=errors)
