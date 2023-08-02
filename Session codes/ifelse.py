#create a marksheet application for a school
# 3 subjects - maths, science, english
#Student name & marks of 3 subjects
#total marks, if the student has passed or not and grade of student.
#identify the topper from the batch i.e. Highest rank 
#we need to store that information in a variable using list
studNamesList = []
mathMarksList = []
scienceMarksList = []
englishMarksList = []
totalMarksList = []
percentageMarksList = []

flag="y"
while(flag=="y"):  #for storing multiple student's data 
     studName = input("Please enter the name of student: ")
     studNamesList.append(studName)

     mathMarks = int(input("Please enter Maths marks: ")) 
     mathMarksList.append(mathMarks)

     scienceMarks =  int(input("Please enter Science marks: ")) 
     scienceMarksList.append(scienceMarks)

     englishMarks =  int(input("Please enter English marks: ")) 
     englishMarksList.append(englishMarks)

#Processing the marks
     totalMarks = mathMarks+scienceMarks+englishMarks
     totalMarksList.append(totalMarks)
     print("Total marks of",studName, ": ",totalMarks)

#calculate percentage
     percentageMarks = (totalMarks/300)*100
     percentageMarksList.append(percentageMarks)
     print("Total percentage of", studName, ": ", percentageMarks)

#checking if studnet is pass or fail
#grade : 0 to 30: F, 30-60: D, 61-80: 
     if(percentageMarks<=30):
          print(studName," is Fail")
          print("Grade: F")
     elif(percentageMarks<=60):
           print(studName,"is PASS")
           print("Grade : C")
     elif(percentageMarks<=80):
          print(studName,"is PASS")
          print("Grade : B")
     elif(percentageMarks>80):
          print(studName,"is PASS")
          print("Grade : A")
     else:
          print("Try Again..")
     flag = input("do you have anyother student data y/n: ")

print(studNamesList)
print(totalMarksList)

#finding highest scorrer. 
# maxPercentage = max(percentageMarksList)
# maxIndex = percentageMarksList.index(maxPercentage)
# studMaxPercentage = studNamesList[maxIndex]
# print(studMaxPercentage,"has got Maximum percentage = ", maxPercentage)

#find maximum percentage using for loop
topper = 0
topperIndex = 0
for index in range(len(studNamesList)):
     if (totalMarksList[index]>topper): 
          topper = totalMarksList[index]
          topperIndex = index
print("The topper is: ", studNamesList[topperIndex])

#Find the rank of student as per their marks.
rankedData = []
for i in range(0,len(studNamesList)):
    rank = 1
    for j in range(0,len(studNamesList)):
        if percentageMarksList[j] > percentageMarksList[i]:
            rank += 1
    rankedData.append((rank,percentageMarksList[i],studNamesList[i]))

# Print the results with ranks
print("Rank\tName\t\tPercentage")
for data in rankedData:
    print(data[0], "\t", data[2], "\t", data[1])