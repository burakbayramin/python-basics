l1 = [1,2,3,4,5]
l2 = [6,7,8,9,10,11]

l3 = list(zip(l1, l2))
print(l3)

l4 = ["A", "B", "C", "D", "E"]
l5 = list(zip(l1, l2, l4))
print(l5)
print("---")

for i, j in zip(l1, l4):
    print(i, j)