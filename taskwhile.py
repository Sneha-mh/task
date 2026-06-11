#1
while True:       
 age = int(input('enter your age '))
 if age < 18:
    print('you are a minor')
 elif age >= 18 and age<60:
    print('you are an adult')
 elif age >=60:
    print('you are a senior citizen')    
 user_input = input('do you want to continue?').lower()
 if user_input == 'no':
     break
 
 #2
while True:
    vehicle = input('enter name of vehicle: ')
    if vehicle != 'bus':
        print('waiting')
    else:
        print('wait is over')   
        break 
    
#3
ratings = [ '4+', '9+', '12+', '17+', '12+', '4+', '17+'] 
content_ratings = {}
i = 0

while i < len(ratings):
    rating = ratings[i]
    if rating in content_ratings:
        content_ratings[rating] += 1
    else:
        content_ratings[rating] = 1
    i += 1

print(content_ratings)


    
#4
import random
number = random.randint(1,10)
attempts = 0
print('guess a number between 1 to 10 ')
while True:
    guess = input('enter your guess: ')
    if not guess.isdigit():
        print("Please enter a valid number.")
        continue
    
    guess = int(guess)
    attempts += 1
    
    if guess < number:
        print("Guess higher ")
    elif guess > number:
        print("Guess lower ")
    else:
         print(f" Correct! The number was {number}.")
         print(f"It took you {attempts} attempts.")
         break
     
#5
correct_username = "admin"
correct_password = "1234"
attempts = 0
max_attempts = 3
while attempts < max_attempts:
    username = input("Enter username: ")
    password = input("Enter password: ")
    if username == correct_username and password == correct_password:
        print("Login successful")
        break
    else:
        attempts += 1
        if attempts < max_attempts:
            print("Invalid credentials, try again.")
        else:
            print("too many failed attempts")
            
#6
import random

while True:
    num1 = random.randint(1, 30)
    num2 = random.randint(1, 30)
    print('type exit to end quiz')

    print(f"what is {num1} * {num2}?")
    answer = input("Enter your answer : ")

    if answer.lower() == "exit":
        print("Quiz ended.")
        break
    if not answer.isdigit():
     print('invalid. please enter a number')
     continue

    if int(answer) == num1 * num2:
        print("Correct")
    else:
        print("Incorrect, try again")
        
#7
count = 0 

while count < 3:
    name = input('enter a name: ')
    if name.lower() == 'exit':
        print('Game closed.')
        break
    if name.lower() == 'goodluck':
        count+=1
        
        if count ==3:
            print('you have typed goodluck 3 times')
        else:
            print(f'you typed goodluck {count} times.')
    else:
        print('wrong name')
            
#8
import random
num = random.randint(1,50)

attempts = 7
while attempts > 0:
    guess= int(input('guess a number between 1 to 50: '))
    
    if guess == num:
        print('you guessed the number')
        break
    else:
        attempts-= 1
        if attempts>0:
            print(f'wrong guess. you have {attempts} left')
        else:
            print(f'out of attempts the number was {num}')
            
#9
current_floor = 1
print('elevator starts at floor 1')
print('press 0 to exit')

while True:
    destination = input('enter floor number: ')
    
    if not destination.isdigit():
        print('invalid input.')
        continue
    
    destination = int(destination)
    
    if destination == 0:
        print('goodbye')
        break
            
    if destination > current_floor:
        print(f'elevator is going up from {current_floor} to {destination}')
        
    elif destination < current_floor:
        print(f'elevator is going down from {current_floor} to {destination}')
    else: 
        print(f'you are already on floor {current_floor}')
        
    current_floor=destination
    
#10
player1_score = 0
player2_score = 0

while True:
    player1 = input('player 1 (rock/paper/scissor): ').lower()
    player2 = input('player 2 (rock/paper/scissor): ').lower()

    if player1 == player2:
        print('it\'s a tie')

    elif (player1 == 'rock' and player2 == 'scissor') or \
         (player1 == 'paper' and player2 == 'rock') or \
         (player1 == 'scissor' and player2 == 'paper'):
        player1_score += 1
        print('player 1 wins this round')

    else:
        player2_score += 1
        print('player 2 wins this round')

    print('current score:')
    print('player 1 =', player1_score)
    print('player 2 =', player2_score)

    if player1_score == 5:
        print('player 1 won the game')
        break

    if player2_score == 5:
        print('player 2 won the game')
        break
    
#11
a = 1
b = 49

while a <= 49:
    print(a, '-', b)
    a += 1
    b -= 1
    
#12
num = int(input('enter a number: '))

total = 0
i = 1

while i <= num:
    total += i
    i += 1

print('sum =', total)

#13
alpha = 65

while alpha <= 90:
    print(chr(alpha), end=' ')
    alpha += 1
    
#14
number = [2, 40, 21, 31, 10, 7, 5]

i = 0

while i < len(number):
    if number[i] < 20:
        print(number[i])
    i += 1
        
        
            
    