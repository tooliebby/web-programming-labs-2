from flask import Blueprint, render_template, request, session
lab4 = Blueprint('lab4', __name__)


@lab4.route('/lab4/')
def lab():
    return render_template('lab4.html')


#Задание - Авторизация
@lab4.route('/lab4/login', methods = ['GET','POST'])
def login():
    if request.method == 'GET':
        return render_template("login.html")
    
    #Получение введенных значений 
    username = request.form.get('username')
    password = request.form.get('password')

    # Проверка на пустой логин и пароль
    if not username:
        error = 'Не введен логин'
        return render_template('login.html', error=error)
    elif not password:
        error = 'Не введен пароль'
        return render_template('login.html', error=error)

    #Если данные введены корректно 
    if username == 'alex' and password == '123':
        return render_template('success_for_lab4.html')
    #Если данные введены некорректно 
    else:
        error = 'Неверный логин и/или пароль'
        return render_template('login.html', error=error, username=username, password=password)
