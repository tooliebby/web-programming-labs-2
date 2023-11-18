from flask import Blueprint, render_template, request, make_response, redirect, session
from Db import db
from Db.models import users, articles
from werkzeug.security import check_password_hash, generate_password_hash
from flask_login import login_user, login_required, current_user

lab6 = Blueprint('lab6', __name__)

#Роут для вывода пользователей из таблицы 'users' в консоль.
@lab6.route("/lab6")
def main():
    if current_user.is_authenticated:
        username = current_user.username
    else:
        username = "Аноним"
    return render_template('lab6.html', username=username)

#Роут для вывода записей из таблицы 'articles' в консоль.
@lab6.route("/lab6/checkarticles")
def check_articles():
    my_articles = articles.query.all()
    print(my_articles)
    return "result in console!"

#Роут для регистрации 
@lab6.route("/lab6/register", methods=["GET", "POST"])
def register():

    errors = ''

    if request.method == "GET":
        return render_template("register.html")
    
    username_form = request.form.get("username")
    password_form = request.form.get("password")

    isUserExist = users.query.filter_by(username=username_form).first()
    
    #Если пустое имя.
    if username_form == '':
        errors='Пустое имя'
        return render_template("register.html", errors=errors)
    else:
        #Если пользователь с таким именем уже существует.
        if isUserExist is not None:
            errors='Пользователь с тамим именем уже существует'
            return render_template("register.html")
        else:
            #Если пароль меньше 5-ти символов.
            if len(password_form) <5:
                errors='Пароль меньше 5-ти сиволов'
                return render_template("register.html")
            else:
                #Хэшируем пароль.
                hashedPswd = generate_password_hash(password_form, method='pbkdf2')
                #Создаем обьект users с нужными полями.
                newUser = users(username=username_form, password=hashedPswd)

                #Это INSERT.
                db.session.add(newUser)
                #Тоже самое, что и conn.commit().
                db.session.commit()

    #Перенаправляем на страницу логина.
    return redirect("/lab6/login")

#Роут для авторизации
@lab6.route("/lab6/login", methods=["GET", "POST"])
def login():
    errors = ''
    if request.method == "GET":
        return render_template("login.html")
    
    username_form = request.form.get("username")
    password_form = request.form.get("password")

    my_user = users.query.filter_by(username=username_form).first()

    #Если поля ввода не заполнены.
    if username_form == '' or password_form == '':
        errors='Заполните поле пользователь и пароль'
        return render_template("login.html", errors=errors)
    else:
        if my_user is not None:
            if check_password_hash(my_user.password, password_form):
                #сохраняем JWT токен.
                login_user(my_user, remember=False)
                return redirect("/lab6/articles")
            #Если введен неправильный пароль.
            else:
                errors='Введен не верный пароль'
                return render_template("login.html", errors=errors)
        #Если пользователя не существует.
        else:
            errors='Пользователя с таким именем не существует'
            return render_template("login.html", errors=errors)

#Роут для просмотра статей
@lab6.route("/lab6/articles")
@login_required
def articles_list():
    my_articles = articles.query.filter_by(user_id=int(current_user.id)).all()
    return render_template("spisok_article.html", articles_list=my_articles)  

@lab6.route('/lab6/articles/<int:article_id>')
@login_required
def view_article(article_id):
    article = articles.query.get(article_id)
    return render_template('spisok_article.html', article=article)

#Роут для разлогинизации 
@lab6.route("/lab6/logout")
@login_required
def logout():
    logout_user()
    return redirect("/lab6/login")   

#Роут для  создания новых заметок
@lab6.route('/lab6/articles/add', methods=['GET', 'POST'])
@login_required
def add_article():
    if request.method == 'POST':
        title_article = request.form['title_article']
        text_article = request.form['text_article']
        new_article = articles(title=title_article, article_text=text_article, user_id=current_user.id)
        db.session.add(new_article)
        db.session.commit()
        return redirect('/lab6/articles')
    return render_template('new_article.html')     