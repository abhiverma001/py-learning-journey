# student_management_no_functions.py
from os.path import split
from re import search

students = [] #to store students details in list
#add first student
print("add first student:")
name1 = input("Enter student name:")
marks1 = input("Enter marks for 5 subjects separated by space: ").split()
marks1_numbers = [int(m) for m in marks1]  #It’s just a convenient way to convert a list of strings to a list of numbers in one line.

avg1 = (marks1_numbers[0] + marks1_numbers[2] + marks1_numbers[3] + marks1_numbers[4]) / 5

#Grade calculations
fail1 = False
if marks1_numbers[0] < 35 or marks1_numbers[1] < 35 or marks1_numbers[2] < 35 or marks1_numbers[3] < 35 or marks1_numbers[4] < 35:
    fail1 = True

if fail1:
    grade1 = "Fail"
elif avg1 >= 75:
    grade1 = "A"
elif avg1 >= 60:
    grade1 = "B"
elif avg1 >= 40:
    grade1 = "c"
else:
    grade1 = "Fail"

student1 = [name1, marks1_numbers, avg1, grade1]
students.append(student1)


# Add second student (same way)
print("\nAdd second student:")
name2 = input("Enter student name: ")
marks2 = input("Enter marks for 5 subjects separated by space: ").split()
marks2_numbers = [int(m) for m in marks2]

avg2 = (marks2_numbers[0] + marks2_numbers[1] + marks2_numbers[2] + marks2_numbers[3] + marks2_numbers[4]) / 5

fail2 = False
if marks2_numbers[0] < 35 or marks2_numbers[1] < 35 or marks2_numbers[2] < 35 or marks2_numbers[3] < 35 or marks2_numbers[4] < 35:
    fail2 = True

if fail2:
    grade2 = "Fail"
elif avg2 >= 75:
    grade2 = "A"
elif avg2 >= 60:
    grade2 = "B"
elif avg2 >= 40:
    grade2 = "C"
else:
    grade2 = "Fail"

student2 = [name2, marks2_numbers, avg2, grade2]
students.append(student2)

#view all students
print("\nAll Students:")
print(students)
print("Name:", students[0][0], "| Avg:", students[0][2], "| Grade:", students[0][3])
print("Name:", students[1][0], "| Avg:", students[1][2], "| Grade:", students[1][3])

#Search student by name
search_name = input("\n Enter student name to search:")
if search_name == students[0][0]:
    print("Found:", "Name:", students[0][0], "| Avg:", students[0][2], "| Grade:", students[0][3])
elif search_name == students[1][0]:
    print("Found:", "Name:", students[1][0], "| Avg:", students[1][2], "| Grade:", students[1][3])


