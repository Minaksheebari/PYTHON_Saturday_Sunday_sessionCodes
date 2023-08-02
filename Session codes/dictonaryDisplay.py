# students = ["Minu","Raj","Lakshmi"]

# for name in students:
#     print(name)

marks = [75,96,85]
name = input("Enter your name: ")

#Using sum function
print("The name is", name, " and the total marks are: ", sum(marks))

print("The name is", name, " and the total marks are: ", marks[0]+marks[1]+marks[2])

#dictionary keyivalue pair

sub_mar = {"Math":95, "Sci":85, "Eng":75}
print(sub_mar.keys())
print(sub_mar.values())
print(sub_mar)

#sum of subjects in dictionary
total = 0       #OR total = sum(sub_mar.values() & then print total
for marks in sub_mar.values():
    total+=marks
print("Total marks are: ", total)
#using sum() 
#print("Total marks are: ", sum(sub_mar.values()))

#Use of append
my_dict = {"name":[],"age":[]}
my_dict["name"].append("Minu")
my_dict["age"].append(27)

#User input
user_input = input("Enter the name ")
my_dict["name"].append(user_input)

user_input2 = int(input("Enter the age "))
my_dict["age"].append(user_input2)
print(my_dict)

#my_dict["name"]["age"].append("Minu",27)