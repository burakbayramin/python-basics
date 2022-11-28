emotes = ["happy", "angry", "sad"]

def sum(*a):
    sum = 0
    for i in a:
        sum += i
    return sum

def hi(name):
    print("Hello",name)