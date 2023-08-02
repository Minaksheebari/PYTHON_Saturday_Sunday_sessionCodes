class Employee:
    comName = ""
    comAdd = ""
    comDept = ""

    def __init__(self,comName,comAdd,comDept):
        self.comName = comName
        self.comAdd = comAdd
        self.comDept = comDept
    
class SalaryNew(Employee):
    def __init__(self, comName, comAdd, comDept):
        super().__init__(comName, comAdd, comDept)

    def display(self):
        print("Company name: " + self.comName + "\n" + "Address: " + self.comAdd + "\n" + "Department: " + self.comDept)

    def salary(self,perDaySalary,noOfWorkingDays):
        self.perDaySalary = perDaySalary
        self.noOfWorkingDays = noOfWorkingDays

        totalSalary = int(perDaySalary) * int(noOfWorkingDays)
        return totalSalary
        #print("Your total salary is: ", totalSalary)

class TechSkills(SalaryNew):
    def __init__(self, comName, comAdd, comDept):
        super().__init__(comName, comAdd, comDept)

    def skills(self,edu,technical):
        self.edu = edu
        self.technical = technical
        print("We required qualification: " + self.edu + " and technical skill in: " + self.technical)

emp1 = TechSkills("TCS","Pune","IT")
emp1.display()
print("Your salary is: " ,  emp1.salary(200,28))
emp1.skills("MCA","FSD")
print("============================================================")

emp2 = TechSkills("IBM","Nashik","Sales")
emp2.display()
# perDaySalary = 250
# noOfWorkingDays = 28
print("Your salary is: " , emp2.salary(180,28))
emp2.skills("MBA","Marketing")
print("============================================================")

emp3 = TechSkills("HCL","Delhi","BPO")
emp3.display()
print("Your salary is: " ,  emp3.salary(150,28))
emp3.skills("Graduate", "Cold calls")