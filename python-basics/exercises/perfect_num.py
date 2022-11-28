num = int(input("enter number\t"))
sum = 0
i = 1
while(num > i):
    if(num % i == 0):
        sum += i
    i += 1
if(sum == num):
    print("perfect number")
else:
    print("nope")
