'''i=1
while i<=10:
    print(i)
    i+=1'''

# task 1

'''i=int(input("enter a number : "))
while i<=5:
    print(i)
    i+=1
print("not availible")'''

# task 2

'''a=int(input("enter the amount :"))
b=int(input("enter the amount   : "))
s=0
while a<b:
    s=s+a
    a+=1
print(s)'''

# task 3

'''a=int(input("enter the starting number : "))
b=int(input("enter the ending number : "))

while a<=b:
    if a%2 !=0:
        print(a)
    a+=1'''

# task 4(Adding odd,even,and n numbers in a single loop)

'''a=int(input("Enter a number : "))
b=int(input("enter a number : "))
s=0
d=0
e=0
while a<=b:
    e+=a
    if a%2 !=0:
        s=s+a
    else:
        d=d+a
    a+=1
# e=s+d
print("Sum of odd Number :",s)
print("Sum of even Number :",d)
print("Sum of numbers :",e)'''

# task 5(multiplication table)

'''a=int(input("enter a number : "))
i=1
while i<=10:
    b=a*i
    print(f"{a}*{i}={b}")
    i+=1'''

# task 6 (itrative)

'''a='python'
i=0
l=len(a)
while i<l:
    print(a[0])
    i+=1'''

# task 7 (reverse )

'''a='sajan'
i=0
l=len(a)
b=a[::-1]
while i<l:
    print(b[i])
    i+=1'''

# task 7(reverse a number)

'''a
=int(input("Enter a number : "))
rev=0
while a>0:
    d=a%10
    print(d)
    rev=rev*10+d
    print(rev)
    a//=10
    print(a)
print('rev',rev)'''

# task 7 (fibonacci)

'''a=int(input("enter a number : "))
b=0
c=1
i=0
while i<a:
    print(b)
    d=b+c
    b=c
    c=d
    i+=1'''



