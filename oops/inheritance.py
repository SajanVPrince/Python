'''Inheritance are of 'five' types they are :'''
# 1.Single inheritance
# 2.Multiple inheritance
# 3.Multilevel inheritance
# 4.Hierarchical inheritance
# 5.Hybrid inheritance

# ---> SINGLE INHERITANCE
# ---------------------
# * with one parent class and one child class
# * parent class also called base class and child class is called derived class


'''class syn:
    def python(self):
        print('python')
    def php(self):
        print('php')

class novavi(syn):
    def dm(self):
        self.a=1
        print('dm works',self.a)
    def web(self):
        print('web_dev')

novstf1=novavi()
novstf1.dm()
novstf1.python()

std1=syn()
std1.php()'''

# MULTIPLE INHERITANCE
# --------------------

# * where it has one or more parent class
# * parent classes are not connected with each other 


# 1

'''class father:
    def shop(self):
        print('shopping')
    def car(self):
        print('car')
class mother:
    def dress_shop(self):
        print('dress shopping')
class child(father,mother):
    def bike(self):
        print('bike')

sonu=child()
sonu.bike()
sonu.car()
sonu.dress_shop()

nu=mother()
nu.dress_shop()

so=father()
so.car()'''

# 2

'''class school:
    def maths_s(self):
        print('maths')
    def physics(self):
        print('physics')
class tution:
    def english(self):
        print('english')
    def maths(self):
        print('maths')
class student(school,tution):
    def __init__(self):
        self.name=input('enter name : ')
    def sports():
        print('sports')

std1=student()
std1.maths()
std1.physics()

sch1=school()
sch1.maths_s()

tut1=tution()
tut1.english()'''

# MULTILEVEL INHERITANCE
# ----------------------

# * where it contain parent class, child class and a subchild class
# * where every subchild class is connected to the child class and every child class is connected to the parent class

# 1

'''class k_u:
    def exams(self):
        print('exams')
    def result(self):
        print('results')
class clg(k_u):
    def notes(self):
        print('notes')
class std(clg):
    def uniform(self):
        print('uniform')

sanu=std()
sanu.exams()
sanu.notes()
sanu.result()
sanu.uniform()'''

#  Hierarchical Inheritance
# -------------------------

# Where it consist of one parent class and more than one child class

# 1

'''class syn:
    def python(self):
        print('python')
    def php(self):
        print('php')
class ntech_staff(syn):
    def admission(self):
        print('admission')
class tech_staff(syn):
    def python_cls(self):
        print('python programming')

staff1=ntech_staff()
staff1.admission()
staff1.python()
staff2=tech_staff()
staff2.python()
staff2.python_cls()'''

# Hybrid Inheritance
# ------------------

# Which consist of all type of inheritance which does not have a specific pattern

# 1

'''class syn:
    def python(self):
        print('python')
    def php(self):
        print('php')
class ntech_staff(syn):
    def admission(self):
        print('admission')
class tech_staff(syn):
    def python_cls(self):
        print('python programming')
class std(tech_staff):
    def notes(self):
        print('notes')

staff1=ntech_staff()
staff1.admission()
staff1.python()
staff2=tech_staff()
staff2.python()
staff2.python_cls()
std1=std()
std1.notes()
std1.python_cls()'''

# 2

'''class g_parent():
    def pocketmoney(self):
        print('pocketmoney')
class father(g_parent):
    def car(self):
        print('car')
class mother(g_parent):
    def shopping(self):
        print('shopping')
class child(father,mother):
    def pets(self):
        print('pets')

child1=child()
child1.pets()
child1.shopping()
child1.car()
child1.pocketmoney()'''