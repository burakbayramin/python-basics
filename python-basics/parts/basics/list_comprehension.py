lst1 = [1,2,3,4,5]
lst2 = []
for i in lst1:
    lst2.append(i)
print(lst2)
print("---")

lst3 = [i for i in lst1]
print(lst3)
print("---")

lst4 = [i * 3 for i in lst1]
print(lst4)
print("---")

lst5 = [(1,2),(4,5),(6,3)]
lst6 = [i*j for i,j in lst5]
print(lst6)
print("---")

a = "python"
lst7 = [i * 3 for i in a]
print(lst7)
print("---")

lst8 = [[1,2,3,4],[12,3,245,56,1],[67,2,32]]
list1 = []
for i in lst8:
    for j in i:
        list1.append(j)
print(list1)
print("---")

list2 = [j for i in lst8 for j in i]
print(list2)