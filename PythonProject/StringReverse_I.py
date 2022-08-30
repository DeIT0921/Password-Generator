# define a function called reverseString that takes in one argument
def reverseString(string):
    
    lenstring = len(string) # declare a variable containing the length of the string
    
    newstring = "" # declare a variable with an empty string
    
    # loop through a range function, 
    # where the first argument is 1 and second 
    # argument is length of the string (second variable) plus one
    for i in range(lenstring):
        # get the negative index of the string, and add it to the first variable
        newstring = newstring + string[lenstring-1-i]
    # print the first variable
    print(newstring)
    
    
# test cases
reverseString("Python")
reverseString("Hello world")
reverseString("Foobar")