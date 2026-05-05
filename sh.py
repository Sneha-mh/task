#1
number = float(input('Enter a number: '))
if 1 <= number <= 100:
    print(f'{number} is between 1 and 100.')
elif number < 1 or number > 100:
    print(f'{number} is NOT between 1 and 100.')
else:
    print('Invalid input')

#2
number = int(input('enter '))
if number % 2 == 0:
    print(f'{number} is even')
else:
    print(f'{number} is odd')

#3
number = int(input('enter a number:'))
if number == 1:
    print(f'january')
elif number == 2:
    print(f'february')
elif number == 3:
    print(f'march')
elif number == 4:
    print(f'april')
elif number == 5:
    print(f'may')
elif number == 6:
    print(f'june')
elif number == 7:
    print(f'july')
elif number == 8:
    print(f'august')
elif number == 9:
    print(f'september')
elif number == 10:
    print(f'october')
elif number == 11:
    print(f'november')
elif number == 12:
    print(f'december')
else:
    print('invalid number')

#4
marks = int(input('enter your marks:'))
if marks > 80:
    print('grade A')
elif marks >= 60:
    print('grade b')
elif marks >= 50:
    print('grade c')
elif marks >= 45:
    print('grade d')
elif marks >=25:
    print('grade e')
else:
    print('grade f')

#5
age = int(input('Enter age: '))
if age >= 18:
    print('Adult')
else:
    print('Minor')
    
#6
num1 = float(input('Enter First Number: '))
num2 = float(input('Enter Second Number: '))
operator = input('Enter operator (+, -, *, /): ')

if operator == '+':
    result = num1 + num2
elif operator == '-':
    result = num1 - num2
elif operator == '*':
    result = num1 * num2
elif operator == '/':
    if num2 != 0:
        result = num1 / num2
    else:
        result = 'Error (Division by Zero)'
else:
    result = 'Invalid Operator'

print(f'Your Answer is : {result}')

#7
salary = float(input('Enter your salary: '))
credit_score = int(input('Enter your credit score: '))
if salary >= 50000 and credit_score >= 700:
    print('Eligible')
else:
    print('Not Eligible')
    
#8
n = int(input('Enter a number: '))

if n % 3 == 0 and n % 5 == 0:
    print('FizzBuzz')
elif n % 5 == 0:
    print('Buzz')
elif n % 3 == 0:
    print('Fizz')
else:
    print(n)
    
#9
ch = input('Enter a character: ').lower()

if ch in ('a', 'e', 'i', 'o', 'u'):
    print('Vowel')
else:
    print('Consonant')

#10
marks = int(input('Enter marks: '))

if 90 <= marks <= 100:
    print('Grade: A')
elif 80 <= marks <= 89:
    print('Grade: B')
elif 70 <= marks <= 79:
    print('Grade: C')
elif marks < 70:
    print('Fail')
else:
    print('Invalid marks')
    
#11
age = int(input('Enter age: '))

if age < 13:
    print('Child')
elif 13 <= age <= 19:
    print('Teenager')
elif age > 19:
    print('Adult')
    
#12
character = input('Enter a character: ')

if character.isupper():
    print('Uppercase')
elif character.islower():
    print('Lowercase')
elif character.isdigit():
    print('Digit')
else:
    print('Special character')
    
#13
color = input('Enter color (Red, Yellow, Green): ').lower()

if color == 'red':
    print('Stop')
elif color == 'yellow':
    print('Get Ready')
elif color == 'green':
    print('Go')
else:
    print('Invalid color')
    
#14
age = int(input('Enter age: '))
experience = int(input('Enter years of experience: '))

if age > 18 and experience >= 2:
    print('Eligible')
else:
    print('Not Eligible')
    
#15
temp = float(input('Enter temperature in °C: '))

if temp > 30:
    print('It\'s hot, stay hydrated!')
elif 15 <= temp <= 30:
    print('Enjoy the weather!')
elif temp < 15:
    print('It\'s cold, wear warm clothes!')
    
#16
menu = input('Enter menu item (Pizza, Burger, Pasta): ')
 
if menu == 'Pizza':
    print('Price: $10')
elif menu == 'Burger':
    print('Price: $7')
elif menu == 'Pasta':
    print('Price: $8')
else:
    print('Item not found')
    
#17
height = float(input('Enter height in feet: '))
 
if height >= 6:
    print('Selected')
else:
    print('Not Selected')
    
#18
age = int(input('Enter age: '))
 
if age >= 18:
    print('Allowed')
else:
    print('Not Allowed')
    
#19
username = input('Enter username: ')
password = input('Enter password: ')
 
if username == 'admin' and password == 'password123':
    print('Access Granted')
else:
    print('Access Denied')
    
#20
month = int(input('Enter month number (1-12): '))
 
if month in [12, 1, 2]:
    print('Winter')
elif month in [3, 4, 5]:
    print('Spring')
elif month in [6, 7, 8]:
    print('Summer')
elif month in [9, 10, 11]:
    print('Autumn')
else:
    print('Invalid month')