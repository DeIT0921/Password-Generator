import string
import random

number = 1,2,3,4,5,6,7,8,9,10
total = len(number)
# for i in range (total):
#     if(i==total-1):
#         print(number[i], end="")
#     else:
#         print(number[i], end = ", ")

# characters = string.ascii_letters + string.digits + string.punctuation
# print(list(characters))
# print("".join(list(characters)))

print(random.choice(string.ascii_letters))
characters = string.ascii_letters + string.digits + string.punctuation
print(len(characters))






# Python 3 code for printing
# on the same line printing
# geeks and geeksforgeeks
# in the same line

# print("geeks", end =" ")
# print("geeksforgeeks")

# # array
# a = [1, 2, 3, 4]

# # printing a element in same
# # line
# for i in range(4):
# 	print(a[i], end =" ")
