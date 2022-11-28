l1  = list(filter(lambda x : x % 2 == 0, [1,2,3,4,5,6,7]))
print(l1)
print("---")

def isPrime(x):
    i = 2
    if(x < 2):
        return False
    elif(x == 2):
        return True
    else:
        while(i < x):
            if(x % i == 0):
                return False
            i += 1
        return True
    
l2 = list(filter(isPrime, range(1,100)))
print(l2)