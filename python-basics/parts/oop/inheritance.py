class Person():
    
    def __init__(self, fname, lname, colors):
        print("Person info")
        self.fname = fname
        self.lname = lname
        self.colors = colors
        
    def info(self):
        print(
        """
        First Name : {}
        Last Name : {}
        Favorite Colors : {}
        """.format(self.fname, self.lname, self.colors)
        )
        
    def color(self, color):
        self.colors.append(color)

        
class Child(Person):
    pass

child1 = Child("Hank", "Schrader", ["red", "black"])
child1.color("yellow")
child1.info()


class Student(Person):
    
    def __init__(self, fname, lname, colors, department):
        super().__init__(fname, lname, colors)
        print("Student info")
        self.department = department

    def info(self):
        print(
        """
        First Name : {}
        Last Name : {}
        Favorite Colors : {}
        Department : {}
        """.format(self.fname, self.lname, self.colors, self.department)
        )
        
student1 = Student("Walter", "White", ["yellow", "green"], "Chemistry")
student1.info()

        

        
    