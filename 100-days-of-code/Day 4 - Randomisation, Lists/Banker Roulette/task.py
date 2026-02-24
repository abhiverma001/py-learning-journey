import random

friends =["Verma", "Maurya", "Tiwari", "Dubey", "Abhinav", "Gupta"]

#Option-1
random_num = random.randint(0,5)
print(friends[random_num])
print(f"Picked random name from option-1 is {friends[random_num]}")

print()

#Option2
print(random.choice(friends))

print(f"Picked random name from option-2 is {random.choice(friends)}")


