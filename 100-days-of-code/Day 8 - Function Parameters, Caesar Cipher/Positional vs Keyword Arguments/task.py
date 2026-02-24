# # Functions with input

# def greet_with_name(name):
#     print(f"Hello {name}")
#     print(f"How do you do {name}?")


# greet_with_name("Jack Bauer")



# # Functions with more than 1 input
# def greet_with(name, location):
#     print(f"Hello {name}")
#     print(f"Happy to know you belong to my native plance : {location}")

# name = input("please give your name :")
# location = input("please provide you location :")

# greet_with(name, location)




#Love calc
def calculate_love_score(name1, name2):
    combine_name = (name1 + name2).lower()
    true_count = 0
    for letter in "true":
        true_count += combine_name.count(letter)

    love_count = 0
    for letter in "love":
        love_count += combine_name.count(letter)

    love_score = int(f"{true_count}{love_count}")
    print(f"Love Score = {love_score}")

calculate_love_score("Kanye West", "Kim Kardashian")            

