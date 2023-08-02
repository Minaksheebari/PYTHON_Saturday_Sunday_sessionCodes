userName = "Sanjoy"
userAge = 30
userProfession = "Teaching"
userskill = "FSD/DevOps"
userPhoneNumb = "123456789"
userAddress = "Kolkata 700140"
# This is a data for single user

#we use key & value pairs to store data in dictionaries
#Key = name,age,profession,skill,phone,address
#key is basically string in whole. 
#in Json also same way to write a code

#user is a dictonary.
user={
    "name":"Sanjoy",
    "age":30,
    "profession":"Teaching",
    "skill":"FSD/DevOps",
    "phoneNumber":"123456789",
    #nested dictonary
    "address": {"city":"Kolkata",
               "state": "WB",
               "PIN":"140"
               }
}
#adding new key-value to user
user["hobby"]="football"

print(user["name"]) 
#to print whole dictonary
print(user)

#to print the city of user
print(user["address"]["city"])

#now users is a list of dictionaries
users = {
    "name":"Sanjoy",
    "age":30,
    "profession":"Teaching",
    "skill":"FSD/DevOps",
    "phoneNumber":"123456789",
    #nested dictonary
    "address": {"city":"Kolkata",
               "state": "WB",
               "PIN":"140"
               }
},
{
    "name":"Minakshee",
    "age":30,
    "profession":"Teaching",
    "skill":"FSD/DevOps",
    "phoneNumber":"123456789",
    #nested dictonary
    "address": {"city":"Jalgaon",
               "state": "WB",
               "PIN":"140"
               }
}
#to print 2nd user in users.
#print(users[1]["name"])   Showing error

# create a dictionary variable for student, keys - name, marks
# create a list for student
# you need to store data in students list from the user
# print the summary of the student. 

students = []       #list to add dictionary values

#taking the inputes from the user
num_student = int(input("Enter the number of students: "))
for i in range(num_student):
    print("Enter the details of students ", (i+1), ": ")

    student = {}    #dictionary

    student['name'] = input("Enter the name: ")
    student['marks'] = int(input("Enter the marks: "))      #float() for decimal values

    students.append(student)

print(students)   #printing dictonary


print("Summary of all the students")

#to print the summary of students
for i in range(num_student):
    student_display = students[i]
    print("Student",(i+1))
    print("Name is: ",(student_display['name']))
    print("Marks are: ",(student_display['marks']))

#Using while loop
flag="y"
students=[]
print("***Enter Student details***")
while(flag=="y"):
    student={"name":input("Enter name of student : "),
             "marks":int(input("Enter the marks : "))}
    students.append(student)
    flag=input("do you want to store another student data : y/n : ")
print(students)