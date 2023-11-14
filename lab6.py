from flask import Blueprint, render_template, request, make_response, redirect, session
from Db import db
from Db.models import users, articles
from werkzeug.security import check_password_hash, generate_password_hash
from flask_login import login_user, login_required, current_user

lab6 = Blueprint('lab6', __name__)

#Роут для вывода пользователей из таблицы 'users' в консоль.
@lab6.route("/lab6/check")
def main():
    #тоже самое, что и select * from users
    my_users = users.query.all()
    print(my_users)
    return "result in console!"

#Роут для вывода записей из таблицы 'articles' в консоль.
@lab6.route("/lab6/checkarticles")
def check_articles():
    my_articles = articles.query.all()
    print(my_articles)
    return "result in console!"