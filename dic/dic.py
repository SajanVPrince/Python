# d={'name':'sajan','age':20,'place':'ekm'}
# print(d['age'])
# for i in d:
#     print(i,d[i])
# d['mark']=30
# d['age']=22
# print(d)
# if d['age']==20:
#     print('availible')
# else:
#     print('not')
# print(d.get('name1'))
# print(d.items())
# print(d.values())
# for i in d.values():
#     print(i)
# print(d.keys())
# a=d.copy()
# print(id(a))
# print(id(d))
# d['mark']=55
# print(a)
# print(d)
# d.pop('place')
# d.popitem()
# d.setdefault('age')
# l=[10,5,9]
# print(d.fromkeys(l))

# d={}
# a=input('enter the key : ')
# b=input('enter the value : ')
# d[a]=b
# print(d)

# task 1

'''shp=[]
import datetime
while True:'''
    # print('''
    # 1.Product Details
    # 2.View product
    # 3.Order Online
    # 4.Update product
    # 5.Delete product details
    # 6.Search a product
    # 7.Exit''')

'''c=int(input('Enter your Choice : '))

    if c==1:
        print('Add Products')
        pname=str(input('Enter product : '))
        pname=pname.lower()
        pid=(input('Enter Product id : '))
        pid=pid.lower()
        type=str(input('Enter the type : '))
        type=type.lower()
        price=float(input('Enter price: '))
        shp.append({'pname':pname,'pid':pid,'type':type,'price':price})

    elif c==2:
        for i in shp:
            print(i)
    
    elif c==3:
        for i in shp:
            print(i['pname'])
        print('Type the product to buy.')
        prod=input("enter the product : ")
        prod=prod.lower()
        f=0
        for i in shp:
            if i['pname']==prod:
                w=int(input('enter the amount needed..'))
                m=w*i['price']
                print('Total Price=',m)
                print('Thankyou For Shopping...')
                f=1
        if f==0:
            print('not availible')
    
    elif c==4:
        name=str(input("enter the product : "))
        name=name.lower()
        f=0
        for i in shp:
            if i['pname']==name:
                price=float(input('enter the new price : '))
                i['price']=price
                f=1
        if f==0:
            print('invalid number...')
    
    elif c==5:
        name=str(input("enter the name : "))
        name=name.lower()
        f=0
        for i in shp:
            if i['pname']==name:
                shp.remove(i)
                f=1
        if f==0:
            print('invalid number...')
    
    elif c==6:
        name=str(input("enter the name : "))
        name=name.lower()
        f=0
        for i in shp:
            if i['pname']==name:
                print('Product Name : ',i['pname'])
                print('Product ID : ',i['pid'])
                print('Product Type : ',i['type'])
                print('Product Price',i['price'])
                f=1
        if f==0:
            print('not availible')

    elif c==7:
        break
    else:
        print('choose Correct option' )'''

'''det=[]
while True:'''
    # print('''
    #       1.add
    #       2.view
    #       3.exit''')
'''c=int(input('enter the choise : '))
    if c==1:
        name=input('enter your name : ')
        age=int(input('enter your age : '))
        det.append({'name':name,'age':age})
    elif c==2:
        for i in det:
            print(i)
    elif c==3:
        break
    else:
        print('invalid')'''



# det=[{'name': 'sajan', 'age': 20},
#     {'name': 'aro', 'age': 32},
#     {'name': 'rosh', 'age': 27},
#     {'name': 'jit', 'age': 38},
#     {'name': 'jib', 'age': 24}]

'''for i in det:
    print(i['age'])

# Method 1

print('{:<10}{:<10}'.format("name","age"))
print('_'*13)
for i in det:
    print('{:<10}{:<10}' .format(i['name'],i['age']))


print('Age Under 30')
print('{:<10}{:<10}'.format("name","age"))
print('_'*13)
f=0
for i in det:
     print('{:<10}{:<10}' .format(i['name'],i['age']))
    if i['age']<=30:
        print('{:<10}{:<10}' .format(i['name'],i['age']))
        f=1
if f==0:
   print('age catogory not availible')

print('Age above 30')
print('{:<10}{:<10}'.format("name","age"))
print('_'*13)
f=0
for i in det:
    print('{:<10}{:<10}' .format(i['name'],i['age']))
    if i['age']>30:
        print('{:<10}{:<10}' .format(i['name'],i['age']))
        f=1
if f==0:
    print('age catogory not availible')''' 

# METHOD 2

'''a=[]
b=[]
for i in det:
    if i['age']<=30:
        b.append(i)
    else:
        a.append(i)
print(a)
print(b)'''

# METHOD 3

# a=[i for i in det if i['age']<=30]
# b=[i for i in det if i['age']>30]
# print(a)
# print(b)

# task 2

'''num={0:'zero',1:'one',2:'two',3:'three',4:'four',5:'five',6:'six',7:'seven',8:'eight',9:'nine'}
a=int(input('enter a number : '))
s=' '
while a>0:
    d=a%10
    s=num[d]+' '+s
    a//=10
print(s)'''

# Display from dictonary

'''l=[{'name':'a','age':20,'proj':['ems','sms']}]
# print(l[0]['proj'][0])

# Add to list
a=str(input('Enter project name : '))
l[0]['proj'].append(a)
print(l)'''

# Dictonary value swap

d={1:'one',2:'two'}
d1={}
for i in d:
    d1[d[i]]=i
print(d1)