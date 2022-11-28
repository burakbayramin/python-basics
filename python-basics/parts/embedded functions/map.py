def double(i):
    return i * 2

l1 = list(map (double, [1,2,3,4,5]))
print(l1)
print("---")

l2 = list(map(lambda x : x ** 2, [1,2,3,4,5]))
print(l2)
print("---")

l3 = [1,2,3,4]
l4 = [7,3,5,8]
l5 = [9,3,6,1,11]

l6 = list(map(lambda x, y : x * y, l3, l4))
print(l6)
l7 = list(map(lambda x, y, z : x * y * z, l3, l4, l5))
print(l7)