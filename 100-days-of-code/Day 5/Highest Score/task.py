student_scores = [150, 142, 185, 120, 171, 184, 149, 24, 59, 68, 199, 78, 65, 89, 86, 55, 91, 64, 89]

total_exam_number = sum(student_scores)   #Directly sum of all numbers
print(total_exam_number)

#OR

number = 0
for score in student_scores:   #using for loop to sum all the numbers
    number += score
print(number)


#To print the max or min numbers from the list
max_number = max(student_scores)
min_number = min(student_scores)
print(f"Highest number is {max_number}")
print(f"Lowest number is {min_number}")

#another way to get the max or min number using conditions, list, and forloop
score = 0  #this is store the value what is getting from line 24
for max_number1 in student_scores:
    if max_number1 > score:
        score = max_number1
print(score)

#So this function will keep executing until all the numbers are not finished in the list student_scores
#and at each execution it will store the received value in score (line 21) also will keep comparing the values form previous stored values
# e.g. take 150 and compare with 0 then take 142 and compare with 0 and 150 both then take 185 and compare with all previous three values
# similar way it way keep going and will get the highest value.

for min_number1 in student_scores:
    if min_number1 < score:
        score = min_number1
print(score)

