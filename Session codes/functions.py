#defining the function
def printName():
    print("Minu")
#Calling the function
printName()

#Function Argument
def printNameArg(name,age,city):
    print(name,age,city)
printNameArg("Minu",27,"Jalgaon")

#Dictionary Argument
student={"name":"Sohail", "age":35,"city":"Delhi"}

def printDicArg(student):
    print(student)   #for single data- print(student["name"]) 
    return(student["age"]-2)
printDicArg(student)

modifiedAge = printDicArg(student)
print(modifiedAge)

#Call by value - primitive data types eg. int,float
#call by reference - non-primitive data types eg. array,list,string

