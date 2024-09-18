# Position Arguments
# to collect arguments is called parameters
# no. of parameters = no. of arguments

# eg1:

'''def sample(a,b):
    print(a,b)
sample('a','b')
sample(10,20)
sample('a',20)
sample([1,2,3],'g')'''

# Function with a keyword

'''def sample(name,age):
    print('name : ',name)
    print('age :',age)
sample('anu',20)
sample(20,'arun')
sample(age=20,name='akhil')'''

# with default values

'''def sample(name='abc',age=20):
    print(name,age)
sample()
sample(age=23)
sample('anu')
sample('anu',30)'''

# Arbitrary arguments
'''
def sample(*a):
    print(a)

# there is no limit in adding data

sample('sajan','saj',3,2,4,21)'''

# Arbitrary Keyword arguments

'''def sample(**a):
    print(a)

sample()
sample(name='arun',age=20)'''
