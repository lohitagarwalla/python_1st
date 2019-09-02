# print(10 / 3) #gives a floating point value
# print(10 // 3) #gives a integer value
# print(10 ** 3) #gives 10 to the power of 3
# print(10 % 3) #gives the remainder
# print(round(3.5))
#
# import math`
# print(math.factorial(4))
# print(math.ceil(3.6))
# print(math.floor(3.6))
#
# #if elif else
# x = 400
# y = 300
# z = 500
#
# if x > y:
#     if x > z:
#         print("x is the greatest integer")
#     else:
#         print("z is the greatest integer")
# else:
#     if y>z:
#         print("y is the greatest")
#     else:
#         print('z is the greatest')


# using and not or
# *****************
# is_the_student_intelligent = False
# # is_the_student_hardworking = False
# if is_the_student_hardworking and is_the_student_intelligent:
#     print('The student can crack IIT JEE ADVANCED')
# elif is_the_student_intelligent and not is_the_student_hardworking:
#     print('he can crack JEE MAINS')
# else:
#     print('he should choose some other career path')

# to convert meters to feet and vice versa
# ****************************************************
# unit = input('"m" for meters and "f" for feet: ')
# length_measured = input('Enter the length measured: ')
# if unit == 'm':
#     suta = ((int(length_measured) * 100) / 2.546 - (int(length_measured) * 100) // 2.546) * 8
#     inches = (int(length_measured) * 100) // 2.546
#     feet = ((int(length_measured) * 100) // 2.546) // 12
#     print(feet,"' ", inches - feet * 12,"'' ", round(suta),"''' ")
# else:
#     meters = int(length_measured) * 12 * 2.546 / 100
#     print(meters)


# while loop and printing a pattern
# *******************
# iterator = 1
# while iterator<6:
#     print('* ' * iterator)
#     iterator += 1


# making a number guessing game
# *****************************
# rules of the game: you get to guess a secret number 3 times, if you get correct number you win else you loose
# secret_number = 5
# count_number = 1
# count_limit = 3
# entered_number = -1
# while count_number <= count_limit:
#     entered_number = int(input ('guess the number: '))
#     if entered_number == secret_number:
#         print('you win')
#         break
#     count_number += 1
# else:
#     print('you loose')

# for loops
# ***********
# for letters in 'lohit':
#     print(letters)
#
# for names in ['lohit', 'nidhi', 'aman', 'suresh', 'saroj']: #this is list
#     print(names)
#
# for i in range(4):
#     print(i)
#
# for i in range(4, 7):
#     print(i)
#
# for i in range(1,10,2):
#     print(i)

# lists in detail
# ******************
# numbers = [1,5,9,6]
# numbers.append(15)
# print(numbers) #inserts 15 at the end of the list
#
# numbers.insert(0,2)
# print(numbers) #inserts 2 at the  index 0
#
# numbers.remove(9) #removes the element 9
# print(numbers)
#
# #numbers.clear() #clears all the elements in the list
# print(numbers)
#
# numbers.pop()
# print(numbers)

# writing a program to remove the duplicates in a list
# numbers = [1,5,1,4,2,3,4,9,4,10,5]
# # numbers.sort()
# for i in numbers:
#     if numbers.count(i) > 1:
#         numbers.remove(i)
# print(numbers)
# # second method
# num = [1,5,1,4,2,3,4,9,4,10,5]
# uniques = []
# for n in num:
#     if n not in uniques:
#         uniques.append(n)
# print(uniques)

# program to store prime numbers in a list
# count = [2]
# for i in range(2,300):
#     for j in range(2,i):
#         if i%j == 0:
#             break
#         if i == j+1:
#             count.append(i)
# print(count)

# TUPPLES: It is similar to list except nothing can be added or deleted
# ***********************************************************************
# a_tuple = (1,2,3,2)
# x = a_tuple.count(2)
# print(x)
#
# #UNPACKING
# **************
# co_ordinates = [1, 2, 8, 5]
# a,b,c,d = co_ordinates
# print(a,b,c,d)
# unpacking can be used with both tuples and lists

# DICTIONARIES
# *************
# it consists of key and values
# address = {
#     "house_no": 9,
#     "street_name": "byelane 1",
#     "is_it_home_address": True,
#     "state": "Assam"
# }
# print(address["street_name"])
# print(address.get("state","assam")) #get is used so that if we put a key that does not exist (for example "state" then it will not throw an error.Instead it will show none. and the second value is the value if it doesn't exist.
# address["street_name"] = 'south_sarania'
# print(address["street_name"])
#
# phone_number = input('Phone number: ')
# numtowords = {
#     "1": "one",
#     "2": "two",
#     "3": "three",
#     "4": "four",
#     "5": "five",
#     "6": "six",
#     "7": "seven",
#     "8": "eight",
#     "9": "nine",
#     "0": "zero",
# }
# for i in phone_number:
#     print(numtowords[i])
# another applicaton of dictionary to convert emogi messages to real emogis
# message = input('> ')
# words = message.split(' ')
# emogi = {
#     ":)": "🙂", #to use emogis press windows and ;
#     ":(": "☹"
# }
# message = ""
# for word in words:
#     message += emogi.get(word, word) + " "
# print(message)

# FUNCTIONS
# ***********
# def summation(a, b):
#     print(f"the sum is {a + b}")
#
#
# summation(3, 10)  # here a and b are parameters and 3 and 4 are arguments

# #using keyword arguments:
# def divide(numerator, denominator):
#     print(numerator/denomminator)
# divide(10,2) #this is positional argument
# divide(denomminator=2, numerator=10) #this is keyword arguments
# divide(30,denomminator=5)

#TRY AND EXCEPT
# try:
#     num = int(input("date of birth: "))
#     print(f'your age is {2019 - num}')
# except ValueError:
#     print('entered value should be a number')
# we can add multiple except for handling different types of error

#CLASSES
# #*******************************
# class Name:
#     def __init__(self,x,y): #this is constructor
#         self.x = x
#         self.y = y
#
#     def first_name(self):     #this is a method
#         print("Lohit")
#
#     def last_name(self):      #this is a also a method
#         print("Agarwalla")
#
#
# my_name = Name(10, 20)
# print(my_name.x)
# my_name.x = 30
# print(my_name.x)

# *ANOTHER EXAMPLE OF CLASS
# class Person:
#     def __init__(self, name):
#         self.name = name
#
#     def talk(self):
#         print(f'hi i am {self.name}')
#
#
# lohit = Person("Lohit Agarwalla")
# lohit.talk()
# nidhi = Person("Nidhi Agarwalla")
# nidhi.talk()


#INHERITANCE
# class Mammal:
#     def walk(self):
#         print("walk")


# class Dog(Mammal):  #   here dog class inherits the methods of mammal class
#     def jump(self):
#         print('jump')
#
#
# class Cat(Mammal):
#     pass #  when we have nothing extra other than inherited methods then we use pass
#
#
# dog1 = Dog()
# dog1.walk()
# dog1.jump()
#
# cal1 = Cat()
# cal1.walk()


#Modules
# **********************************
#  to create a modul, create a file with classes and functions and then import that file
# import converters
# print(converters.joules_to_calorie(8.4))
# from converters import joules_to_calorie
# y = joules_to_calorie(60)
# print(y)


#PACKAGES: These are folders that contains many modules.
import ecommersce.shipping
ecommersce.shipping.calculate_shipping_cost()

from ecommersce.shipping import calculate_shipping_cost
calculate_shipping_cost()

import math
print(math.sqrt(25))

