l1 = ["A", "B", "C", "D", "E"]

print(list(enumerate(l1)))
print("---")

for i, j in enumerate(l1):
    print(i, j)
print("---")

for i, j in enumerate(l1):
    if(i % 2 == 0):
        print(j)
        