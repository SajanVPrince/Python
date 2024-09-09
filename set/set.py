# introduction

'''s={1,3,4,5,6,'abc',2.0,8,9}
for i in s:
    print(i)
if 7 in s:
    print('true')
else:
    print('false')'''

# l=[1,2,3,4,5,1,2,3,4]
# s=set(l)
# l=list(s)
# print(l)

# Set Methods
# add,delete

'''s=set()
s.add()
s={10,11,12}
s.pop()
s.discard()
s.remove()
s.clear()
s.copy()
print(s)'''

'''s={1,2,3,4,5}
s1={1,2,3,4,5,6}
# print(s.difference(s1))
# print(s.union(s1))
# print(s.intersection(s1))
# print(s.symmetric_difference(s1))
s2={6,7,8}
# print(s.isdisjoint(s2))
# print(s.issubset(s1))
# print(s.issuperset(s1))
# print(s.update({10,11,12}))
# print(s)
# print(s.difference_update(s1))'''

# TASK 1

'''s=set()
a=int(input('enter the limit : '))
for i in range(a):
    b=str(input('enter the name : '))
    s.add(b)
print(s)'''

# TASK 2

php=set()
a=int(input('enter the limit : '))
for i in range(a):
    b=str(input('enter the name : '))
    php.add(b)

python=set()
a=int(input('enter the limit : '))
for i in range(a):
    b=str(input('enter the name : '))
    python.add(b)

java=set()
a=int(input('enter the limit : '))
for i in range(a):
    b=str(input('enter the name : '))
    java.add(b)

print('php = ',php)
print('python = ',python)
print('java = ',java)
