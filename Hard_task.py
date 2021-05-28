#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Hard Level - Order of characters randomised:

password = ""
for char in range(1, nr_letters + 1):
  password += random.choice(letters)

for sym in range (1, nr_symbols + 1):
  password += random.choice(symbols)

for num in range(1, nr_numbers + 1):
  password += random.choice(numbers)

password_as_list = list(password)

random.shuffle(password_as_list)
shuffled_password = ''.join(password_as_list)

print(shuffled_password)

# can use the 'append' function as a password = [list] instead of password = "string"
# so password_list = []
# in for loop:
  #password_list.append(random.choice(letters)) 
#then just random.shuffle(password_list) then back into string using for loop to add to password again