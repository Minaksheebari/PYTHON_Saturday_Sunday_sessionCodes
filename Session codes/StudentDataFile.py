##Take input from the user, student name,age,phy,sci,eng
#create student.csv file
import os
def createFile():
    if not os.path.exists("student.csv"):
        fileObject = open("student.csv",'w')
        data = "Name\t Age\t Physics\t English\t Science"
        fileObject.write(data)
    else:
        print("File already exist!")
createFile()

def UserInput(): 
    studName = input("Enter your name: ")
    studAge = int(input("Enter Age: "))
    physicsMarks = int(input("Enter Marks for Physics: "))
    englishMarks = int(input("Enter Marks for English: "))
    scienceMarks = int(input("Enter Marks for Science: "))

    return studName,studAge,physicsMarks,englishMarks,scienceMarks

def writeFile(studName,studAge,physicsMarks,englishMarks,scienceMarks):
    fileObject = open("student.csv",'a') 
    data = "\n" + studName + "\t " + str(studAge) + "\t " + str(physicsMarks) + "\t " + str(englishMarks) + " \t" + str(scienceMarks)
    fileObject.write(data)

studName,studAge,physicsMarks,englishMarks,scienceMarks=UserInput()
writeFile(studName,studAge,physicsMarks,englishMarks,scienceMarks)

def readFile():
    fileObject = open("student.csv",'r')
    data = fileObject.read()
    print(data)

def userData(userName):
    fileObject = open("student.csv",'r')
    for line in fileObject:
        stringArray = line.split("\t")
        if stringArray[0] == userName:
            print(line)


readFlag = input("Do you want to read the file?")
if readFlag == "y":
    readFile()
    userName = input("For whome you are looking for? ")
    userData(userName)