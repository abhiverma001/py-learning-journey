#Shopping List manager
import random
from xml.dom.minidom import ProcessingInstruction

print("\n Shopping List Manager")
shopping_list = []

item1 = input("Enter the first item to add:")
shopping_list.append(item1)
print("Added:", item1)

item2 = input("Enter the second item to add:")
shopping_list.append(item2)
print("Added:", item2)

item3 = input("Enter the third item to add:")
shopping_list.append(item3)
print("Added:", item2)

print("Current list of items:", shopping_list)

#remove an item
remove_item = input("Enter an item to remove from list:")
if remove_item in shopping_list:
    shopping_list.remove(remove_item)
    print("Removed:", remove_item)
else:
    print("Item not found in shopping list")

print("Current shopping list:", shopping_list)

#Password generator
print("\n Password Manager")
length_input = int(input("Enter desired password length: "))

# Possible characters for password
letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
digits = "0123456789"
symbols = "!@#$%^&*"

all_chars = letters + digits + symbols

password = ""
for i in range(length_input):
    password += random.choice(all_chars)
print("Your generated password is : ", password)

#login attempt
login_pass = input("\nPlease enter same password to login : ")
if login_pass == password:
    print("Login Done!")
else:
    print("Login Failed.")