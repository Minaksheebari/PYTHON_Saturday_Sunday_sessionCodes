class Car:
    name = "Tata Nexon"

    #Constructor 
    #init will be calling by default.
    def __init__(self,name,topSpeed):    #constructor
        self.name = name
        self.topSpeed = topSpeed
    
    def longDrive(self):
        if self.topSpeed > 250:
            print(self.name, "Good for long drive")
        else:
            print(self.name, "Not good for long drive")

#myCar = Car()          #Create object
#print(myCar.name)      #Calling object using . DOT 

minuCar = Car("Ferrari",270)
urvashiCar = Car("Lamborgini",225)

print(minuCar.name, minuCar.topSpeed)
minuCar.longDrive()   #This is how abstraction is acheived,
# that we do not know what is happening in longDrive method 
# because there is no change in calling object.  

print(urvashiCar.name, urvashiCar.topSpeed)
urvashiCar.longDrive()