from add import *
from sub import *
from num import *
from mul import *
from div import *
from mod import *
from invalid import *
while True:
    print('''
        1.Add
        2.Subtract
        3.multiply
        4.divide
        5.modules
        6.exit''')
    
    c=int(input('enter your choice : '))
    if c==1:
        a,b=number()
        add(a,b)
    elif c==2:
        a,b=number()
        sub(a,b)
    elif c==3:
        a,b=number()
        mul(a,b)
    elif c==4:
        a,b=number()
        div(a,b)
    elif c==5:
        a,b=number()
        mod(a,b)
    elif c==6:
        break
    else:
        invalid()