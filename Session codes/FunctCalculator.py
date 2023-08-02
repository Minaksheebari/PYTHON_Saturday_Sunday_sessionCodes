# Break the problem statements into seperate blocks
# write the skeleton of the program with function names
# Write functions in seperate files with arguments and return. 
# Test the individual functions.
# write the main code importing all the functions.
from multiply import multiply
from addition import addition
from division import division
from subtraction import subtract

# def add():
#     total= num1 + num2
#     print("Addition of ", num1, " + ", num2, " is: ", total)

# def mul():
#     total= num1 * num2
#     print("Multiplication of ", num1, " * ", num2, " is: ", total)

# def sub():
#     total= num1 - num2
#     print("Subtraction of ", num1, " - ", num2, " is: ", total)

# def div():
#     total= num1 / num2
#     print("Division of ", num1, " / ", num2, " is: ", total)

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
operator = input("Enter operator: ")


if(operator == "+"):
    result = addition(num1,num2)
    print("Addition of ", num1, " + ", num2, " is: ", result)

elif(operator == "-"):
    result = subtract(num1,num2)
    print("Subtraction of ", num1, " - ", num2, " is: ", result)

elif(operator == "/"):
    result = division(num1,num2)
    print("Division of ", num1, " / ", num2, " is: ", result)

elif(operator == "*"):
    result = multiply(num1,num2)
    print("Multiplication of ", num1, " * ", num2, " is: ", result)



#Another way
# def multiply(num1,num2):
#     return num1*num2

# if(operator=="*"):
#     result = multiply(num1,num2)