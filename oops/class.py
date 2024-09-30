# There are different types of oops concept
# -->.class
# -->.object
# -->.Attribute
# -->.Methods
# -->.Inheritance
# -->.Polymorphism
# -->.Encapsulation
# -->.Abstraction

# CLASS
# -----

'''* its a blue print to create objects
* it is also called user-defined data type'''

# Syntax
# ------

# class class_name:
#     Statement

'''Objects are the insistence of a class '''

# EXAMPLE :

'''class syn:
    def python():
        print('python')
    def php():
        print('php')
    def java():
        print('java')
sajan=syn
sajan.python()'''

class Bank:
    def __init__(self):
        self.name=input('Enter your name : ')
        self.age=int(input('enter your age : '))
        self.bal=0
    
    def deposit(self,amt):
        self.bal+=amt
        print('Deposit')
    def withdraw(self,amt):
        self.bal-=amt
        print('Withdraw')
    def balance(self):
        print('balance : ',self.bal)

obj=Bank()
obj.deposit(5000)
obj.balance()
obj.withdraw(2764)
obj.balance()

obj1=Bank()
obj1.deposit(4000)
obj1.balance()



