from functools import reduce

def sum(x, y):
    return x + y

print(reduce(sum, [12, 18, 20, 10]))
print("---")

print(reduce(lambda x, y : x * y, [1,2,3,4,5]))
print("---")

