a = 1 < 2 # true
b = "a" == "a" # true
print(type(a), type(b))
print(a and b)
print("---")

b = "a" == "b" # false
print(a and b) 
print("---")

b = "a" == " a " # false
print(a and b)
print(a or b)
print("---")

b = "a" == "a" # true
c = 23 < 12 # false
print((a and b) or c)
print((a and b) and c)
print("---")

print(not 2 == 2)
print(not "a" == "b")