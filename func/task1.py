def register():
    print('Registration Page')
    email=input('enter your email :')
    f=0
    for i in user:
        if i['email']==email:
            f=1
            register()
    if f==0:
        name=str(input('enter your name : '))
        id=int(input('enter an id : ')) 
        username=email
        phone=int(input('enter your number : '))
        password=input('enter the password : ')
        user.append({'id':id,'name':name,'email':email,'username':username,'phone':phone,'password':password})

user=[]
lib=[]
while True:
    print('''
    1.Register as User
    2.Login
    3.EXIT''')
    c=int(input('enter your choice : '))
    if c==1:
        register()
    for i in user:
        print(i)
