"""
1'den 1000'e kadar olan sayılardan mükemmel sayı olanları ekrana yazdırın.
Bunun için bir sayının mükemmel olup olmadığını dönen bir tane fonksiyon yazın.
Bir sayının bölenlerinin toplamı kendine eşitse bu sayı mükemmel bir sayıdır.
Örnek olarak 6 mükemmel bir sayıdır (1 + 2 + 3 = 6).
"""

def perfectnumbers(number):
    summary = 0
    for j in range(1, number):
        if number % j == 0:
            summary = summary + j
    if number == summary:
        print("{} number is perfect number.".format(number))

for i in range(1, 1000):
    perfectnumbers(i)

