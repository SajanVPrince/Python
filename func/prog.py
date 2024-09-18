# Task 1

emp=[]
def login():
    user=input('enter the USERID : ')
    password=input('enter your PASSWORD : ')
    f=0
    if user=='admin' and password=='admin':
        f=1
    for i in emp:
        if user.isdigit():
            user=int(user)
            if user==i['id'] and password==i['dob']:
                f=2
    return f

def add():
    id=int(input('enter your id : '))
    f1=0
    for i in emp:
        if i['id']==id:
            f1=1
            add()
    if f1==0:
        name=str(input('enter name : '))
        phone=int(input('enter mobile number : '))
        salary=float(input('enter the salary : '))
        dob=str(input('ente the date of birth : '))
        pos=str(input('enter the position : '))
        emp.append({'id':id,'name':name,'phone':phone,'salary':salary,'dob':dob,'pos':pos,})
    
def view():
    for i in emp:
        print(i)

def update():
    id=input('enter your id : ')
    f1=0
    for i in emp:
        if i['id']==id:
            f1=1
            salary=float(input('enter the salary : '))
            pos=str(input('enter the position : '))
            i['salary']=salary
            i['pos']=pos
            print('details updated')
    if f1==0:
        print('invalid ID')

def delete():
    id=input('enter your id : ')
    f1=0
    for i in emp:
        if i['id']==id:
            f1=1
            emp.remove(i)
            print('user deleted')
    if f1==0:
        print('invalid ID')


while True:
    print('''
    1.Login
    2.EXIT
    ''')
    c=int(input('Enter your choice : '))
    if c==1:
        f=login()
        if f==1:
            while True:
                print('''
                1.Add Employe
                2.View Employe
                3.Update Employe
                4.Delete Employe
                5. LOGOUT
                ''')
                c1=int(input('enter your choice : '))
                if c1==1:
                    add()
                elif c1==2:
                    view()
                elif c1==3:
                    update()
                elif c1==4:
                    delete()
                elif c1==5:
                    break
                else:
                    print('invalid Selection')
        elif f==2:
            print('user login')
        else:
            print('invalid username or password...')
    elif c==2:
        break
    else:
        print('invalid choice')