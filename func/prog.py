# Task 1

emp=[{'id': 1, 'name': 'a', 'phone': 3, 'salary': 4.0, 'dob': '2/2', 'pos': 'hr','password':'2/2'}]
def login():
    user=input('enter the USERID : ')
    password=input('enter your PASSWORD : ')
    f=0
    u=''
    if user=='admin' and password=='admin':
        f=1
    for i in emp:
        if user.isdigit():
            user=int(user)
            if user==i['id'] and password==i['password']:
                f=2
                u=i
    return f,u

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
        password=dob
        emp.append({'id':id,'name':name,'phone':phone,'salary':salary,'dob':dob,'pos':pos,'password':password})
    
def view():
    # print("{:<5}{:<10}{:<10}{:<10}{:<10}{:<10}".format('ID','NAME','PHONE','SALARY','DOB','POSITION'))
    # print('_'*45)
    # for i in emp:
    #     print("{:<5}{:<10}{:<10}{:<10}{:<10}{:<10}".format(i['id'],i['name'],i['phone'],i['salary'],i['dob'],i['position']))
    for i in emp:
        print(i)
        
def update():
    id=int(input('enter your id : '))
    f1=0
    for i in emp:
        if i['id']==id:
            salary=float(input('enter the salary : '))
            pos=str(input('enter the position : '))
            i['salary']=salary
            i['pos']=pos
            print('details updated')
            f1=1
    if f1==0:
        print('invalid ID')

def delete():
    id=int(input('enter your id : '))
    f1=0
    for i in emp:
        if i['id']==id:
            emp.remove(i)
            print('user deleted')
            f1=1
    if f1==0:
        print('invalid ID')

def profile(u):
    print('WELCOME',u['name'])
    print('DETAILS')
    print('USER ID : ',u['id'])
    print('NAME : ',u['name'])
    print('PHONE : ',u['phone'])
    print('SALARY : ',u['salary'])
    print('DATE OF BIRTH : ',u['dob'])
    print('POSITION : ',u['pos'])


def upd_user(u):
    name=str(input('enter name : '))
    phone=int(input('enter mobile number : '))
    dob=str(input('ente the date of birth : '))
    u['name']=name
    u['phone']=phone
    u['dob']=dob
    print('Profile Updated..')



while True:
    print('''
    1.Login
    2.EXIT
    ''')
    c=int(input('Enter your choice : '))
    if c==1:
        f,u=login()
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
            if u['dob']==u['password']:
                password=input('enter a new password : ')
                u['password']=password

            while True:
                print('''
                1.View Profile
                2.Update Profile
                3.Logout
                ''')
                c1=int(input('enter your choice : '))
                if c1==1:
                    profile(u)
                elif c1==2:
                    upd_user(u)
                elif c1==3:
                    break
                else:
                    print('invalid Choice')
        else:
            print('invalid username or password...')
    elif c==2:
        break
    else:
        print('invalid choice')