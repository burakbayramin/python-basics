class Person():
    
    def __init__(self, name, id, salary):
        self.name = name
        self.id = id
        self.salary = salary
        
    def info(self):
        print("""
            Person info 
            Name : {}
            Id : {}
            Salary : {} 
            """.format(self.name, self.id, self.salary))
        
    def raisee(self, amount):
        self.salary += amount
    
p1 = Person("Frank", 101, 100000)
p2 = Person("Hank", 110, 30)

p2.raisee(12000)

p1.info()
p2.info()    
        
   
        
        
        
