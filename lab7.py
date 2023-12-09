from flask import Blueprint, render_template, request, make_response
from flask import abort

lab7=Blueprint('lab7', __name__)

#Роут для 7-й лабораторной
@lab7.route('/lab7/')
def main():
    return render_template('lab7/index.html')

#Роут для страницы заказа напитка
@lab7.route('/lab7/drink')
def drink():
    return render_template('lab7/drink.html')

@lab7.route('/lab7/api', methods=['POST'])
def api():
    data=request.json

    if data['method'] == 'get-price':
        return get_price(data['params'])
    if data['method'] == 'pay':
        return pay(data['params'])
    
    abort(400)

def get_price(params):
    return{'result': calculate_price(params), 'error':None}

def calculate_price(params):
    drink=params['drink']
    milk=params['milk']
    sugar=params['sugar']

    if drink == 'coffee':
        price = 120
    elif drink == 'black tea':
        price=80
    else:
        price=70

    if milk:
        price+=30
    if sugar:
        price+=10

    return price

def pay(params):
    card_num=params['card_num']
    if len(card_num) != 16 or not card_num.isdigit():
        return {'result':None, "error": 'Неверный номер карты'}
    cvv=params['cvv']
    if len(cvv) != 3 or not cvv.isdigit():
        return {'result':None, "error": 'Неверный номер cvv'}
        
    price=calculate_price(params)
    return{"result": "success", "message": f"С карты {card_num} списано {price} руб", "error": None}

#Функция возврата
def refund(params):
    card_num = params['card_num']
    price = calculate_price(params)
    return {"result":f'Деньги возвращены на карту {card_num} в сумме {price}','error': None}