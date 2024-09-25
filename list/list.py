'''l=[1,2,10,20,'abc',1]
print(l[0])
print(l[1])
if 10 in l:
    print('availible')
else:
    print('not availible')
for i in l:
    print(i)
l[1]=7
print(l)'''

# list method
# adding

'''l=[]
l.append(10)
l.append('abc')
l.append([21,80,90])
if 10 in l:
    print('availible')
else:
    print('not availible')
l.extend([444,555,666])
l.insert(3,7)
print(l)'''

# delete

'''l=[10,20,30]
l.remove(30)
l.pop(0)
l.clear()
print(l)'''

# index,sort(ascending),reverse

'''l=[7,4,6,10,9,7]
print(l.index(10))
print(l.count(7))
l.sort()
l.reverse()
print(l)'''


# add list elements

'''l=[1,10,12,'abc',8.5]
s=0
for i in l:
    if type(i)==int or type(i)==float:
        s+=i 
print(s)'''

# sum of odd and even

'''l=[10,1,2,3,5,8,6]
o=0
e=0
for i in l:
    if i%2!=0:
        o+=i
    else:
        e+=i
print('Sum of odd numbers = ',o)
print('Sum of even numbers = ',e)'''

# unique

        # using membership opertor

'''l=[10,1,2,3,5,8,6,1,3,8]
u=[]
# l.sort()
for i in l:
    if i not in u:
        u.append(i)
print(u)'''

        # using set

'''l=[10,1,2,3,5,8,6,1,3,8]

s=set(l)
l=list(s)
print(l)'''

        # using count
    
'''l=[10,1,2,3,5,8,6,1,3,8]

for i in l:
    if l.count(i)>=2:
        l.remove(i)
print(l)'''

# task 1

'''l=['apple','malayalam','amma','python']
for i in l:
    rev=i[::-1]
    if rev==i:
        print(rev,'its a palindrome')
    else:
        print(rev,'its not a palindrome')'''
    
# task 2

'''l=[1,3,2,7,6,9]
for i in l:
    if i%3==0:
        print(i,'is divisibe by 3')
    else:
        print(i,'not divisible by 3')'''

# task 3

# while True:
#     print('''
#         1.add
#         2.sub
#         3.mul
#         4.div
#         5.exit''')
    
'''c=int(input('enter the function you need : '))
    if c==1:
        a=int(input('enter the first number : '))
        b=int(input('enter the second number : '))
        d=a+b
        print(f"{a}+{b}={d}")
    elif c==2:
        a=int(input('enter the first number : '))
        b=int(input('enter the second number : '))
        d=a-b
        print(f"{a}-{b}={d}")
    elif c==3:
        a=int(input('enter the first number : '))
        b=int(input('enter the second number : '))
        d=a*b
        print(f"{a}*{b}={d}")
    elif c==4:
        a=int(input('enter the first number : '))
        b=int(input('enter the second number : '))
        d=a/b
        print(f"{a}/{b}={d}")
    elif c==5:
        break
    else:
        print('enter a valid number')'''

# task 4

# std=[]
# while True:
#     print('''
#           1.add Student
#           2.view student
#           3.update student
#           4.delete student
#           5.exit''')
    
'''c=int(input('enter the choice : '))
    if c==1:
        name=str(input("enter the name : "))
        age=int(input("enter the age : "))
        mark=int(input("enter the mark : "))
        std.append([name,age,mark])

    elif c==2:
        for i in std:
            print(i)
    
    elif c==3:
        name=str(input("enter the name : "))
        f=0
        for i in std:
            if name in i:
                mark=int(input('enter the mark : '))
                i[2]=mark
                f=1
        if f==0:
            print('invalid number...')
    elif c==4:
        name=str(input("enter the name : "))
        f=0
        for i in std:
            if name in i:
                std.remove(i)
                f=1
        if f==0:
            print('invalid number...')
    elif c==5:
        break
else:
    print('invalid choice')'''

# task Employee

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
        if name not in emp:
            print('not Availible')
        else:    
            for i in emp:
                if name in i:
                    print(i)
        print('select an id to update..')
        for i in emp:
            empid=int(input('enter the id : '))
            f=0
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
            if f==0:
                print('invalid id')

    elif c==4:
        print('Delete the data')
        name=str(input("enter the name : "))
        # f=0
        if name not in emp:
            print('not Availible')
        else:
            
            for i in emp:
                if name in i:
                    print(i)
            print('select an id to delete..')
        for i in emp:
            empid=int(input('enter the id : '))
            f=0
            if empid in i:
                emp.remove(i)
                f=1
            if f==0:
                print('invalid number...')

    elif c==5:
        print('search an employee')
        name=str(input("enter the name : "))
        if name not in emp:
            print('not Availible')
        else:
            for i in emp:
                if name in i:
                    print(i)
            print('select an id..')
        for i in emp:
            empid=int(input('enter the id : '))
            if empid in i:
                print('Employee ID : ',emp[1])
                print('Name : ',emp[0])
                print('Age : ',emp[2])
                print('Place : ',emp[3])
                print('Position : ',emp[5])
                print('Experience: ',emp[6])
    elif c==6:
        while True:
            print('Assign work..')
            id=int(input('enter an id : '))
            for i in emp:
                if id in i:
                    task=input('Enter the name of task : ')
                    date=datetime.datetime.now().strftime('%x')
                    i.append([task,date])
            print(emp)
    elif c==7:
        break
    else:
        print('invalid option')
                    

    
                
            
           
