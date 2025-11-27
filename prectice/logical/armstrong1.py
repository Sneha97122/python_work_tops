
# for num in range(100,1000):
#     temp = num
#     sum = 0

#     while num > 0:
#         rem = num % 10
#         sum += rem*rem*rem
#         num = num // 10

#     if temp==sum:
#       print(temp)

for num in range(100,1000):
    temp = num
    s = 0
    n = num   # copy number for while loop

    while n > 0:
        rem = n % 10
        s += rem*rem*rem
        n = n // 10

    if temp == s:
        print(temp)




