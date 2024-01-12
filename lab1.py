from flask import Blueprint, redirect, url_for
lab1 = Blueprint('lab1', __name__)


@lab1.route("/")
@lab1.route("/index")
def start():
    return redirect("/menu", code=302)


@lab1.route("/menu")
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
                <li>
                    <a href="http://127.0.0.1:5000/lab3" target="_blank">Лабораторная работа №3</a>
                </li>
                <li>
                    <a href="http://127.0.0.1:5000/lab4" target="_blank">Лабораторная работа №4</a>
                </li>
                <li>
                    <a href="http://127.0.0.1:5000/lab5" target="_blank">Лабораторная работа №5</a>
                </li>
                <li>
                    <a href="http://127.0.0.1:5000/lab6" target="_blank">Лабораторная работа №6</a>
                </li>
                <li>
                    <a href="http://127.0.0.1:5000/lab7" target="_blank">Лабораторная работа №7</a>
                </li>
                <li>
                
                    <a href="http://127.0.0.1:5000/lab8" target="_blank">Лабораторная работа №8</a>
                </li>
                <li>
                
                    <a href="http://127.0.0.1:5000/lab10" target="_blank">Защита экзамена</a>
                </li>
            </ol>
        </main>

        <footer>
            &copy; Гритчин Георгий, ФБИ-12, 3 курс, 2023
        </footer>
    <body>
</html> 
"""


@lab1.route("/lab1")
def lab():
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


@lab1.route('/lab1/oak')
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


@lab1.route('/lab1/student')
def sudent():
    return'''
<!doctype html>
<html>
    <h1>Гритчин Георгий Эдуардович</h1>
    <img src="''' + url_for('static', filename='nstu.jpg') + '''">
</html>
'''


@lab1.route('/lab1/python')
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


@lab1.route('/lab1/stix')
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