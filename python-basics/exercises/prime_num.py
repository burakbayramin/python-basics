def isPrime(x):
    if(x < 2):
        print("Not prime")
    else:
        for i in range(2,x):
            if(x % i == 0):
                return False
            return True
        
while True:
    num = input("enter number")
    if(num == "q"):
        break
    else:
        num = int(num)
        if(isPrime(num)):
            print(num,"prime")
        else:
            print(num,"not prime")