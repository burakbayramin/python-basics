try:
    file = open("testfile3.txt", "r")
except FileNotFoundError:
    print("File not exist")
print("---")
    
file = open("testfile2.txt", "r")
for i in file:
    print(i, end="")
file.close()
print("\n---")

file = open("testfile2.txt", "r")
content = file.read()
print("Names 1: ")
print(content)

content2 = file.read()
print("Names 2: ")
print(content2)
file.close()
print("---")

file = open("testfile2.txt", "r")
print(file.readline())
print(file.readline())
print(file.readline())
file.close()
print("---")

file = open("testfile2.txt", "r")
list = file.readlines()
print(list)
file.close()
print("---")

with open("testfile2.txt", "r") as file:
    print(file.tell())
    file.seek(4)
    print(file.tell())
print("---")

with open("testfile3.txt", "r") as file:
    file.seek(6)
    content = file.read(10)
    print(content)
    print(file.tell())
    file.seek(0)
    content = file.read(7)
    print(content)
    print(file.tell())    

