# input() = A function that PROMPTS the user to enter data
#           Returns the entered data as a STRING
#
# name = input('What is your name?:')
# print(f'hello, {name}!')
#
# topic = input('Did you have a girlfriend?')
# print(f'{topic}. I am off the market.')
#
# Which means, when we use input, we store the input as a string
# Can only concatenate str to str. not int to str.
# so use typecasting.
#
# Exercise 1 Rectangle Area Cal
# width = float(input('the width: '))
# length = float(input('the length:  '))
# area = length * width
# print(f'The rectangle is {area}cm\u00B2.')
#
# Exercise 2 Shopping Cart Program
# item = input('What did you buy in Costco? ')
# quantity = int(input('I have bought '))
# price = float(input('Each of them is $'))
# total = quantity * price
# print(f'So all of them costs me ${total}. ')
#
# Madlibs Game 1
# A word game that creates a story
# By filling the blanks with random words
# Creative!
# noun1 = input('Enter the word 1 (person, place, thing):')
# noun2 = input('Enter the word 2 (person, place, thing):')
# adjective1 = input('Enter the adjective word 1:')
# adjective2 = input('Enter the adjective word 2:')
# verb1 = input('Enter the word (do, to do):')
# print(f'I have read an {noun1}.')
# print(f'It is {adjective1}.')
# print(f'I believe that I will {verb1} {noun2}.')
# print(f'Because I am {adjective2}')
# print(f'Madlibs Game 1 ends.')
#
# Madlibs Game 2
# verb1 = input('Enter a verb1 ending with -ing.:')
# verb2 = input('Enter a verb2 ending with -ing.:')
# verb3 = input('Enter a verb3 ending with -ing.:')
# noun1 = input('Enter a noun1 (person, place, thing).:')
# noun2 = input('Enter a noun2 (person, place, thing).:')
# noun3 = input('Enter a noun3 (person, place, thing).:')
# noun4 = input('Enter a noun4 (person, place, thing).:')
# noun5 = input('Enter a noun5 (person, place, thing).:')
# noun6 = input('Enter a noun6 (person, place, thing).:')
# adjective1 = input('Enter a adjective1 (description).:')
# print(f'I was {verb1} and {verb2} a {noun1}.')
# print(f'It is about {noun2}')
# print(f'I invest in {noun3}, {noun4} and {noun5}.')
# print(f'I am {verb3} great and become a {adjective1} {noun6}.')
# print(f'I have a mansion and I collect cars and motorcycles.')
# print(f'Madlibs Game 2 Ends.')
#
#
# Exercise of the circumference of a circle. Math Functions
# C = 2 pi r
# import math
# radius = float(input('Enter the radius of a circle. :'))
# circumference = 2 * math.pi * radius
# print(f'The circumference is {round(circumference, 3)}cm.')
#
# Exercise of the area of a circle
# import math
# radius = float(input('Enter the radius of a circle: '))
# area = math.pi * pow(radius, 2)
# print(f'The area of a circle is {round(area, 3)}cm\u00b2')
#
# Exercise of hypotenuse of a right triangle.
# hypotenuse of a right triangle is c = sqrt of a^2 + b^2
# import math
# a = float(input('Enter side A is: '))
# b = float(input('Enter side B is: '))
# c = math.sqrt(pow(a,2)+pow(b,2))
# print(f'Side C is {round(c, 3)}cm.')
#
#
# Exercise of if statements
#
# age = int(input('Enter your age: '))
# if 0 < age < 18:
#         print('You are in a teenager group!')
# elif 18 <= age < 60:
#         print('You are in a adult group!')
# elif 60<= age < 90:
#         print('You are in a retirement group!')
# else:
#         print('Sorry. Your are not selected.')
#
# answer = input('Would you like some pizza? Enter (Y/N):')
# if answer == 'Y':
#         print('Here it is. Enjoy!')
# else:
#         print('No problem.')
#
# need_sponsor = False
# if need_sponsor:
#     print('Okay. What type of sponsorship do you need?')
# else:
#     print('When would you come to work?')
#
# date = str(input('Enter the date: '))
# if date == '':
#     print('Sorry. Please enter the date.')
# else:
#     print(f'Great! You will do onboard on {date}.')
#
# # Exercise 1 of python calculator (Simple Version)
# operator = input('Enter the operator (+ - * /): ')
# num1 = float(input('Enter the 1st num: '))
# num2 = float(input('Enter the 2nd num: '))
# if operator == '+':
#     result = num1 + num2
#     print(result)
# elif operator == '-':
#     result = num1 - num2
#     print(result)
# elif operator == '*':
#     result = num1 * num2
#     print(result)
# elif operator == '/':
#     result = num1 / num2
#     print(round(result, 3))
# else:
#     print(f'Sorry. {operator} is not recognized. Please follow the sign.')
#
# # Exercise 2 of python calculator (Simple Version)
# # python weight converter
# weight = float(input('Enter the weight: '))
# unit = input('Enter kilograms or pounds. K/L? ')
# if unit == 'K':
#     weight = weight * 2.205
#     unit = 'Lbs'
#     print(f'The weight is {weight} {unit}.')
# elif unit == 'L':
#     weight = weight / 2.205
#     unit = 'Kgs'
#     print(f'The weight is {round(weight, 2)} {unit}.')
# else:
#     print(f'Incorrect. Please try again later.')
#
# # Exercise 3 of python calculator (Simple Version)
# # python temperature converter
# temperature = float(input('Enter the temperature. '))
# unit = input('Is it Celsius or Fahrenheit? (C or F?) ')
# if unit == 'C':
#     temperature = round((temperature * 9/5) + 32, 2)
#     unit = 'degrees Fahrenheit'
#     print(f'The temperature is {round(temperature, 2)} {unit}.')
# elif unit == 'F':
#     temperature = round(((temperature - 32)*5/9), 2)
#     unit = 'degrees Celsius'
#     print(f'The temperature is {round(temperature, 2)} {unit}.')
#
#
# # Exercise of logical operators = evaluate multiple conditions( or, and, not)
# #                or = at least one condition must be true
# #               and = both conditions are true or both false
# #               not = inverts the conditions (not false, not true)
# response = ''
# time = (2025, 11, 22)
# no_meeting = False
# if response == 'Okay' and time < (2025, 11, 22) or no_meeting:
#     print('The plan works as scheduled.')
# elif response == '' and time > (2025, 11, 21):
#     print('The plan is canceled.')
#
# # Exercise of conditional expression = A one-line shortcut for if-else statement (ternary operator)
# #                          Print or Assign one of two values based on one condition
# #                Formula = X if condition else Y
# # Attention: Python does NOT allow if and else inside print() with commas.
# # A conditional expression must be one continuous expression: It cannot be split by commas.
#
# response_datetime = (2025, 11, 21)
# print('Let us go' if response_datetime  < (2025, 11, 21)  else'Canceled.')
# age = 21
# print('You can go to the bar' if age >= 21 else'You are not allowed to drink in the bar.')
# a = 99
# b = 101
# print(a if a>b else b)
# max(a, b)
# print(b if max(a, b) else b)
# num = 6
# result = 'EVEN' if num %2 == 0 else 'ODD'
# print(result)
# max_num = a if a > b else b
# print(max_num)
# Text = 'Empty'
# result = 'Not going' if Text == 'Empty' else 'Going'
# print(result)
#
# # Exercise of string method
# # e.g. username
# # e.g. phone_number
#
# name = input('Enter your name: ')
# result = len(name)
# # len of string includes 标点符号, numbers and spaces
# print(result)
#
# result = name.find('G')
# print(result)
#
# result = name.rfind('E')
# print(result)
#
# name = name.capitalize()
# print(name)
#
# name = name.upper()
# print(name)
#
# name = name.lower()
# print(name)
#
# result = name.isdigit()
# print(result)
#
# result = name.isalpha()
# print(result)
#
# phone_number = input('Enter the phone number: ')
# result = phone_number.count('-')
# print(result)
#
# result = phone_number.replace('-', '')
# print(result)
#
# # Exercise of string methods
# # validate user input exercise
# # 1. username is no more than 12 characters
# # 2. username must not contain spaces
# # 3. username must not contain digits
#
# username = input('Please enter the username: ')
# if len(username) > 12:
#     print(f'The username should be no more than 12 characters.')
# elif not username.find(' ') == -1:
#     print(f'The username must not contain spaces. Try again.')
# elif not username.isalpha():
#     print(f'The username must not contain digits. Try again.')
# else:
#     print(f'Congratulations, {username}!')
#
# # Exercise of Indexing = access the elements of a sequence using [] (index operator)
# #                        [start: end: step]
# # There is up to three fields we can fill in: a start, an end, and a step.
# # Negative index [-1], [::-1]
# credit_number = '7294-3767-3917-888'
# print(credit_number[0])
# print(credit_number[: 5])
# print(credit_number[5 : 9])
# print(credit_number[5 : ])
# print(credit_number[-3])
# print(credit_number[::3])
# print(credit_number[14: 18])
# print(credit_number[-4: ])
# # We want the last 3 digits. So!
# last_3_digits = credit_number[-3: ]
# print(f'Here you go, this is {last_3_digits}.')
# # Reverse the string
# backwards = credit_number[:: -1]
# print(f'The new credit number is {backwards}.')
#
# # Exercise of While loop = execute some code WHILE some condition remains true
# # Python expects all indented lines under the while loop to belong to the loop.
# price = float(input('Give me the lowest price offer. '))
# while price >=699.99:
#     print('Deal failed.')
# # Reprompt the user input the answer again. 👇
#     price = float(input('Give me the lowest price offer. '))
# print(f'Cool. Deal {price}.')
#
# TEST = input('Tell me you love me. Just copy: Yes, I love you, Alicia. ')
# while TEST != 'Yes, I love you, Alicia.':
#     print('You DEAD.')
#     TEST = input('Tell me you love me. Just copy:Yes, I love you, Alicia. ')
#
# print('Well done!')
#
# # Introduce logical operator for example: NOT, OR
# num = int(input('Enter a number between 1 - 10 '))
# while num < 1 or num > 10 :
#     print('Retype pls!')
#     num = int(input('Enter a number between 1 - 10 '))
#
# print(f'{num} is passed.')
#
# # Exercise in Python compound interest calculator
# principle = float(input('Enter the money you invest initially, at least great than 0. '))
# rate = float(input('The rate of the bank, at least great than 0. '))
# time = int(input('Years, great than 0 and input integer. '))
# total = principle * pow((1 + rate / 100), time)
#
# while principle <= 0:
#     print('Invalid.')
#     principle = float(input('Enter the money you invest initially, at least great than 0. '))
#
# while rate <= 0:
#     print('Invalid.')
#     rate = float(input('The rate of the bank, at least great than 0. '))
#
# while time <= 0:
#     print('Invalid.')
#     time = int(input('Years, great than 0 and input integer. '))
#
# print(f'Mrs. Solis. Your account balance in our bank after {time} year/s is ${total:.2f}.')
#
# # for loops = execute a block of code
# #             iterate over a string, range, sequence, etc.
# # if you want to count backwards, you can enclose the range function within reversed function.
# # There is additional parameter you could add, that is the STEP. you learned in Indexing.
# # in for loops, you use CONTINUE key word to skip over an iteration.
# # in for loops, you use BREAK key word to break out of the loop
# for x in reversed(range(1, 4)):
#     print(x)
# for x in range(3, 0, -1):
#     print(x)
# print('Marry Christmas!')
# for total_usd in range(-10, 11):
#     if total_usd == 0:
#         continue
#     else:
#         print(total_usd)
#
#
# # import time module, use sleep function within time module to sleep for a given amount of time.
# import time
# time.sleep(3)
# print('It is time to get up.')
#
# # import time module, use sleep function within time module to sleep for a given amount of time.
# # Notes: why second = x % 60, because x // 60 = full minutes. x % 60 = remainder of seconds after removing the removing full minutes.
# # suppose x = 125 seconds  example: (minutes) = 125 // 60   # 2   seconds = 125 % 60    # 5
# # // is integer division / is float division
#
# import time
# timer_set = int(input('Enter the time in seconds: '))
# for x in range(timer_set, -1, -1):
#     second = x % 60
#     minutes = (x % 3600) // 60
#     hour = x // 3600
#     print(f'{hour:02}:{minutes:02}:{second:02}')
#     time.sleep(1)
#
# print(f'Pass!')
#
# # Exercise of
# # nested loop = a loop within another loop.
# #               outer loop:
# #                   inner loop:
#
# rows = int(input('Enter the # of the rows: '))
# columns = int(input('Enter the # of the columns: '))
# symbol = input('Enter the 💛 as the symbol. ')
# for x in range(rows):
#     for y in range(columns):
#      print(symbol, end='')
#     print()
#
#
# # Exercise of
# # Collections = a single "variable" used to store multiple values
# # List = [] ordered, changeable. Duplicates okay
# # Set = {} unordered, immutable. Add/Remove okay. No duplicates
# # Tuple = () ordered, unchangeable. Duplicates okay. Faster
#
# fruits = ['apple', 'orange', 'pear', 'banana', 'coconut']
# print(dir(fruits))
# print(help(fruits))
# print(fruits.count('orange'))
# print(fruits.copy())
#
#
# # Exercise of Shopping cart program
# # In Collections
#
# foods = []
# prices = []
# quantities = []
# total = 0
# while True:
#     food = input('Enter the food to buy(Q to quit.): ')
#     if food.lower() == 'q':
#         break
#     else:
#         price = float(input(f'the price of {food}: $'))
#         quantity = int(input(f'the amounts of {food}: '))
#         foods.append(food)
#         prices.append(price)
#         quantities.append(quantity)
# print('----Your Shopping Bill----')
# for i in range(len(foods)):
#     item_total = prices[i] * quantities[i]
#     total += item_total
#     print(f"{foods[i]}  x{quantities[i]}  @ ${prices[i]} = ${item_total}")
# print()
# print(f'You finally spend ${total:02}.')
#
# # Exercise of
# # 2Dlist
# num_pad = ((1, 2, 3),
#            (4, 5, 6),
#            (7, 8, 9),
#            ('*', 0,'#'))
# for row in num_pad:
#     for num in row:
#         print(num, end='   ')
#     print()
#
#
# # Exercise of
# # Dictionaries
# capitals = {'China': 'Beijing', 'USA': 'DC'}
# # print(capitals.get('China'))
# # capitals.update({'UK':'London'})
# # print(capitals)
# # capitals.pop('USA')
# # capitals.popitem()
# # capitals.clear()
# # keys = capitals.keys()
# # print(keys)
# # Return to an object, which resembles a list ------ OBJECT ORIENTED programming. I will learn.
# # for key in capitals.keys():
# #    print(key)
#
# # values = capitals.values()
# # print(values)
# # for value in capitals.values():
# #    print(value)
#
# # items = capitals.items()
# # print(items)
# # for key, value in capitals.items():
# #       print(f'{key}:{value}')
#
# # Exercise of concession stand program
# # In Dictionaries
#
# menu = {'plum': 2.00,
#         'peach': 3.78,
#         'popcorn': 6.90,
#         'butter': 1.99,
#         'beer': 3.50}
# cart = []
# total = 0
# print('♥♥♥♥♥♥Welcome to Cams Shop♥♥♥♥♥♥')
# for key, value in menu.items():
#     print(f'{key:10}: ${value:.2f}.')
# print('🍿🍿🍿Show what you get here!🍿🍿🍿')
# while True:
#     food = input('Select the item(q to quit): ')
#     if food.lower() == 'q':
#         break
#     elif menu.get(food) is not None:
#         cart.append(food)
#
# for food in cart:
#     total = total + menu.get(food)
#     print(food, end=' ')
# print()
# print(f'Total is ${total:.2f}')
#
#
# print('🙂🙂🙂Thank you for choosing us.🙂🙂🙂')
#

# Exercise of
# import random
import random
lowest_num = 1
highest_num = 100
answer = random.randint(lowest_num, highest_num)
guesses = 0
is_running = True

print('Let us do a number guessing game.')
print(f'Select a number in {lowest_num} and {highest_num}')
while True:

    guess = input('Enter your guess: ')
    if guess.isdigit():
        guess = int(guess)
        guesses += 1

        if guess < lowest_num or guess > highest_num:
            print('Out of range!')
        elif guess < answer:
            print('Too low, try again.')
        elif guess > answer:
            print('Too high, try again')
        else:
            print('Correct.')
            print(f'You made {guesses} guesses in total.')
            break


    else:
        print('Invalid.')
