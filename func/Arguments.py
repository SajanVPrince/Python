# Position Arguments
# to collect arguments is called parameters
# no. of parameters = no. of arguments

# eg1:

'''def sample(a,b):
    print(a,b)
sample('a','b')
sample(10,20)
sample('a',20)
sample([1,2,3],'g')'''

# Function with a keyword

'''def sample(name,age):
    print('name : ',name)
    print('age :',age)
sample('anu',20)
sample(20,'arun')
sample(age=20,name='akhil')'''

# with default values

'''def sample(name='abc',age=20):
    print(name,age)
sample()
sample(age=23)
sample('anu')
sample('anu',30)'''

# Arbitrary arguments
'''
def sample(*a):
    print(a)

# there is no limit in adding data

sample('sajan','saj',3,2,4,21)'''

# Arbitrary Keyword arguments

'''def sample(**a):
    print(a)

sample()
sample(name='arun',age=20)'''

# TASK 1

emp=[]
def login():
    user=input('enter the USERID : ')
    password=input('enter your PASSWORD : ')
    f=0
    if user=='admin' and password=='admin':
        f=1
    return f

def add():
    id=input('enter your id : ')
    f1=0
    for i in emp:
        if i['id']==id:
            f1=1
    if f1==0:
        name=str(input('enter name : '))
        phone=int(input('enter mobile number : '))
        salary=float(input('enter the salary : '))
        dob=str(input('ente the date of birth : '))
        pos=str(input('enter the position : '))
        emp.append({'id':id,'name':name,'phone':phone,'salary':salary,'dob':dob,'pos':pos,})
    
# def view():



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
        else:
            print('invalid username or password...')
    elif c==2:
        break
    else:
        print('invalid choice')