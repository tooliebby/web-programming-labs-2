from werkzeug.security import check_password_hash, generate_password_hash
from flask import jsonify, abort, Blueprint, render_template, request, make_response, redirect, session
import psycopg2
from datetime import date, datetime
from Db import db
from Db.models import users, articles
from flask_login import login_user, login_required, current_user, logout_user

lab8 = Blueprint('lab8', __name__)

@lab8.route('/lab8/')
def main():
    return render_template("lab8/index.html")

courses = [
    {"name": "c++", "videos": 3, "price": 3000, "created": '2019-01-06'},
    {"name": "basic", "videos": 30, "price": 0, "created": '2021-02-11'},
    {"name": "c#", "videos": 8, "created": '2023-11-26'}
]

@lab8.route('/lab8/api/courses/', methods=['GET'])
def get_courses():
    return jsonify(courses)

@lab8.route('/lab8/api/courses/<int:course_num>', methods=['GET'])
def get_course(course_num):
    if course_num not in range(0, len(str(get_courses())) - 1):
        abort(404)
    else:
        return courses[course_num]

@lab8.route('/lab8/api/courses/<int:course_num>', methods=['DELETE'])
def del_course(course_num):
    if course_num not in range(0, len(str(get_courses())) - 1):
        abort(404)
    else:
        del courses[course_num]
        return '', 204

@lab8.route('/lab8/api/courses/<int:course_num>', methods=['PUT'])
def put_course(course_num):
    if course_num not in range(0, len(str(get_courses())) - 1):
        abort(404)
    else:
        course = request.get_json()
        course[course_num] = course
        return courses[course_num]

@lab8.route('/lab8/api/courses/', methods=['POST'])
def add_course():
    course = request.get_json()
    course['created'] = (str(datetime.now()))[:10]
    courses.append(course)
    return {"num": len(courses) - 1}

    