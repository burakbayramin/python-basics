list = [1,2,3,4,5]
for i in list:
    print(i)
print("---")

toplam = 0
for i in list:
    toplam += i
    print(toplam)
print("---")

list1 = [1,23,35425,32,56,74,33,31]
for i in list1:
    if(i % 2 == 0):
        print(i)
print("---")

s = "python"
for i in s:
    print(i)
print("---")

for i in s:
    print(i * 3)
print("---")

list2 = [(1,2,3),(34,54,12),(213,142,12,3)]
for i in list2:
    print(i)
print("---")

list3 = [(12,123),(45,121)]
for (i,j) in list3:
    print("i = {}\tj = {}".format(i,j))
print("---")

for (i,j) in list3:
    print(i * j)
print("---")

dict = {"bir":"merbhaba" ,"iki":2,"uc":"selamlar"}
for i in dict:
    print(i)
print("---")

for i in dict.values():
    print(i)
print("---")

for i,j in dict.items():
    print("key {}\tvalues {}".format(i,j))