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