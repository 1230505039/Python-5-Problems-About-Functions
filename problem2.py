"""
Kullanıcıdan 2 tane sayı alarak bu sayıların en büyük ortak bölenini (EBOB) dönen bir tane fonksiyon yazın.
"""

def gcd(number1, number2):
    if number1 == 0:
        return number2
    elif number2 == 0:
        return number1
    else:
        return gcd(number2, number1 % number2)

number1 = int(input("Enter a number: "))
number2 = int(input("Enter another number: "))

if number1 > number2:
    print("Result: ", gcd(number1, number2))
else:
    print("Result: ", gcd(number2, number1))




