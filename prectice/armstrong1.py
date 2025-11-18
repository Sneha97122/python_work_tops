for num in range(100,104):
    temp = num
    sum = 0

    while num > 0:
        rem = num % 10
        sum += rem*rem*rem
        num = num // 10

    if temp==sum:
      print(temp)




