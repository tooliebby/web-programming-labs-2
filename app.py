from flask import Flask, redirect, url_for, render_template
from lab1 import lab1

app = Flask(__name__)
app.register_blueprint(lab1)

# Роут второй лабораторной 
@app.route('/lab2/example')
def example():
    name = 'Гритчин Георгий Эдуардович'
    number = '2'
    groupe = 'ФБИ-12'
    course = '3 курс'
    fruits = [
        {'name':'яблоки','price':'99₽'},
        {'name':'груши','price':'139₽'},
        {'name':'апельсины','price':'79₽'},
        {'name':'мандарины','price':'259₽'},
        {'name':'манго','price':'199₽'}
        ]
    books = [
        {'name': '1984', 'name_author': 'Джордж Оруэлл', 'zanr': 'Антиутопия', 'kol_stranits': '328'},
        {'name': 'Преступление и наказание', 'name_author': 'Федор Достоевский', 'zanr': 'Роман', 'kol_stranits': '592'},
        {'name': 'Гарри Поттер и философский камень', 'name_author': 'Дж. К. Роулинг', 'zanr': 'Фэнтези', 'kol_stranits': '320'},
        {'name': 'Война и мир', 'name_author': 'Лев Толстой', 'zanr': 'Роман', 'kol_stranits': '1225'},
        {'name': 'Убийство в Восточном экспрессе', 'name_author': 'Агата Кристи', 'zanr': 'Детектив', 'kol_stranits': '256'},
        {'name': 'Алиса в Стране чудес', 'name_author': 'Льюис Кэрролл', 'zanr': 'Приключения', 'kol_stranits': '240'},
        {'name': 'Мастер и Маргарита', 'name_author': 'Михаил Булгаков', 'zanr': 'Роман', 'kol_stranits': '448'},
        {'name': 'Три товарища', 'name_author': 'Эрих Мария Ремарк', 'zanr': 'Роман', 'kol_stranits': '416'},
        {'name': 'Самый богаты человек в вавилоне', 'name_author': 'Джордж Оруэлл', 'zanr': 'Антиутопия', 'kol_stranits': '156'},
        {'name': 'Анна Каренина', 'name_author': 'Лев Толстой', 'zanr': 'Роман', 'kol_stranits': '864'}
    ]
    return render_template('example.html', name=name, number=number, groupe=groupe,course=course, fruits=fruits, books=books)

#Ссылка на вторую лабораторную
@app.route('/lab2/')
def lab2():
    return render_template('lab2.html')

#Ссылка на самостоятельное задание
@app.route('/lab2/cars')
def cars():
    return render_template('cars.html')

#ЗАЩИТА ЛАБОРАТОРНОЙ №2
@app.route('/lab2/zashita_2')
def zashita_2():
    #Задание №1
    A, B, C = 8, 10, 12

    if A<B<C:
        A=A*2
        B=B*2
        C=C*2
    #Задание №2
        N = 6
        K = 100
        result = str(N) * K 
    #Задание №3
        G = 2
        Q = 4
        result_2 = 0
        for i in range(1, G+1):
            result_2 += i**Q

        letters = [
        {'A': A,'B': B, 'C': C },
    ]
    return render_template('zashita_2.html', letters = letters, N=N, K=K,  result = result, result_2 = result_2)

   
    
    
