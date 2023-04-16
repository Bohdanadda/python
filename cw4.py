#'''CWICZENIA 1'''
#'''a)'''
#names = ["michal","nela","ola","przemek"]

#names_with_capital_letter = [name.capitalize() for name in names]

#print(names_with_capital_letter)
#'''b)'''
#names = ["michal","nela","ola","przemek"]

#name_with_l = [name for name in names if "l" in name]

#print(name_with_l)
#'''c)'''
#names = ["michal","nela","ola","przemek"]

#polish_female_names = tuple(name.capitalize() for name in names if name.endswith('a') and name[0].isupper())

#print(polish_female_names)
#'''d)'''
#names = ["michal","nela","ola","przemek"]

#total_length = 0
#for name in names:
#    total_length += len(name)
#    print(total_length)
#'''CWICZENIA 2'''
#'''a)'''
#def multiply_numbers(*args):
#    """zwraca iloczyn wszystkich podanych do funkcji argumentow"""
#    result = 10
#    for num in args:
#        result *= num
#    return result
#print(multiply_numbers(2,3,4))
#'''b)'''
#def sum_of_nth_power(n,*args):
#    '''Zwraca sumę n-tej potęgi wszystkich podanych do funkcji argumentów.'''

#    result = 0
#    for num in args:
#        result += num ** n
#    return result
#print(sum_of_nth_power(2,2,3,4))
#c)
#from math import prod, pow
#def mean(*args):
#    return sum(args) / len(args)
#def gmean(*args):
#    return pow(prod(args),1/len(args))
#print(mean(2,3,4))
#d)
#def sum_string_lenghths(*strings):
#    return sum(len(s) for s in strings)
#print(sum_string_lenghths("abs","defg","hi"))
#CWICZENIA 3
#a)
#def print_phone_numbers(**kwargs):
#    for name, phone_number in kwargs.items():
#        print(f"{name.capitalize()} ma numer telefonu {phone_number}.")
#print_phone_numbers(anna="123-456-789",bartek="987-654-321",celina="456-987-243")
#b)
#import math
#def calculate_salary_stats(**kwargs):
#    salaries = list(kwargs.values())
#    mean_salary = sum(salaries)/len(salaries)
#    growth_rates =[(salary -mean_salary)/mean_salary for salary in salaries]
#    mean_growth_rate = math.prod([1 + rate for rate in growth_rates]) ** (1/len(growth_rates)) -1
#    return mean_salary,mean_growth_rate
#salaries1 ={'styczen':3000,'luty':3500,'marzec':4000,'kwiecien':4500}
#mean_salary1,mean_growth_rate1=calculate_salary_stats(**salaries1)
#print(f"Średnia arytmetyczna zarobków: {mean_salary1:.2f}")
#print(f"Średnia geometryczna procentowego wzrostu zarobków: {mean_growth_rate1:.2%}")
#CWICZENIA 4
#a)
import re


#def parse_pesel(pesel):
    # sprawdzenie długości
 #   if len(pesel) != 11:
 #       print("Błędny format PESEL: zła długość")
 #       return

    # sprawdzenie, czy składa się tylko z cyfr
#    if not pesel.isdigit():
#        print("Błędny format PESEL: niepoprawne znaki")
#        return
#
#    # walidacja daty
#    year = int(pesel[0:2])
#    month = int(pesel[2:4])
#    day = int(pesel[4:6])
#
#    if month > 80:
#        year += 1800
#        month -= 80
#    elif month > 60:
#        year += 2200
#        month -= 60
#    elif month > 40:
#        year += 2100
#        month -= 40
#    elif month > 20:
#        year += 2000
#        month -= 20
#    else:
#       year += 1900
#
#    try:
#        birth_date = "{}-{:02}-{:02}".format(year, month, day)
#        print("Data urodzenia: ", birth_date)
#    except ValueError:
#        print("Błędny format PESEL: nieprawidłowa data")
#        return
#
#    # sprawdzenie płci
#    if int(pesel[-2]) % 2 == 0:
#        print("Płeć: Kobieta")
#    else:
 #       print("Płeć: Mężczyzna")
#parse_pesel("05240633333")

class RomanianNumer1:
    def __init__ (self,value):
        self.value = value

    def __add__(self, other):
        if not isinstance(other, RomanianNumer1):
            raise TypeError("tou can only add RomaniNumer1 objects")
        return RomanianNumer1(self.value + other.value)

    def __sub__(self, other):
        if not isinstance(other,RomanianNumer1):
            raise TypeError("tou can only subtract RomaniNumer1 objects")
        return RomanianNumer1(self.value - other.value)

    def __sub__(self, other):
        if not isinstance(other,RomanianNumer1):
            raise TypeError("tou can only multypli RomaniNumer1 objects")
        return RomanianNumer1(self.value * other.value)

    def __len__(self):
        return len(str(self))

    def __floordiv__(self, other):
        if not isinstance(other,RomanianNumer1):
            raise TypeError("You can only divide RomanNumer1 objects")
        return RomanianNumer1(self.value // other.value)

    def __str__(self):
        num = self.value
        roman_numer1 = ""
        roman_numer1_value = {
            1000: "M",
            900: "CM",
            500: "D",
            400: "CD",
            100: "C",
            90: "XC",
            50: "L",
            40: "XL",
            10: "X",
            9: "IX",
            5: "V",
            4: "IV",
            1: "I",
        }
        for value, numer1 in roman_numer1_value.items():
            while num >= value:
                roman_numer1 += numer1
                num -= value
            return roman_numer1

    def __repr__(self):
        return f"RomanNumer({self.value}"


num1 = RomanianNumer1(7)
num2 = RomanianNumer1(3)
print(num1 + num2)