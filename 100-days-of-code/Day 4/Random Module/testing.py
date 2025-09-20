import random

#random functions

random_integer = random.randint(1,10)
print(random_integer)

random_number_0_1 = random.random()
print(random_number_0_1)

random_float = random.uniform(1, 10)
print(f"random_float = {random_float}")


#To print heads and tails randomly for practice
random_heads_tails = random.randint(0,1)
if random_heads_tails == 0:
    print("Heads")
else:
    print("Tails")
