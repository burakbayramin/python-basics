i = 0
while(i < 5):
    print(i)
    print("abc",i)
    i+=1
print("---")

i = 0
while(i<6):
    print(i)
    i+=2
print("---")

list1 = [1,2,3,4,5]
i = 0
while(i < len(list1)):
    print("index",i,"liste elemani",list1[i])
    i +=1
print("---")

print(*range(0,6))
print("---")

print(*range(6))
print("---")

print(*range(0,21,2))
print("---")

print(*range(10,0,-1))
print("---")

result = list(range(3, 31 ,3))
print(result)
print("---")

for i in range(1,6):
    print(i)
print("---")

for i in range(1,6):
    print("*" * i)