with open("testfile4.txt", "r+", encoding="utf-8") as file:
    print(file.read())
print("---")
    
with open("testfile4.txt", "a", encoding="utf-8") as file: #"a" goes end
    file.write("Dwayne Wade\n")
    
with open("testfile4.txt", "r+", encoding="utf-8") as file:
    print(file.read())
print("---")

with open("testfile4.txt", "r+", encoding="utf-8") as file:
    content = file.read()
    content = "Sebastian Vettel\n" + content
    file.seek(0)
    file.write(content)
    
with open("testfile4.txt", "r+", encoding="utf-8") as file:
    print(file.read())
print("---")

with open("testfile4.txt", "r+", encoding="utf-8") as file:
    list = file.readlines()
    list.insert(3, "John Cena\n")
    file.seek(0)
    for i in list:
        file.write(i)
    
with open("testfile4.txt", "r+", encoding="utf-8") as file:
    print(file.read())
print("---")

with open("testfile4.txt", "r+", encoding="utf-8") as file:
    list = file.readlines()
    list.insert(5, "Emily\n")
    file.seek(0)
    file.writelines(list)
    
with open("testfile4.txt", "r+", encoding="utf-8") as file:
    print(file.read())