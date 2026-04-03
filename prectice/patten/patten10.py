for i in range(1,6):
    for k in range(6-i):
        print(" ",end=" ")
    for j in range(i*2-1):
        if j==0 or j==2*i-2:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print(" ")
for i in range(6,0,-1):
    for k in range(6-i):
        print(" ",end=" ")
    for j in range(i*2-1):
        if j==0 or j==2*i-2:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print(" ")



