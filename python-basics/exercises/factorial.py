num = int(input("enter number\t"))
if(num == 1 or num ==0):
    print("factorial of this num",num)
elif(num < 0):
    print("this number has no factorial")
else:
    fac = 1
    for i in range(2, num+1):
        fac *= i
    print(fac)