from flask import Blueprint, render_template, request
lab3 = Blueprint('lab3', __name__)

#Роут "Лабораторная работа№3"
@lab3.route('/lab3/')
def lab():
    return render_template('lab3.html')

#Роут "Формы"
@lab3.route('/lab3/form1')
def form1():
    errors = {}
    user = request.args.get('user')
    if user == '':
        errors['user'] = 'Заполните поле!'
    age = request.args.get('age')
    if age == '':
        errors['age'] = 'Заполните поле!'
    sex = request.args.get('sex')
    return render_template('form1.html', user=user, age=age, sex=sex, errors=errors)


#Роут "Заказ напитка"
@lab3.route('/lab3/order')
def order():
    return render_template('order.html')


#Роут "Оплата"
@lab3.route('/lab3/pay')
def pay():
    price = 0
    drink = request.args.get('drink')
    #Пусть кофе стоит 120 рублей, черный чай - 80 рублей, зеленый чай - 70 рублей.
    if drink == 'coffe':
        price = 120
    elif drink == 'black-tea':
        price = 80
    else:
        price = 70

    #Добавка молока удоражает напиток на 30 рублей, а сахар на 10.
    if request.args.get('milk') == 'on':
        price += 30
    if request.args.get('sugar') == 'on':
        price += 10
    return render_template('pay.html', price=price)


#Роут "Согласие"
@lab3.route('/lab3/success')
def success():
    return render_template('success.html')

#Роут "Железнодорожный билет"
@lab3.route('/lab3/ticket')
def ticket():
    #Переменная "Ошибки"
    errors = {}
    #Перкменная "ФИО"
    user = request.args.get('user')
        #Если поле ввода "ФИО" будет пустым, то выскочит надпись ошибка.
    if user == '':
        errors['user'] = 'Заполните поле!'
    #Переменна "Тип билета"
    type = request.args.get('type')  
    #Переменна "Полка"  
    shelf = request.args.get('shelf') 
    #Переменна "Багаж" 
    bag = request.args.get('bag')
    #Переменная "Возраст"
    age = request.args.get('age')
        #Если поле ввода "Возраст" будет пустым, то выскочит надпись ошибка.
    if age == '':
        errors['age'] = 'Заполните поле!'
    #Перкменная "Пункт отправления"
    departure = request.args.get('departure')
        #Если поле ввода "Пункт отправления" будет пустым, то выскочит надпись ошибка.
    if departure == '':
        errors['departure'] = 'Заполните поле!'
    #Перкменная "Пункт прибытия"
    entry = request.args.get('entry')
        #Если поле ввода "Пункт прибытия" будет пустым, то выскочит надпись ошибка.
    if  entry == '':
        errors['entry'] = 'Заполните поле!'
    #Переменная "Дата"
    date = request.args.get('date')
        #Если поле ввода "Дата" будет пустым, то выскочит надпись ошибка.
    if  date == '':
        errors['date'] = 'Заполните поле!'
    return render_template('ticket.html', user=user, errors=errors, type=type, shelf=shelf, bag=bag, age=age, departure=departure,entry=entry, date=date)