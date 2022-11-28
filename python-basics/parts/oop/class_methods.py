class Book():
    
    def __init__(self, name, page, type):
        self.name = name
        self.page = page
        self.type = type
        
    def __str__(self):
        return "Name : {}\nPage : {}\nType : {}".format(self.name, self.page, self.type)
    
    def __len__(self):
        return self.page
    
    def __del__(self):
        print("Book is removed")
    
b1 = Book("ABC", 120, "Adventure")
