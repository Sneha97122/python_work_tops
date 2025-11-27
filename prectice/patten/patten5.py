
# 1
# 23
# 456
# 78910
# 1112131415

row=1
for i in range(1,6):
    for j in range(i):
        print(row,end=" ")
        row +=1
    print()