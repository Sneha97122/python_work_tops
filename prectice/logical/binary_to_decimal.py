number = 101101 
decimal =0
power =0

while number != 0:
    digit = number % 10          
    decimal += digit * (2 ** power)
    number = number // 10           
    power += 1

print("Decimal number is:", decimal)

