from flask import Flask
app = Flask(__name__)

@app.route("/")
def start():
    return """
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

        <footer>
            &copy; Гритчин Георгий, ФБИ-12, 3 курс, 2023
        </footer>
    <body>
</html> 
"""


