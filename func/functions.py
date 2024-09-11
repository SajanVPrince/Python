'''def sample():
    print('Welcome',a)
    print('welcome',b)
a=input('enter your name : ')
b=input('enter your name : ')
sample()
a=input('enter your name : ')
b=input('enter your name : ')
sample()
a=input('enter your name : ')
b=input('enter your name : ')
sample()'''

# scope of variable

'''def sample():
    # b=20    #local scope
    a=20    #local scope
    print(a)
    # print(b)

a=10     #global scope
print(a)
sample()
# print(b)'''

# Global keyword

'''def sample():
    global a
    a=10
    print(a)
sample()
print(a)'''

# Return Keyword

'''def sample():
    a=10
    b=19
    return 'WELCOME',a,b
a,b,c=sample()
print(a)
print(b)
print(c)'''

# Task 1

'''def num():
    a=int(input('enter a number : '))
    b=int(input('enter a number : '))
    return a,b
while True:
    print(''''''
    1. add
    2. sub
    3. mul
    4. divi
    5. exit'''''')

    c=int(input('enter the number : '))
    if c==1:
        a,b=num()
        print(a+b)
    elif c==2:
        a,b=num()
        print(a-b)
    elif c==3:
        a,b=num()
        print(a*b)
    elif c==4:
        a,b=num()
        print(a//b)
    elif c==5:
        break
    else:
        print('Choose Correct number')'''