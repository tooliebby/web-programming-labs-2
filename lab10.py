from flask import Blueprint, redirect, url_for, render_template,request
lab10 = Blueprint('lab10', __name__)


@lab10.route('/lab10/')
def ekzamen():
    return render_template('lab10/ekzamen.html')

@lab10.route('/result', methods=['POST'])
def result():
    x = int(request.form['x'])
    y = int(request.form['y'])
    z = int(request.form['z'])
    result = 2*x + 8*y + 7*z
    return render_template('lab10/result.html', result=result)