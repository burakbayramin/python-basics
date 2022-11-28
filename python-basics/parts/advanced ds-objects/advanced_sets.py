l = [1, 1, 1, 2, 3, 4, 4, 5]
x = set(l)
print(x)
print("---")

x = set("Hello Darkness My Old Friend")
print(x)

x = {"ABC", "DDD", "ABC",}
print(x)
print("---")

x = {"a", "b", "c", "d"}
x.add("b")
x.add("e")
print(x)
print("---")

y = {"1", "2", "3", "a", "b"}
print(x.difference(y))
print(x.intersection(y))
print("---")

x.discard("c")
print(x)
print("---")

print(x.union(y))
print(x)
x.update(y)
print(x)