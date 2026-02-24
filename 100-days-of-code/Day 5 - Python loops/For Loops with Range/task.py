for number in range(1, 11): #prin the value between 1-11
    print(number)

print()

for number in range(1, 11, 3):  #print the value between 1-11 but with 3 number gap
    print(number)



#practice, Work out the total of the numbers between 1 and 100, inclusive of both 1 and 100.
total = 0   #this is called
for number in range(1, 101):
    total += number
print(total)