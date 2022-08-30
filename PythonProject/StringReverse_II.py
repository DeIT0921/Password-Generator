# define a function called reverseString_v2 that takes in one argument
def reverseString_v2(string):
    result = reversed(string)
    # use the reversed() function with the argument and assign it to a variable
    list_result = list(result)
    # use the list() function with the variable above and assign it to another variable
    print("".join(list_result))
    # use the .join method of the list above and turn the list into a string and assign it to another variable
    # print the variable above


# test cases
reverseString_v2("Hello world")
reverseString_v2("Python rocks")
reverseString_v2("I enjoy Python")