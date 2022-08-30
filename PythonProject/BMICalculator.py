# define a function called bmi_calculator
def bmi_calculator(weight, height):
    bmi = weight / (height ** 2)
    return bmi

# define a function called bmi_category
def bmi_category(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif bmi < 25:
        return "Normal"
    elif bmi < 30:
        return "Overweight"
    else:
        return "Obesity"

# main code
restart = True
print("\tBMI (Body-mass index) Calculator")
print("-------------------------------------------------------\n")
print("Test Cases:")
# use height = 1.69 and weight = 69
print("Weight: 69, Height: 1.69 =====> BMI: {:.2f}".format(bmi_calculator(69, 1.69)) + ", BMI Category: " + bmi_category(bmi_calculator(69, 1.69)) + "\n")
while True:
    weight = float(input("Please enter your weight in kilograms (kg): "))
    height = float(input("Please enter your height in meters (m): "))
    # declare a variable called "result" and 
    # assign it the result of using the function 
    result = bmi_calculator(weight, height)

    # print the "result" variable
    # two ways method to print the result
    print("\nYour BMI = {:.2f}".format(result)) # method 1
    print("Your BMI Category is:", bmi_category(result)) # method 2
    print("-------------------------------------------------------\n")

    while True:
        decision = input("Do you want to input more data? (Y/N) ")
        if decision == "Y" or decision == "y":
            break
        elif decision == "N" or decision == "n":
            restart = False
            break
        else:
            print("Invalid input, please try again.")
    if(restart == False):
        print("Thank you for using this program.")
        break