def hello():
    print("hello")
    print("wassup")
print(type(hello))
hello()
print("---")

def name(nm):
    print("your name ->", nm)
name("frank")
print("---")

def sum(a,b,c):
    print("sum is", a+b+c)
sum(31,32,21)
print("---")

def factorial(num):
    fac = 1
    if(num == 0 or num == 1):
        print("Factorial ->",fac)
    else:
        while(num>=1):
            fac *= num
            num -= 1
        print("Factorial ->",fac)
factorial(5)
print("---")

def summ(a, b, c):
    return a+b+c

def mult(a):
    return a*2

print(mult(summ(12,23,34)))
print("---")

def hi(name = "no name"):
    print("Hi", name)
hi()
hi("frank")
print("---")

def showInfo(name = "no info", surname = "no info", id = "no info"):
    print("Name",name,"Surname",surname,"Id",id)
showInfo()
showInfo("frank","sinatra")
showInfo(id=12234)
print("---")

def summm(*a):
    print(a)
    sum = 0
    for i in a:
        sum += i
    print(sum)
summm(1,2,3,4,5,6,7)
print("---")

a = 5
def fonk():
    b = 10
    global a
    print(a, b)
fonk()
print("---")

if True:
    e = 4
    print(e)
print(e)
print("---")

multi2 = lambda x : x * 2
print(multi2(16))
print("---")

sumnums = lambda x, y, z : x + y + z
print(sumnums(11,23,98))
print("---")

reverse = lambda s : s[::-1]
print(reverse("python"))
print("---")

even = lambda x : x % 2 == 0
print(even(2))
print(even(3))
print("---")