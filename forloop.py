#1
for num in range (1,6):
    
    if num %2 ==0:
        print(f'Number {num} is even')
    else:
        print(f'Number {num} is odd')
    
#2
num = [ 10,20, 30, 40]
sum=0
for value in num:
    sum += value
    print(f"Added {value}. Running total is {sum}.")

print("------------------------------")
print(f"Total Sum: {sum}")

#3
student_names = ['Ram', 'Hari', 'Sita']

print('--- Email Greetings Generated ---')

for name in student_names:
    print(f'Hi {name}, your course approval is ready!')
    
#4
chapter_pages = [45, 30, 50, 40]

print('--- Book Chapter Summary ---')

for chapter_number, pages in enumerate(chapter_pages, start=1):
    print(f'Chapter {chapter_number} has {pages} pages.')
    
#5
number = [4,5,3,2]
for i in number:
    for j in range(1,11):
        print(f'{i} * {j} = {i*j}')
        print()
        
#6
number = [11]
for i in number:
    for j in range(1,11):
        print(f'{i} * {j} = {i*j}')
        print()
        
#7
lst = [3, 2, 1, 4, 5]

reversed_list = []

for i in range(len(lst) - 1, -1, -1):
    reversed_list.append(lst[i])

print(reversed_list)

#8
list1 = [1, 2, 3, 4, 5]
list2 = [3, 4, 5, 6, 7]

print('Common elements:')

for num in list1:
    if num in list2:
        print(num)

#9
lst = [1, 2, 3, 4]

for num in lst:
    if num == 1 or num == 4:
        print(num)
        
#10
text = 'Hello World'

result = ''

for char in text:
    if char.lower() not in 'aeiou':
        result += char

print(result)

#11
sentence = 'Loops are Fun'

vowels = 0
consonants = 0

for char in sentence.lower():
    if char.isalpha():
        if char in 'aeiou':
            vowels += 1
        else:
            consonants += 1

print('vowels:', vowels)
print('consonants:', consonants)

#12
numbers = [1, 2, 3, 4, 5]

odd = []
even = []

for num in numbers:
    if num % 2 == 0:
        even.append(num)
    else:
        odd.append(num)

print('Odd numbers:', odd)
print('Even numbers:', even)

#13
number = 17

is_prime = True

if number <= 1:
    is_prime = False
else:
    for i in range(2, number):
        if number % i == 0:
            is_prime = False
            break

if is_prime:
    print('Prime number')
else:
    print('Not a prime number')
    
#14
lst = [1, 2, 3, 4, 'a', 'b']

numbers = []
strings = []

for item in lst:
    if type(item) == int:
        numbers.append(item)
    elif type(item) == str:
        strings.append(item)

print('Numbers:', numbers)
print('Strings:', strings)

#15
text = 'Python123'

letters = 0
digits = 0

for char in text:
    if char.isalpha():
        letters += 1
    elif char.isdigit():
        digits += 1

print('Letters:', letters)
print('Digits:', digits)

#16
username = input('Enter username: ')
password = input('Enter password: ')

if username == 'admin' and password == '1234':
    print('Login successful')
else:
    print('Invalid username or password')
    
#17
number = int(input('Enter a number: '))

if number % 2 == 0:
    print('Even')
else:
    print('Odd')
    
#18
number = int(input('Enter a number: '))

factorial = 1

for i in range(1, number + 1):
    factorial *= i

print('Factorial =', factorial)

#19
number = [1,2,3,4,5,6,7,8 ]
for i in number:
    for j in range (1,11): 
        print(f'{i} * {j} = {i*j}')
        print()
        
#20
lst = [1, 2, 3, 4]
for num in lst:
    if num == 1 or num == 4:
        print(num)
        
#21
start = 1
end = 10

total = 0

for num in range(start, end + 1):
    if num % 2 != 0:
        total += num

print('Sum of odd numbers:', total)

#22
start = 1
end = 10

total = 0

for num in range(start, end + 1):
    if num % 2 == 0:
        total += num

print('Sum of even numbers:', total)

#23
text = 'Python is easy to learn'

spaces = 0

for char in text:
    if char == ' ':
        spaces += 1

print('Spaces:', spaces)

#24
lst = [1, 2, 3, 4]

result = []

for num in lst:
    result.append(num ** 3)

print(result)

#25
a = 'programming'

reverse = ''

for char in a:
    reverse = char + reverse

print(reverse)

#26
for i in range(50):
    if i > 7:
        break
    print(i)
    
#27
text = 'Python'

for char in text:
    print(char)
    
#28
a = ['ram', 'shyam', 1, 2]

for item in a:
    if type(item) == str:
        print('Hello!' + item)
        
#29
a = ['ram', 'shyam', 1, 2]

result = []

for item in a:
    result.append('Dr.' + str(item))

print(result)

#30
lst = [1, 2, 3, 4, 5]

new_list = []

for num in lst:
    new_list.append(num ** 2)

print(new_list)

#31
lst1 = [111, 32, -9, -45, -17, 9, 85, -10]

positive_numbers = []

for num in lst1:
    if num > 0:
        positive_numbers.append(num)

print(positive_numbers)

#32
lst = [0, 1, 2, 3, 4, 5, 6]

for num in lst:
    if num == 3 or num == 6:
        continue
    print(num)
    
#33
lst1 = [1, 'Python', 3.5, True]

lst2 = []

for item in lst1:
    lst2.append(type(item))

print(lst2)

#34
for i in range(5):
    print(i)
else:
    print('Done')
    
#35
for num in range(105, 0, -7):
    print(num, end=' ')
    
#36
bad_chars = [';', ':', '!', '*']
text = 'py;th* o:n ! ;py * t*h:o !n'

result = ''

for char in text:
    if char not in bad_chars and char != ' ':
        result += char

print(result)

#37
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

even_count = 0
odd_count = 0

for num in numbers:
    if num % 2 == 0:
        even_count += 1
    else:
        odd_count += 1

print('Even numbers:', even_count)
print('Odd numbers:', odd_count)

#38
total = 0

for num in range(3, 100):
    if num % 3 == 0 or num % 5 == 0:
        total += num

print('Sum:', total)

#39
even_sum = 0
odd_sum = 0

for num in range(1, 101):
    if num % 2 == 0:
        even_sum += num
    else:
        odd_sum += num

print('Even sum:', even_sum)
print('Odd sum:', odd_sum)

#40
list1 = [10, 20, 10, 30, 10, 40, 50]
target = 10

count = 0

for num in list1:
    if num == target:
        count += 1

print('Occurrences:', count)    
