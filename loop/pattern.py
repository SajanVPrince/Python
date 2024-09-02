# pattern

'''for i in range(3):
    for j in range(3):
        print(j,end=' ')
    print()'''

# Task 1
# 0 1 2
# 3 4 5 
# 6 7 8

'''a=0
for i in range(3):
    for j in range(3):
        print(a,end=' ')
        a+=1
    print()'''

# Task 2
# 0 1 2
# 1 2 3
# 2 3 4


'''for i in range(3):
    for j in range(3):
        print(i+j,end=' ')
    print()'''

# task 3
# 0 1 2
# 2 1 0
# 0 1 2
# 2 1 0

'''a=0
for i in range(4):
    for j in range(3):
        if i % 2 == 0:
            print(j, end=" ")
        else:
            print(2-j,end=' ')
    print()'''

# task 4
#  0
#  0 1
#  0 1 2

'''for i in range(1,4):
    for j in range(i):
        print(j,end=' ')
    print()'''

# task 5
#  0
#  1 2
#  3 4 5

'''a=0
for i in range(1,4):
    for j in range(i):
        print(a,end=' ')
        a+=1
    print()'''

# task 6
#  0
#  1 1
#  2 2 2

'''l=0
for i in range(1,4):
    for j in range(i):
        print(i-l,end=' ')
    print()'''

# task 7
#  0
#  1 0
#  2 1 0

'''l=0
for i in range(1,4):
    for j in range(i):
        print(l-j,end=' ')
    l+=1
    print()'''

