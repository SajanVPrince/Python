# check whether the number is same or not 

'''a=int(input("enter a number : "))
b=int(input("enter a number : "))
if a==b:
    print("True")
else:
    print("Flase")'''

# Check which is the largest number

'''a=int(input("enter a number : "))
b=int(input("enter a number : "))
if a>b:
    print("Largest Number :",a)
else:
    print("Largest Number :",b)'''

# largest of three numbers using nested if

'''a=int(input("Enter a number"))
b=int(input("Enter a number"))
c=int(input("Enter a number"))
if a>b:
    if a>c:
        print("Largest is ",a)
    else:
        print("largest is ",c)
else:
    if b>c:
        print("largest is ",b)
    else:
        print("largest is ",c)'''

# Task 1

'''s=int(input("Enter Your Salary :"))
e=int(input("How many years of service do you have? :"))

if e>5:
    a=s*5/100
    ts=a+s
    print("Total Salary is :",ts)
    print("Bonus",a)
else:
    print("Total Salary is :",s)
    print("Bonus = 0")'''

# Task 2

'''u=int(input("Enter your electricity unit : "))

if u<100:
    print("Your unit price = 0")
else:
    if u<200 and u>100:
        up=u-100
        ua=up*5
        print("your unit price is",ua)
    else:
        ui=u-200
        us=ui*10+500
        # 500 default value of 100 unit when it is 5/unit
        print("Your unit price is",us)'''

# Task 3

'''a=int(input("Enter a number between 1 to 7 : "))

if a==1:
    print("Sunday")
elif a==2:
    print("Monday")
elif a==3:
    print("Tuesday")
elif a==4:
    print("Wednesday")
elif a==5:
    print("Thursday")
elif a==6:
    print("Friday")
elif a==7:
    print("Saturday")
else:
    print("Invalid Number")'''


# Task 4


'''a=input("enter your city : ")
a=a.lower()
print(a)

if a=='delhi':
    print("monuments is : 'Redfort'")
elif a=="agra":
    print("monuments is : 'Taj Mahal'")
elif a=="jaipur":
    print("monuments is : 'jal mahal'")
else:
    print("Invalid")'''

# Task 5

a=int(input("enter a number : "))
a=a%10
b=a%3
if a==0:
    print("the entered number is not divisible by 3")
elif b==0:
    print("the entered number is divisible by 3")
else:
    print("the number is not divisible by 3")

# Task 6

'''a=int(input("enter the price : "))

if a>100000:
    b=a*15/100
    total=a+b
    print(f"Ex- Showroom Price = {a} and tax amount is ={b}")
    print("Total Amount is = ",total)
elif a>50000 and a<=100000:
    b=a*10/100
    total=a+b
    print(f"Ex- Showroom Price = {a}and tax amount is ={b}")
    print("Total Amount is = ",total)
else:
    b=a*5/100
    total=a+b
    print(f"Ex- Showroom Price = {a}and tax amount is ={b}")
    print("Total Amount is = ",total)'''