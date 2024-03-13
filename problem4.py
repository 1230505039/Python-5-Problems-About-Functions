"""
Kullanıcıdan 2 basamaklı bir sayı alın ve bu sayının okunuşunu bulan bir fonksiyon yazın.
"""
first_digit_list = ["on", "yirmi", "otuz", "kırk", "elli", "altmış", "yetmiş", "seksen", "doksan"]
second_digit_list = [" ", "bir", "iki", "üç", "dört", "beş", "altı", "yedi", "sekiz", "dokuz"]

def string_number(number):
    second_digit = number % 10
    first_digit = int(number / 10)
    return first_digit_list[first_digit - 1] + " " + second_digit_list[second_digit]



number = int(input("Enter a two digit number: "))

print(string_number(number))
