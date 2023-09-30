from flask import Flask, redirect, url_for, render_template
app = Flask(__name__)

@app.route("/")
@app.route("/index")
def start():
    return redirect("/menu", code=302)

@app.route("/menu")
def menu():
    return """
<!doctype html>
<html>
    <head>
        <title>Гритчин Георгий, Лабораторная 1</title>
    </head>
    <body>
        <header>
            НГТУ, ФБ, WEB-программирование, часть 2. Список лабораторных
        </header>        

        <h1>web-сервер на flask</h1>

        <h2>Меню лабораторных работ</h1>

        <main>
            <ol>
                <li>
                    <a href="http://127.0.0.1:5000/lab1" target="_blank">Лабораторная работа №1</a>
                </li>
                <li>
                    <a href="http://127.0.0.1:5000/lab2" target="_blank">Лабораторная работа №2</a>
                </li>
            </ol>
        </main>

        <footer>
            &copy; Гритчин Георгий, ФБИ-12, 3 курс, 2023
        </footer>
    <body>
</html> 
"""
@app.route("/lab1")
def lab1():
    return"""
<!doctype html>
<html>
    <head>
        <title>Гритчин Георгий, Лабораторная 1</title>
    </head>
    
    <body>
        <header>
            НГТУ, ФБ, Лабораторная 1
        </header>        

        <h1>web-сервер на flask</h1>

            <h5>
            Flask — фреймворк для создания веб-приложений на языке
            программирования Python, использующий набор инструментов
            Werkzeug, а также шаблонизатор Jinja2. Относится к категории так
            называемых микрофреймворков — минималистичных каркасов
            веб-приложений, сознательно предоставляющих лишь самые базовые возможности.
            </h5>
            <a href="/menu" target="_blank">меню</a>

        <h1>Реализованные роуты</h1>

        <main>
            <ul>
                <li>
                    <a href="http://127.0.0.1:5000/lab1/oak" target="_blank">Дуб</a>
                </li>
            </ul>
            <ul>
                <li>
                    <a href="http://127.0.0.1:5000/lab1/student" target="_blank">Студент</a>
                </li>
            </ul>
            <ul>
                <li>
                    <a href="http://127.0.0.1:5000/lab1/python" target="_blank">Python</a>
                </li>
            </ul>
            <ul>
                <li>
                    <a href="http://127.0.0.1:5000/lab1/stix" target="_blank">Стихотворение А.С.Пушкина</a>
                </li>
            </ul>
        </main>

        <footer>
            &copy; Гритчин Георгий, ФБИ-12, 3 курс, 2023
        </footer>
    <body>
</html> 
"""
@app.route('/lab1/oak')
def oak():
    return'''
<!doctype html>
<html>
    <head>
        <link rel="stylesheet" type="text/css" href="''' + url_for('static', filename='lab1.css') + '''">
    </head>
    <body>
        <h1>Дуб</h1>
        <img src="''' + url_for('static', filename='oak.jpg') + '''">
        
     
    </body>
</html>
'''
@app.route('/lab1/student')
def sudent():
    return'''
<!doctype html>
<html>
    <h1>Гритчин Георгий Эдуардович</h1>
    <img src="''' + url_for('static', filename='nstu.jpg') + '''">
</html>
'''

@app.route('/lab1/python')
def python():
    return'''
<!doctype html>
<html>
    <h1>
    Что такое Python?
    </h1>

    <h5>
    Python — это язык программирования, который широко используется в интернет-приложениях, разработке программного обеспечения, науке о данных и машинном обучении (ML). Разработчики используют Python, потому что он эффективен, прост в изучении и работает на разных платформах. Программы на языке Python можно скачать бесплатно, они совместимы со всеми типами систем и повышают скорость разработки.
    </h5>

    <h1>
    В чем заключаются преимущества языка Python?
    </h1>

    <h5>
    Язык Python имеет следующие преимущества:

    Разработчики могут легко читать и понимать программы на Python, поскольку язык имеет базовый синтаксис, похожий на синтаксис английского. 
    Python помогает разработчикам быть более продуктивными, поскольку они могут писать программы на Python, используя меньше строк кода, чем в других языках.
    Python имеет большую стандартную библиотеку, содержащую многократно используемые коды практически для любой задачи. В результате разработчикам не требуется писать код с нуля.
    Разработчики могут легко сочетать Python с другими популярными языками программирования: Java, C и C++.
    Активное сообщество Python состоит из миллионов поддерживающих разработчиков со всего мира. При возникновении проблем сообщество поможет в их решении.
    Кроме того, в Интернете доступно множество полезных ресурсов для изучения Python. Например, вы можете легко найти видеоролики, учебные пособия, документацию и руководства для разработчиков.
    Python можно переносить на различные операционные системы: Windows, macOS, Linux и Unix.
    </h5>

    <img src="''' + url_for('static', filename='python.jpg') + '''">
</html>
'''

@app.route('/lab1/stix')
def stix():
    return'''
<!doctype html>
<html>
    <head>
        <link rel="stylesheet" type="text/css" href="''' + url_for('static', filename='lab1.css') + '''">
    </head>
    <img src="''' + url_for('static', filename='stix.jpg') + '''">
    <h2>Напрасно воспевать мне ваши именины</h2>
    <h2>При всем усердии послушности моей;</h2>
    <h2>Вы не милее в день святой Екатерины</h2>
    <h2>Затем, что никогда нельзя быть вас милей.</h2>
</html>
'''

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

   
    
    
