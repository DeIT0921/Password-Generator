# import random and string libraries
import random
import string

def randomize_password(length, variation, reuse):
    random.seed(variation)
    # add string.ascii_letters with .digits and .punctuation, and assign it to a variable
    characters = string.ascii_letters + string.digits + string.punctuation

    # turn the string into a list with list(), and assign it to another variable
    characters = list(characters)

    # use random shuffle to shuffle the list
    for i in range(reuse):
        random.shuffle(characters)

    # slice the first 10 items from the list, and assign it to another variable
    password = characters[:length]

    # join the sliced shuffled list into a string with .join() and assign it to another variable
    password = "".join(password)
    return password

# set random seed to be 42
reuse = 1
password_length = 10
variation = 42
print("\tPassword Generator By Danar IT")
print("-------------------------------------------------------\n")
print("\tTest Cases:")
print("\tCurrent Random seed: 10, Password Length: 10 =====> Password: " + randomize_password(password_length, variation, reuse))
print("\tMaximum Lenght password is: " + str(len(string.ascii_letters + string.digits + string.punctuation)) + "\n")

# Invalid input for password length
while True:
    password_length = int(input("Please enter the length of the password: "))
    if password_length > 0:
        break
    else:
        print("Invalid input, please try again.")

# invalid input for random seed
while True:
    variation = int(input("Please enter the random seed: "))
    if variation > 0:
        break
    else:
        print("Invalid input, please try again.")

# print the joined string
print("\nPassword = " + randomize_password(password_length, variation, reuse))
while True:
    choice = input("\nDo you want to generate another password? (y/n): ")
    if choice == "y" or choice == "Y":
        reuse += 1
        print("\nPassword = " + randomize_password(password_length, variation, reuse))
    else:
        print("\nThank you for using this program.")
        break