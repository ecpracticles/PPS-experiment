binary = input("Enter a Binary Number: ") 

decimal = 0
power = 0

for digit in binary[::-1]:
    decimal += int(digit) * (2 ** power)
    power += 1

print("Decimal Number:", decimal)
