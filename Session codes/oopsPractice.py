class StudentsData:
    def __init__(self,name,course,total,grade):
        self.name =name
        self.course = course
        self.total = total
        self.grade = grade
    
    

minuData = StudentsData("Minakshee","FSD",500,'A+')
vaibhData = StudentsData("Vaibhav","FSD",450,'B')
UrviData = StudentsData("Urvashi","FSD",460,'A')

#print(minuData,vaibhData,UrviData) #It only gives you address of the object
print(minuData.name, minuData.course, minuData.total, minuData.grade)
print(vaibhData.name, vaibhData.course, vaibhData.total, vaibhData.grade)
print(UrviData.name, UrviData.course, UrviData.total, UrviData.grade)
