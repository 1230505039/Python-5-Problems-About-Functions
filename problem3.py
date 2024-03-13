"""
Kullanıcıdan 2 tane sayı alarak bu sayıların en küçük ortak katlarını (EKOK) dönen bir tane fonksiyon yazın.
"""

def lcm(number1, number2):
    product = number1 * number2

    for i in range(2, number2):
        if number1 % i == 0 and number2 % i == 0:
            number1 /= i
            number2 /= i
            product = product / i
        elif number1 % i == 0:
            number1 /= i
        else:
            number2 /= i
    return int(product)

number1 = int(input("Enter a number: "))
number2 = int(input("Enter another number: "))

print("Result: ", lcm(number1, number2))

