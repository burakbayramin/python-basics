class Car():
    def __init__(self, model = "no info", power = 0, color = "White"): #constructor
        print("Object is created")
        self.model = model
        self.power = power
        self.color = color
        
car1 = Car("Mercedes", 300, "Black")
car2 = Car("BMW", 450, "Orange")
car3 = Car()

print(car1.model)
print(car2.power)
print(car3.model)