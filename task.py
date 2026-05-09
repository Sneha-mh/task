#4
username = input("Enter username: ")
password = input("Enter password: ")

if username == "admin" and password == "ad123":
    print("Access Granted: Faculty Dashboard")
elif username == "student" and password == "st2026":
    print("Access Granted: Notes and Practice Questions")
else:
    print("Invalid Credentials. Please try again.")
    
#5
color = input("Enter traffic light color (red, yellow, green): ").lower()
if color == "red":
    print("Stop")
elif color == "yellow":
    print("Ready")
elif color == "green":
    print("Go")
else:
    print("Invalid traffic light color")


#6
season_number = int(input("Enter season number (1-4): "))
match season_number:
    case 1:
        print("Spring")
    case 2:
        print("Summer")
    case 3:
        print("Autumn")
    case 4:
        print("Winter")
    case _:
        print("Invalid season number. Please enter a number between 1 and 4.")
        
#7
age = int(input("Enter your age: "))
income = float(input("Enter your monthly income: "))
credit_score = int(input("Enter your credit score: "))

if 21 <= age <= 60 and income >= 30000 and credit_score >= 700:
    print("Loan Approved ")
else:
    print("Loan Not Approved ")
    if not (21 <= age <= 60):
        print("Condition Failed: Age must be between 21 and 60.")
    if income < 30000:
        print("Condition Failed: Monthly income must be at least 30,000.")
    if credit_score < 700:
        print("Condition Failed: Credit score must be at least 700.")
        
#8
age = int(input("Enter your age: "))
membership = input("Do you have a membership card? (yes/no): ").lower()
if age < 12:
    print("Ticket Price: Free ")
else:
    if age <= 60:
        if membership == "yes":
            print("Ticket Price: Rs. 150 ")
        else:
            print("Ticket Price: Rs. 200 ")
    else:
        print("Ticket Price: Rs. 100  (Senior Citizen Discount)")
        
#9
salary = float(input("Enter your salary: "))
year_of_service = int(input("Enter your years of service: "))
if  year_of_service > 5:
    bonus = salary * 0.05
    print(f"Bonus Amount: Rs. {bonus:.2f}")
else:
    print("No bonus awarded. Years of service must be greater than 5.")
    
#10
radius = float(input("Enter the radius of the circle: "))
if radius <= 0:
    print("Invalid radius. Please enter a positive number.")
    
else:
    area = 3.14159 * radius ** 2
    print(f"The area of the circle is: {area:.2f}")
    
    
#11
age = int(input("Enter your age: "))
gender = input("Enter your gender (M/F): ").upper()
days = int(input("Enter number of working days: "))

if 18 <= age < 30:
    if gender == "M":
        wage_per_day = 700
    elif gender == "F":
        wage_per_day = 750
   
elif 30 <= age <= 40:
    if gender == "M":
        wage_per_day = 800
    elif gender == "F":
        wage_per_day = 850
   


if wage_per_day > 0:
    total_wage = wage_per_day * days
    print("Wage per day:", wage_per_day)
    print("Total wage for", days, "days:", total_wage)
else:
    print("No wage applicable for the given age/gender.")
    

#12
number = int(input("Enter a number: "))
if number % 3 == 0 and number % 5 == 0:
    print("FizzBuzz")
elif number % 3==0 and number % 5 != 0:
    print("Fizz")
elif number % 5 == 0 and number % 3 != 0:
    print("Buzz")
else:
    print(number)


#13
units = int(input('enter number of units: '))
if units <100:
    cost = units * 5
elif units <=300:
    cost = 100 * 5 + (units - 100) * 8
else:
    cost = 100 * 5 + 200 * 8 + (units - 300) * 10
    print(f'total cost: Rs. {cost}')
    
#14
player1 = input("player 1, enter your move (rock paper or scissors):").lower()
player2 = input("player 2, enter your move (rock paper or scissors):").lower()
action_list = {"rock", "paper", "scissors"}
if player1 not in action_list or player2 not in action_list:
    print("invalid input")
else:
    if player1 == player2:
        print("it is a tie")
    elif ( player1 == "rock" and player2 == "scissors"):
        print("player 1 wins") 
    elif (player1 == "paper" and player2 == "rock"):
        print("player 1 wins")
    elif (player1 == "scissors" and player2 =="paper"):
        print("player 1 wins")
    else:
        print("player 2 wins")


#15
number = int(input("enter a number: "))
if number <0:
    print("number must be positive.")
else:
    if number % 2 == 0:
        print(f"{number} is even")
    else:
        print(f'{number} is odd')
        
#16
total_amount =float(input("enter a number:"))
is_member = input("are you a member (yes?no):").lower()
if total_amount > 1000 and is_member == "yes":
    discount = total_amount * 0.20
    final_amount = total_amount - discount
    print(f"final amount after discount is: Rs.{final_amount}")
elif total_amount > 1000 and is_member == "no":
    discount = total_amount * 0.10
    final_amount = total_amount - discount
    print(f'final amount after discount: rs. {final_amount}')


#17
weight = float(input("enter your weight: "))
planet = int(input("enter planet number: "))
if planet == 1:
    destination_weight = weight * 0.38
    print(f"your weight in mercury is: {destination_weight}")
elif planet == 2:
    destination_weight = weight * 0.91
    print(f"your weight in venus is: {destination_weight}")
elif planet == 3:
    destination_weight = weight * 0.38
    print(f'your weight in mars is: {destination_weight}')
elif planet == 4:
    destination_weight = weight * 2.34
    print(f"your weight in jupiter is: {destination_weight}")
elif planet == 5:
    destination_weight = weight * 1.06
    print(f"your weight in saturn is: {destination_weight}")
elif planet == 6:
    destination_weight = weight * 0.92
    print(f"your weight in uranus is: {destination_weight}")
elif planet == 7:
    destination_weight = weight * 1.19
    print(f"your weight in neptune is: {destination_weight}")
else:
    print("invalid planet number")
    
#18
marks1 = int(input("enter your marks in subject 1: "))
marks2 = int(input("enter your marks in subject 2: "))
marks3 = int(input("enter your marks in subject 3: "))
marks4 = int(input("enter your marks in subject 4: "))
total_marks = marks1 + marks2 + marks3 + marks4
percentage = (total_marks / 400) * 100
print("total marks:", total_marks)
print("percentage:", percentage)
if percentage > 70:
    print("grade: distinction")
elif percentage > 60:
    print("grade: first")
elif percentage > 40:
    print("grade: pass")
else:
    print("grade: fail")


#19
balance = 5000
is_valid = True
correct_pin = 123
if is_valid:
    pin = int(input("enter your pin: "))
    if pin == correct_pin:
        print("menu:")
        print("1. Withdraw")
        print("2. Check Balance")
        print("3. Exit")
        option = int(input("select an option: "))
        if option == 1:
            amount = float(input("enter amount to withdraw: "))
            if amount <= balance:
                balance -= amount
                print(f"withdrawal successful. current balance: Rs.{balance}")
            else:
                print("insufficient balance.")
        elif option == 2:
            print(f"current balance: Rs.{balance}")
        elif option == 3:
            print("thank you for visiting.")
        else:
            print("invalid option.")
    else:
        print("wrong pin.")
        
        
#20
direction = input("enter you direction: (north, south): ").lower()
if direction == "south":
    print("game over")
else:
    way = input("enter your choice: (cross the river, folow the path): ").lower()
    if way == "cross the river":
        print("game over")
    else:
        character = input("enter your choice: (fairy, elf, orge): ").lower()
        if character == "orge" or character == "fairy":
            print("game over")
        else:
            print("you win")
            
    
#21
floor = int(input("Enter floor number: "))

if floor < 0 or floor > 10:
    print("Invalid floor number")

else:
    print("Valid floor number")

    weight = int(input("Enter total weight: "))

    if 0 <= weight <= 500:

        
        door = input("Is the door closed? (yes/no): ").lower()

        if door == "yes":
            print("Elevator is moving")
        else:
            print("Warning: Close the door")

    else:
        print("Overweight: Lift cannot move")
        
    
        
        
    
        
   
        
        
    


        
    
        
        
    
        
   
        
        
    

