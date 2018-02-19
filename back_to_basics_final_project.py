import statistics as s 
admins = {'Doug':'Funny'}
students = {"sam":[77,88,99],
            'Alex':[92,76,88],
            'digs':[1,40,33]}

def enter_grades():
  print(students)
  name = input('Student Name: ')
  grade = input('Grade: ')

  if name in students:
    print('adding grade')
    students[name].append(grade)
  else:
    print('student doesnt exit')

  print(students)

def remove_student():
  print(students)
  name = input("Who would you like to remove ")

  if name in students:
    del students[name]

  print(students)

def average_grades():
  for eachStudent in students:
    grades = students[eachStudent]
    avgGrade = s.mean(grades)

    print(eachStudent,'has an average grade',avgGrade)

def menu():
  print('[1] - Enter Grades')
  print('[2] - Remove Student')
  print('[3] - Student Average Grades')
  print('[4] - Exit')

  selection = input("What would you like to do today?  ")

  if selection == '1':
    enter_grades()
  elif selection == '2':
    remove_student()
  elif selection == '3':
    average_grades()
  elif selection == '4':
    exit()
  else:
    print('invalid input')


login = input("Username: ")
passw = input("Password: ")

if login in admins:
  if admins[login] == passw:
    while True:
      menu()
else:
  print("invlaid username")
  