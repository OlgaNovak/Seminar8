from addfunctions import create_db, save_db, write_student, write_grade, show_grades

def logic():
    create_db()
    print('Введите "0", если Вы являетесь учителем')
    print('Введите "1", если Вы являетесь учеником')
    flag=int(input())
    while flag==0:
        print('Введите "0", если хотите закончить')
        print('Введите "1", если хотите записать ученика')
        print('Введите "2", если хотите поставить оценку')
        choice=int(input())
        if choice=='1':
            write_student()
        elif choice=='2':
            write_grade()
        elif choice=='0':
            flag=1
    else:
        save_db()
        while flag==1:
            print('Введите фамилию ученика')
            print('Введите "0", если хотите закончить')
            surname=input()
            if surname=='0':
                flag=0
            else:
                show_grades(surname)
