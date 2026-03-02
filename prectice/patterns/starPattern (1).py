# *
# * *
# * * *
# * * * *
# * * * * *
for i in range(1,6):
    for j in range(i):
        print("*",end=" ")
    print()

print('-----------------------------------------')

# * * * * * *
# * * * * *
# * * * *
# * * *
# * *
# *
for i in range(6,0,-1):
    for j in range(i):
        print("*",end=" ")
    print()

print("---------------------------------------------------")

#           *
#         * *
#       * * *
#     * * * *
#   * * * * *
for i in range(1,6):
    for k in range(6-i):
        print(" ",end=" ")
    for j in range(i):
        print("*",end=" ")
    print()

print("--------------------------------------")

# * * * * * *
#   * * * * *
#     * * * *
#       * * *
#         * *
#           *
for i in range(6,0,-1):
    for k in range(6-i):
        print(" ",end=" ")
    for j in range(i):
        print("*",end=" ")
    print()

print("-------------------------------------------")

#           *
#         * * *
#       * * * * *
#     * * * * * * *
#   * * * * * * * * *
for i in range(1,6):
    for k in range(6-i):
        print(" ",end=" ")
    for j in range(2*i-1):
        print("*",end=" ")
    print()


print('----------------------------------------------')

# * * * * * * * * * * *
#   * * * * * * * * *
#     * * * * * * *
#       * * * * *
#         * * *
#           *
for i in range(6,0,-1):
    for k in range(6-i):
        print(" ",end=" ")
    for j in range(2*i-1):
        print("*",end=" ")
    print()

print("-------------------------------------------")

#           *
#         * * *
#       * * * * *
#     * * * * * * *
#   * * * * * * * * *
# * * * * * * * * * * *
#   * * * * * * * * *
#     * * * * * * *
#       * * * * *
#         * * *
#           *
for i in range(1,6):
    for k in range(6-i):
        print(" ",end=" ")
    for j in range(2*i-1):
        print("*",end=" ")
    print()
for i in range(6,0,-1):
    for k in range(6-i):
        print(" ",end=" ")
    for j in range(2*i-1):
        print("*",end=" ")
    print()

print('-----------------------------------------')

# * * * * * * * * * * *
#   * * * * * * * * * 
#     * * * * * * *
#       * * * * *
#         * * *
#           *
#         * * *
#       * * * * *
#     * * * * * * *
#   * * * * * * * * *
# * * * * * * * * * * *
for i in range(6,0,-1):
    for k in range(6-i):
        print(" ",end=" ")
    for j in range(2*i-1):
        print("*",end=" ")
    print()
for i in range(2,7):
    for k in range(6-i):
        print(" ",end=" ")
    for j in range(2*i-1):
        print("*",end=" ")
    print()

print('-----------------------------------------------')

# *                     *
# * *                 * *
# * * *             * * *
# * * * *         * * * *
# * * * * *     * * * * *
# * * * * * * * * * * * *
# * * * * * * * * * * * *
# * * * * *     * * * * *
# * * * *         * * * *
# * * *             * * *
# * *                 * *
# *                     *
for i in range(1,6+1):
    for j in range(i):
        print("*",end=" ")
    for k in range(2*(6-i)):
        print(" ",end=" ")
    for j in range(i):
        print("*",end=" ")
    print()
for i in range(6,0,-1):
    for j in range(i):
        print("*",end=" ")
    for k in range(2*(6-i)):
        print(" ",end=" ")
    for j in range(i):
        print("*",end=" ")
    print()

print('-----------------------------------------------')

# * * * * * *
# *         *
# *         *
# *         * 
# *         *
# * * * * * *
for i in range(6):
    for j in range(6):
        if i==0 or j==0 or i==5 or j==5:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()

print("-----------------------------------------------")

# *
# * *
# *   *
# *     *
# *       *
# * * * * * *
for i in range(6):
    for j in range(6):
        if j==0 or j==i or i==5:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()

print('-------------------------------------------')

# * * * * * *
# *       *
# *     *
# *   *
# * *
# *
for i in range(6):
    for j in range(6):
        if i==0 or j==0 or j==6-i-1:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()

print('-----------------------------------------')

#           *
#         * *
#       *   *
#     *     *
#   * * * * *
for i in range(1,6):
    for k in range(6-i):
        print(" ",end=" ")
    for j in range(1,i+1):
        if j==1 or j==i or i==5:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()

print('---------------------------------------')

# * * * * * *
#   *       *
#     *     *
#       *   *
#         * *
#           *
for i in range(6,0,-1):
    for k in range(6-i):
        print(" ",end=" ")
    for j in range(1,i+1):
        if j==1 or j==i or i==6:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()

print('-----------------------------------------')

#           *
#         *   *
#       *       *
#     *           *
#   * * * * * * * * *
for i in range(1,6):
    for k in range(6-i):
        print(" ",end=" ")
    for j in range(2*i-1):
        if j==0 or j==2*i-2 or i==5:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
    
print('---------------------------------------')

# * * * * * * * * * * *
#   *               *
#     *           *
#       *       *
#         *   *
#           *

for i in range(6,0,-1):
    for k in range(6-i):
        print(" ",end=" ")
    for j in range(2*i-1):
        if j==0 or j==2*i-2 or i==6:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()

print('------------------------------------------')

#           *
#         *   *
#       *       *
#     *           *
#   *               *
# *                   *
#   *               *
#     *           *
#       *       *
#         *   *
#           *
for i in range(1,6):
    for k in range(6-i):
        print(" ",end=" ")
    for j in range(2*i-1):
        if j==0 or j==2*i-2:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
for i in range(6,0,-1):
    for k in range(6-i):
        print(" ",end=" ")
    for j in range(2*i-1):
        if j==0 or j==2*i-2:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()

print("--------------------------------------------------")

# * * * * * * * * * * *
#   *               *
#     *           *
#       *       *
#         *   *
#           *
#         *   *
#       *       *
#     *           *
#   *               *
# * * * * * * * * * * *

for i in range(6,0,-1):
    for k in range(6-i):
        print(" ",end=" ")
    for j in range(2*i-1):
        if j==0 or j==2*i-2 or i==6:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
for i in range(2,7):
    for k in range(6-i):
        print(" ",end=" ")
    for j in range(2*i-1):
        if j==0 or j==2*i-2 or i==6:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()

print("----------------------------------------------")



