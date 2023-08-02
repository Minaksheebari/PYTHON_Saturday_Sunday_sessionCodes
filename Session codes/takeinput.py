#user-defined = user will defined or declare the functions as per need vs built-in functions = pre defined functions which are ready to use.
#input() is built in function which takes everything as a string. So we are using int before input.

name = input("Enter your name:")
chem = int(input("Enter Chemistry Marks:"))
phy = int(input("Enter Physics Marks:"))
maths = int(input("Enter Maths Marks:")) #OR after input() we can add int(maths)

total = chem+phy+maths
print("Your Total is: ", total)

print(type(total))


# maths = input("enter your maths mark")                            cntrl + / for commenting all together 
# chemistry = input("enter your chemistry mark")
# physics = input("enter your physics marks")
# total=int(maths) + int(chemistry) + int(physics)
# print("your total marks is :",total)