d={'name':'sajan','age':20,'place':'ekm'}
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

shp=[{'pname': 'apple', 'pid': 'a1001', 'type': 'fruits', 'price': 160.0},{'pname': 'orange', 'pid': 'o1001', 'type': 'fruits', 'price': 160.0}]
import datetime
while True:
    print('''
    1.Product Details
    2.View product
    3.Order Online
    4.Update product
    5.Delete product details
    6.Search a product
    7.Exit''')

    c=int(input('Enter your Choice : '))

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
        print('choose Correct option' )


        


