emp=[]
id=1000
import datetime
while True:
    print('''
    1.Register as new
    2.View employee
    3.Update the details
    4.Delete the details
    5.Search an employee
    6.Assign Work
    7.Exit''')

    c=int(input('Enter your Choice : '))

    if c==1:
        print('Register here...')
        name=str(input('Enter your name : '))
        id+=1
        empid=id
        age=int(input('Enter your age : '))
        place=str(input('Enter your place : '))
        salary=int(input('Enter Your Salary : '))
        position=str(input('Enter your position : '))
        exp=str(input('Enter your experience : '))
        emp.append([name,id,age,place,salary,position,exp])

    elif c==2:
        print('Our Employess')
        for i in emp:
            print(i)

    elif c==3:
        print('Update the details')
        name=str(input("enter the name : "))
        if name in emp:
                for i in emp:
                    print(i)
                    print('select an id to update..')
                    empid=int(input('enter the id : '))
                    # f=0
                    while True:
                        print('Select the item to be updated')
                        print('''
                            1.salary
                        2.position
                        3.exp
                        4.exit''')
        
                        u=int(input('enter your choice : '))
                        if u==1:
                            salary=int(input('enter your new salary : '))
                            i[4]=salary
                            f=1
                        elif u==2:
                            position=int(input('enter your new position: '))
                            i[5]=position
                            f=1
                        elif u==3:
                            exp=int(input('enter your new exp: '))
                            i[6]=exp
                            f=1
                        elif u==4:
                            break
                        else:
                            print('invalid choice')
                    # if f==0:
                    #     print('invalid id')