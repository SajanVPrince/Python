# Functions

def register():
    print('Registration Page')
    if len(user)==0:
        id=1000
    else:
        id=user[-1]['id']+1
    email=str(input('enter your email :'))
    f=0
    for i in user:
        if i['email']==email:
            f=1
            print('email already exists enter another one')
            register()
    if f==0:
        name=str(input('enter your name : '))
        phone=int(input('enter your number : '))
        password=input('enter the password : ')
        print('Registration Succesfull email id is your username')
        user.append({'id':id,'name':name,'email':email,'phone':phone,'password':password})

def login():
    usern=input('Enter Username : ')
    passw=input('Enter password : ')
    f=0
    u=''
    if usern=='admin' and passw=='admin':
        f=1
    for i in user:
        if usern==i['email'] and passw==i['password']:
            f=2
            u=i
    return f,u

def add():
    print('ADD BOOK')
    if len(lib)==0:
        id=1
    else:
        id=lib[-1]['id']+1
    name=str(input('enter name : '))
    price=int(input('enter the price : '))
    stock=int(input('enter the stock availible : '))
    lib.append({'id':id,'name':name,'price':price,'stock':stock})

# Fuctions end

user=[{'id': 1000, 'name': 'sajan', 'email': 's@','phone': 920712, 'password': 'asdf'}]
lib=[]
while True:
    print('''
    1.Register as User
    2.Login
    3.EXIT''')
    c=int(input('enter your choice : '))
    if c==1:
        register()
    elif c==2:
        f,u=login()
        if f==1:
            while True:
                print('''
                1.Add book
                2.View Book
                3.Update Book Details
                4.Delete book
                5.View Users
                6.Logout''')

                c1=int(input('enter your choice : '))
                if c1==1:
                    add()
        elif f==2:
            print('user login')
        else:
            print('invalid username or password')
    elif c==3:
        break
    else:
        print('Invalid Choice')
