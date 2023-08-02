students = []

flag = "y"
while flag == "y":
    student = {}
    studentName = input("Please enter the student Name: ")
    student["name"] = studentName
    subjectFlag = "y"
    subjects = []
    totalMarks = 0

    while subjectFlag == "y":
        subject = {}
        subjectName = input("Please enter the name of the subject: ")
        marks = int(input("Enter the marks for the subject: "))
        subject["name"] = subjectName
        subject["marks"] = marks
        subjects.append(subject)
        totalMarks += marks
        subjectFlag = input("Do you have any other subject data? (y/n) ")

    student["subjects"] = subjects
    student["totalMarks"] = totalMarks
    student["percentageMarks"] = (totalMarks / (len(subjects) * 100)) * 100

    if student["percentageMarks"] < 30:
        student["grade"] = "F"
        student["passStatus"] = False
    elif student["percentageMarks"] < 60:
        student["grade"] = "D"
        student["passStatus"] = True
    elif student["percentageMarks"] < 80:
        student["grade"] = "B"
        student["passStatus"] = True
    else:
        student["grade"] = "A"
        student["passStatus"] = True

    students.append(student)

    flag = input("Do you have any other student data? (y/n) ")

print("Student Marksheet Summary:")
for student in students:
    print("Name: ", student["name"])
    print("Subjects:")
    for subject in student["subjects"]:
        print("- Subject:", subject["name"])
        print("  Marks:", subject["marks"])
    print("Total Marks:", student["totalMarks"])
    print("Percentage: {:.2f}%".format(student["percentageMarks"]))
    print("Grade:", student["grade"])
    print("Pass Status:", "Passed" if student["passStatus"] else "Failed")
    print("-" * 20)
