#refer ifelse.py program first.
#List is non-primitive data type. Always name the variable of list in plural form because it is collection of data.
#in advance python we have concept of array. 

newLists = [23,45,65,80,95,"Sohail"]
print(newLists)

#update list
newLists[2]=75

#add new element at the end of the list
newLists.append("Minakshee")

#insert new element at specific index.
newLists.insert(2,"Urvi") #very rarly used in industry. 

print(newLists)

#newLists[6] = "Vaibhav" #will give indexError out of range

studNames = ["Minakshee","Urvi","Sunita"]
phyMarks = [90,30,60]
sciMarks = [96,67,26]
engMarks = [28,68,56]

#print(studNames[0]," has got ", phyMarks[0], " in Physics, ", sciMarks[0], " in Science and ",engMarks[0]," in English.")

print(len(studNames)) #access length of list for ending value in for loop.

#using loop
for index in range(0,3,1):
    print(studNames[index]," has got ", phyMarks[index], " in Physics, ", sciMarks[index], " in Science and ",engMarks[index]," in English.")
    # if(phyMarks[index]<30):
    #     print(studNames[index],"The student have failed in Physics.")

#append using loop
for index in range(1):
    studNames.append("Ayush")
    phyMarks.append(30)
    sciMarks.append(40)
    engMarks.append(50)
print(studNames,phyMarks,sciMarks,engMarks)

