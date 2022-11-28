operations = ["addition", "multiplication"]

def sum(*a):
    sum = 0
    for i in a:
        sum += i
    return sum

def mult(*a):
    sum = 1
    for i in a:
        sum *= i
    return sum
