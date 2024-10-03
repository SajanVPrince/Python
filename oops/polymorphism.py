# POLYMORPHISM
# ------------

# It Supports method overriding
# Polymorphism is often used in Class methods, where we can have multiple classes with the same method name

# 1

'''class school:
    def notes(self):
        print('notes in school')
class std(school):
    def notes(self):
        print('notes in std')
    
manu=std()
manu.notes()'''

# 2 using init constrain

'''class bank:
    def __init__(self):
        print('bank details')
class user(bank):
    def __init__(self):
        print('user details')
sbi=bank()
manu=user()'''

# 3  Using Super function

'''class school:
    def notes(self):
        print('notes in school')
class ed(school):
    def notes(self):
        super().notes()
        print('notes in ed')
class std(ed):
    def notes(self):
        super().notes()
        print('notes in std')
    
manu=std()
manu.notes()'''

# 4 using super function in __init__

'''class bank:
    def __init__(self):
        print('bank details')
class user(bank):
    def __init__(self):
        super().__init__()
        print('user details')
sbi=bank()
manu=user()'''

# 5 transfering of data

'''class school:
    def notes(self,sub):
        print('notes in school',sub)
class std(school):
    def notes(self,sub):
        super().notes(sub)
        print('notes in std')
    
manu=std()
manu.notes('py')'''