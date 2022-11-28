i=0
while(i < 10):
    if(i == 5):
        break
    print(i)
    i +=1
print("---")

for i in range(0,10):
    if(i == 4):
        break
    print(i)
print("---")

while True:
    print("press q for exit")
    i = input("enter a name\t")
    if(i == "q"):
        print("you just exit")
        break
    print(i)
print("---")

for i in range(11):
    if(i == 3 or i ==5):
        continue
    print(i)
print("---")

i = 0
while(i < 10):
    if(i == 2):
        i += 1
        continue
    print(i)
    i +=1