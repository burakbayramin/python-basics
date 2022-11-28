try:
    a = int("abc123")
    print("program runs")
except:
    print("error")
print("program ends")
print("---")

try:
    a = int("123")
    print("program runs")
except:
    print("error")
print("program ends")
print("---")

try:
    a = int("abc123")
    print("program runs")
except ValueError:
    print("error")
print("program ends")
print("---")

try:
    a = int(input("first number"))
    b = int(input("second number"))
    print(a/b)
except ValueError:
    print("enter right type(integer)")
except ZeroDivisionError:
    print("number cant divide 0")
print("---")

try:
    a = int(input("enter number"))
    b = int(input("enter number"))
    print(a/b)
except ValueError:
    print("enter right type(integer)")
except ZeroDivisionError:
    print("number cant divide 0")
finally:
    print("program ends")
print("---")

def reverse(s):
    if(type(s) != str):
        raise ValueError("Please enter string")
    else:
        return s[::-1]

print(reverse("abc"))

try:
    print(reverse(123))
except ValueError:
    print("Value error")
