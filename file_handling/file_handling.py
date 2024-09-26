# Modes in file handling
# ----------------------

# 1.create(x)
# 2.read(r)
# 3.write(w)
# 4.append(a)

# synatx
# ------

# open('file_name','modes')

# EXAMPLE
# -------

# f=open('demo.txt','x')
# f.write('Welcome')
# f.write(' all')


# Methods in file handling
# ------------------------

# 1.write
# 2.read
# 3.readline
# 4.readlines
# 5.seek (to change cursor position)
# 6.tell (to know where the cursor is)

# Created a File

# f=open('demo.txt','x')

# File to be readed by using read mode

# f=open('demo.txt','r')

# READ
# ----

# f.write('Sajan')
# f.write(' v.')
# f.write(' prince')
# a=f.read()
# print(a)

# SEEK

# f.seek(5)

# b=f.read(1)
# print(b)

# READLINE
# --------

# a=f.readline(3)
# print(a)
# b=f.readline(1)
# print(b)
# c=f.readline()
# print(c)

# READLINES
# ---------
# readlines is also used to find how many lines are in a file using len()

# a=f.readlines()
# print(a)
# print(len(a))

# TELL

# print(f.tell())

# print lines using for loop

# to find letters in a file and reverse the letters
# -------------------------------------------------

# a=f.readlines()
# l=len(a)
# f.seek(0)
# letter=0
# capital=0
# for i in range(l):
#     b=f.readline() .strip()
#     # print(b[::-1])  #to reverse a number
#     for i in b:
#         if i!=' ':
#             letter+=1
#     print(letter)


# to find capital and small letters
# ---------------------------------

# a=f.readlines()
# l=len(a)
# f.seek(0)
# letter=0
# cap=0
# for i in range(l):
#     b=f.readline() .strip()
#     for i in b:
#         print(i)
#         if i!=' ':
#             letter+=1
#             if i.isupper():
#                 cap+=1
            
# print('capital',cap)
# print('small',letter-cap)

# to find words in a txt file
# ---------------------------

# a=f.readlines()
# l=len(a)
# f.seek(0)
# w=0
# for i in range(l):
#     b=f.readline() .strip()
#     s=b.split(' ')
#     for j in s:
#         if j!='':
#             w+=1
# print(w)

# WRITE
# -----

# if already file exists it will over write the content

f=open('demo.txt','w')
# f.write('welcome\n')
# f.write('123\n')
# f.write('hi '+'hello\n')

# if file doesn't exist it will create a new file and write the content

# f=open('test.txt','w')
# f.write('welcome\n')
# f.write('123\n')
# f.write('hi '+'hello\n')

a=int(input('enter a number : '))
for i in range(1,11):
    x=a*i
    x=str(x)
    f.write(f"{a} x {i} = {x}\n")
