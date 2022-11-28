class Animal():
     
    def __init__(self, legs, color):
        print("Animal created")
        self.legs = legs
        self.color = color
         
    def walk(self):
        print("walking...")
        
a1 = Animal(4, "Grey")
a1.walk()

class Bear(Animal):
    
    def __init__(self, legs, color, speed):
        super().__init__(legs, color)
        self.speed = speed
        
    def attack(self):
        print("Attacking !!!!")

b1 = Bear(2, "Brown", 120)
b1.walk()
b1.attack()