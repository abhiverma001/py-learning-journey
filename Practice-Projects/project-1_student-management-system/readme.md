# Student Management System (Simple Version)

## Overview
This is a beginner-friendly Python program to manage two students’ records. 
It allows adding student names and marks, calculates average and grade, and provides a simple search functionality.

## Features
- Add two students with marks for 5 subjects each.
- Calculate average marks.
- Determine grade based on average and subject marks.
- View all students.
- Search for a student by name.

## How it Works
1. **Student Storage**
   - All student details are stored in a list called `students`.
   - Each student is represented as a list: `[name, marks, average, grade]`.

2. **Adding a Student**
   - Program asks for the student name.
   - Program asks for marks in 5 subjects separated by space.
   - Marks are converted from strings to integers.
   - Average is calculated.
   - Grade is assigned:
     - Fail if any subject < 35
     - Average ≥ 75 → A
     - Average ≥ 60 → B
     - Average ≥ 40 → C
     - Else → Fail
   - Student details are added to the `students` list.

3. **Viewing All Students**
   - Prints all stored students with name, average, and grade.

4. **Searching a Student**
   - Program asks for a name to search.
   - If found, prints student details.
   - Otherwise, prints "Student not found."

## Key Concepts Used
- Input and output (`input`, `print`)
- Lists to store multiple data items
- Arithmetic operations
- Conditional statements (`if`, `elif`, `else`)
- Manual indexing in lists

## Example Run
Add first student:\
Enter student name: Arjun\
Enter marks for 5 subjects separated by space: 78 65 90 82 70

Add second student:\
Enter student name: Priya\
Enter marks for 5 subjects separated by space: 40 35 50 60 30

All Students:\
Name: Arjun | Avg: 77.0 | Grade: B\
Name: Priya | Avg: 43.0 | Grade: Pass

Enter student name to search: Priya\
Found: Priya | Avg: 43.0 | Grade: Fail