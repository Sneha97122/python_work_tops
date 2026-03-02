# 1 
# 2 3 
# 4 5 6
# 7 8 9 10
num=1 
for i in range(1,5):
    for j in range(i):
        print(num,end=" ")
        num+=1 
    print()

print('-------------------------------------------')

# 1
# 2 2
# 3 3 3
# 4 4 4 4
# 5 5 5 5 5
for i in range(1,6):
    for j in range(i):
        print(i,end=" ")
    print()

print('--------------------------------------------------')

# 1
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5
for i in range(1,6):
    for j in range(1,i+1):
        print(j,end=" ")
    print()

print('---------------------------------------------')

# 7 8 9 10
# 4 5 6
# 2 3
# 1
num=10 
for i in range(4,0,-1):
    for j in range(i):
        print(num-(i-j-1),end=" ")
    num-=i
    print()

print('-------------------------------------------')

# 6 6 6 6 6 6
# 5 5 5 5 5
# 4 4 4 4
# 3 3 3 
# 2 2
# 1
for i in range(6,0,-1):
    for j in range(i):
        print(i,end=" ")
    print()

print("--------------------------------------------------")

# 1 2 3 4 5 
# 1 2 3 4
# 1 2 3
# 1 2
# 1
for i in range(5,0,-1):
    for j in range(1,i+1):
        print(j,end=" ")
    print()

print('---------------------------------------------')

#         1
#       2 3
#     4 5 6
#   7 8 9 10
num=1 
for i in range(1,5):
    for k in range(5-i):
        print(" ",end=" ")
    for j in range(i):
        print(num,end=" ")
        num+=1 
    print()

print('------------------------------------------------')

#         1
#       2 2
#     3 3 3
#   4 4 4 4
for i in range(1,5):
    for k in range(5-i):
        print(" ",end=" ")
    for j in range(i):
        print(i,end=" ")
    print()

print('--------------------------------------------')

#         1
#       1 2
#     1 2 3
#   1 2 3 4
for i in range(1,5):
    for k in range(5-i):
        print(" ",end=" ")
    for j in range(1,i+1):
        print(j,end=" ")
    print()

print('----------------------------------------------')

#     1
#    2 3
#   4 5 6
#  7 8 9 10
num=1 
for i in range(1,5):
    for k in range(5-i):
        print("",end=" ")
    for j in range(i):
        print(num,end=" ")
        num+=1 
    print()

print('-----------------------------------------------------')

#      1
#     2 2
#    3 3 3
#   4 4 4 4
#  5 5 5 5 5

for i in range(1,6):
    for k in range(6-i):
        print("",end=" ")
    for j in range(i):
        print(i,end=" ")
    print()

print('------------------------------------------------')

#      1
#     1 2 
#    1 2 3
#   1 2 3 4
#  1 2 3 4 5
for i in range(1,6):
    for k in range(6-i):
        print("",end=" ")
    for j in range(1,i+1):
        print(j,end=" ")
    print()

print('-------------------------------------------------')

# 7 8 9 10
#  4 5 6
#   2 3
#    1
num=10 
for i in range(4,0,-1):
    for k in range(4-i):
        print("",end=" ")
    for j in range(i):
        print(num-(i-j-1),end=" ")
    num-=i
    print()

print('--------------------------------------------')

# 5 5 5 5 5
#  4 4 4 4
#   3 3 3
#    2 2
#     1
for i in range(5,0,-1):
    for k in range(5-i):
        print("",end=" ")
    for j in range(i):
        print(i,end=" ")
    print()

print('--------------------------------------------')

# 1 2 3 4 5
#  1 2 3 4
#   1 2 3
#    1 2
#     1
for i in range(5,0,-1):
    for k in range(5-i):
        print("",end=" ")
    for j in range(1,i+1):
        print(j,end=" ")
    print()

print('-------------------------------------------')

#    1
#   2 3
#  4 5 6
# 7 8 9 10
#  4 5 6
#   2 3
#    1
num=1 
for i in range(1,4):
    for k in range(4-i):
        print("",end=" ")
    for j in range(i):
        print(num,end=" ")
        num+=1 
    print()
num=10 
for i in range(4,0,-1):
    for k in range(4-i):
        print("",end=" ")
    for j in range(i):
        print(num-(i-j-1),end=" ")
    num-=i
    print()

print('--------------------------------------------------------')

#     1
#    2 2
#   3 3 3
#  4 4 4 4
# 5 5 5 5 5
#  4 4 4 4
#   3 3 3
#    2 2
#     1
for i in range(1,5):
    for k in range(5-i):
        print("",end=" ")
    for j in range(i):
        print(i,end=" ")
    print()
for i in range(5,0,-1):
    for k in range(5-i):
        print("",end=" ")
    for j in range(i):
        print(i,end=" ")
    print()

print('------------------------------------------------')

#     1
#    1 2
#   1 2 3
#  1 2 3 4
# 1 2 3 4 5
#  1 2 3 4
#   1 2 3
#    1 2
#     1
for i in range(1,5):
    for k in range(5-i):
        print("",end=" ")
    for j in range(1,i+1):
        print(j,end=" ")
    print()
for i in range(5,0,-1):
    for k in range(5-i):
        print("",end=" ")
    for j in range(1,i+1):
        print(j,end=" ")
    print()
    



