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

f=open('demo.txt','r')

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

a=f.readlines()
l=len(a)
f.seek(0)
for i in range(l):
    b=f.readline() .strip()
    c=len(b)
    print(c)
    # print(b)
    print(b[::-1])  #to reverse a number
