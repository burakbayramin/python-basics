num = input("enter number\t")
power = len(num)
num = int(num)
temp = num
dig = 0
top = 0

while(temp > 0):
    dig = temp % 10
    top += dig ** power
    temp //= 10

if(top == num):
    print("this is armstrong number")
else:
    print("none")