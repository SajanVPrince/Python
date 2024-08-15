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

a=int(input("enter a number : "))
i=1
while i<=10:
    b=a*i
    print(f"{a}*{i}={b}")
    i+=1
    

