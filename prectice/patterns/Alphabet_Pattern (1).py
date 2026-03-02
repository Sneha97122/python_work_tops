# A 
# B C 
# D E F
# G H I J
ch=1 
for i in range(1,5):
    for j in range(i):
        print(chr(64+ch),end=" ")
        ch+=1 
    print()

print('-----------------------------------------------')

# G H I J
# D E F
# B C
# A
ch=10 
for i in range(4,0,-1):
    start=ch-i+1 
    for j in range(start, ch+1):
        print(chr(64+j),end=" ")
    print()
    ch-=i


print('------------------------------------------')

# A
# B B
# C C C
# D D D D
for i in range(1,5):
    for j in range(i):
        print(chr(64+i),end=" ")
        ch+=1 
    print()

print('--------------------------------------')

# D D D D
# C C C
# B B
# A
ch=10 
for i in range(4,0,-1):
    for j in range(i):
        print(chr(64+i),end=" ")
        ch-=1 
    print()

print('-----------------------------------------')

# A
# A B 
# A B C 
# A B C D
ch=1 
for i in range(1,5):
    for j in range(1,i+1):
        print(chr(64+j),end=" ")
        ch+=1 
    print()

print('-------------------------------------------')

# A B C D
# A B C
# A B
# A

ch=10 
for i in range(4,0,-1):
    for j in range(1,i+1):
        print(chr(64+j),end=" ")
        ch-=1 
    print()

print('------------------------------------------------')

#         A
#       B C
#     D E F
#   G H I J

ch=1 
for i in range(1,5):
    for k in range(5-i):
        print(" ",end=" ")
    for j in range(i):
        print(chr(64+ch),end=" ")
        ch+=1
    print()

print('----------------------------------------------')

# G H I J
#   D E F
#     B C
#       A
ch=10 
for i in range(4,0,-1):
    for k in range(4-i):
        print(" ",end=" ")
    start=ch-i+1
    for j in range(start,ch+1):
        print(chr(64+j),end=" ")
    print()
    ch-=i 

print('--------------------------------------------------------')

#         A
#       B B
#     C C C
#   D D D D
for i in range(1,5):
    for k in range(5-i):
        print(" ",end=" ")
    for j in range(i):
        print(chr(64+i),end=" ")
    print()

print('------------------------------------------')

# D D D D
#   C C C
#     B B
#       A
ch=10 
for i in range(4,0,-1):
    for k in range(4-i):
        print(" ",end=" ")
    for j in range(i):
        print(chr(64+i),end=" ")
        ch-=1 
    print()

print('---------------------------------------')

#         A
#       A B
#     A B C
#   A B C D
for i in range(1,5):
    for k in range(5-i):
        print(" ",end=" ")
    for j in range(1,i+1):
        print(chr(64+j),end=" ")
    print()

print('-------------------------------------------')

# A B C D
#   A B C
#     A B
#       A 
ch=10 
for i in range(4,0,-1):
    for k in range(4-i):
        print(" ",end=" ")
    for j in range(1,i+1):
        print(chr(64+j),end=" ")
        ch-=1 
    print()







