import os
import json

def write_student():
    data=input("Введите данные (фамилию) ученика ").split()
    student_list[data[0]]=data[1:],{}


def write_grade():
    surname=input("Введите фамилию ученика: ")
    object=input("Введите название предмета: ")
    grade=input("Введите оценки через пробел: ").split()
    if student_list.get(surname) is None:
        print('Ученик с такой фамилией не найден')
        print(student_list)
    else:
        if object in student_list[surname][1]:
            student_list[surname][1][object].extend(grade)
        else:
            student_list[surname][1][object]=grade


def show_grades(surname):
    if student_list.get(surname) is None:
        print('Ученик с такой фамилией не найден')
    else:
        data=student_list[surname]
        print(f'{surname}{", ".join(data[0])}:')

def create_db():
    global student_list
    if os.stat('list_student.json').st_size==0:
        student_list={}
    else:
        student_list=json.load(open('list_student.json'))

def save_db():
    json.dump(student_list, open('list_student.json', 'w'))