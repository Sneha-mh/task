#i
email = {'ram':'ram@gmail.com',
         'shyam':'shyam@gmail.com',
         'hari':'hari@gmail.com'}
name=input('enter a username')
print(email.get(name, "user not found"))

#ii
email = {'ram':'ram@gmail.com',
         'shyam':'shyam@gmail.com',
         'hari':'hari@gmail.com'}
name=input('enter a username')
if name in email:
    print(email[name])
else:
    print("user not found")
    
#2
shopping_list = {'milk', 'bread', 'eggs'}
bought = {'bread', 'eggs'}
unbought = shopping_list.difference(bought)
print(unbought)
if not unbought:
    print("shopping complete")
else:
    print(f'unbought items: {unbought}')
    
#3
class_list = ['ram', 'sita', 'laxman']
new_student = input('enter new students name: ')
if new_student in class_list:
    print("student already exists")
else:
    class_list.append(new_student)
    print("student added successfully") 
    
   
#4   
votes = ['blue', 'red', 'blue', 'green', 'blue']
blue_count = votes.count('blue')
if blue_count >= 3:
    print("blue wins")
else:
    print("blue loses")
    
#5
grades = {'Ram':92, 'Sita':88}
name = input('enter name of student: ')
if name in grades:
    print(grades[name]) 
else:
    print('grade is not available')
    
#6
applicants = {'name':'priya', 'skills':['java', 'SQL'], 'experience years': 1}
required_skills = ['python', 'java']
skills = bool(set(applicants['skills'])& set(required_skills))
experience = applicants['experience years'] >= 2
if skills and experience:
    print('priya qualifies')
else:
    print('priya does not qualify')
    
#7
banned_items = {'scissors', 'knife', 'lighter'}
weight = float(input('Enter the baggage weight : '))
item = input('Enter the name of item : ').lower()
if weight <= 7 and item not in banned_items:
    print('Bag allowed')
else:
    print('Bag not allowed')


#8
sample_dict = {
    'emp1': {'name': 'Jhon', 'salary': 7500},
    'emp2': {'name': 'Emma', 'salary': 8000},
    'emp3': {'name': 'Shyam', 'salary': 500}
    }
sample_dict.update({'emp3': {'name': 'Shyam', 'salary': 8500}})
print(sample_dict)


#9
ram_items = {'apple', 'banana', 'mango'}
laxman_items = {'grapes', 'orange', 'watermelon'}
if ram_items.isdisjoint(laxman_items):
    print('They picked completely different items')
else:
    print('They have some common items')
    
#10
list_data = [10, 20, 30]
tuple_data = (10, 20, 30)
set_data = {10, 30}
dict_data = {'a': 1, 'b': 2, 'c': 3}

val = 20
if val in list_data and val in tuple_data:

    
    if 'b' in dict_data and val not in set_data:
        print('Path A')

    else:
        print('Path B')

else:
    print('Path C')
    
    
#11
#The value of a becomes 30

#12
#[1,2,3] cannot be used as key

#13
#Not found

#14
#2

#15
#my_set.add(40)

#16
menu = {'pizza': 15, 'burger': 10, 'salad': 8}
order = 'pizza'

if order in menu:
    print(menu[order])
else:
    print('item not found')

#17
student_data = {'name': 'sam', 'score': 85}
if student_data['score'] >= 80:
    student_data['status']='passed'
else:
    student_data['status']='review'
print(student_data)

#18
database = {'admin': '1234', 'user': 'abcd'}
user_input = 'admin'
user_pass = '1234'
if user_input in database and database[user_input] == user_pass:
    print("login successful")
else:
    print("login failed")
    
    
#19
emails = {'ram123@gmail.com', 'hari77@gmail.com'}
blacklisted_email = {'hari77@gmail.com'}
current_email = {'hari77@test.com'}
if current_email in emails and current_email not in blacklisted_email:
    print('email sent')
else:
    print('blocked')
    
    
#20
inventory = {'A1': 50, 'B2': 0, 'C3': 10}
restricted_zones = {'B2', 'Z9'}
target = 'B2'
if target in inventory:
    
    
    if target not in restricted_zones and inventory[target] > 0:
        print('dispatch item')
    else:
        print('stock error')
        
else:
    
    print('invalid zone')
    
    
#21
valid_courses = {'python', 'robotics', 'java'}
hs_grades = [9, 10, 11, 12]
name_input = input('Enter student name: ')
course_input = input('Enter requested course: ').strip().lower()  
grade_input = int(input('Enter high school grade (integer): '))
student_records = {
    'name': name_input,
    'course': course_input,
    'grade': grade_input
}
if student_records['course'] not in valid_courses:
    print(f"{student_records['name']} selected an invalid course.")
else:
    
    if student_records['grade'] not in hs_grades:
        if student_records['grade'] < 9:
            print('grade too low')
        elif student_records['grade'] > 12:
            print('grade too high')
    else:
        print('Enrollment successful!') 

  
    
    


    
    

    


