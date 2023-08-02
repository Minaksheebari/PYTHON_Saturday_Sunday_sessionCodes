#BASE CLASS
class Car:
    #brand,model
    brand = "Honda"
    model = "Xuv"
    def __init__(self,brand,model):
        self.brand = brand
        self.model = model
    
    def brake(self):
        return "Brakes Applied"

    def accelator(self):
        return "Speed Increased"

#Child Class

class Bmw(Car): 
    def __init__(self,brand,model,engine,noOfSeats):
        super().__init__(brand,model) #Using super you can access base cls arguments
        self.engine = engine
        self.noOfSeats = noOfSeats
    
    def display(self):
        print("The car has " + self.engine + " and " + self.noOfSeats + " number of seats.")

    def brake(self):
        return super().brake()
        #b = super().brake()
        #print(b)
        #return b 
        #return "New Brake" #if we don't return anything it will show None

Bmw1 = Bmw("Audi","Au7","En89","7")
print(Bmw1.brake())
print(Bmw1.accelator())
Bmw1.display()
print(Bmw1.engine)
print(Bmw1.brand)
print(Bmw1.brake())  #printing object's address if I remove () aftere Brake
