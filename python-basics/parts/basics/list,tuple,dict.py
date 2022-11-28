print(1,2,3,45,6,sep="#")
print("---")

print(*"python")
print("---")


a = 5
print(type(a))
print("---")

print(*"python",sep="-")
print(*"ython",sep="\n",)
print("---")

a = [1,2,3,4,5]
print(len(a))
print(type(a))
print("---")

l = list()
print(l)
print("---")

s = "merhaba"
liste2 = list(s)
print(liste2)
print("---")

liste3 = [23,34543,534,634,342,23434]
print(liste3[4])
print(liste3[-1])
print(liste3[3:])
print(liste3[:2])
print(liste3[::2])
print(liste3[::-1])
print("---")

l1 = [2,3,6,8]
l2 = [1,2,4,7]
l3 = l1 + l2 
print(l3)
print(l1 * 3)
print("---")

l4 = [1,2,3,4,5]
l4[2] = 15
print(l4)
l4[:2] = [56,66]
print(l4)
print("---")

l5 = [1,2,3]
l5.append(4)
print(l5)
l5.append("python")
print(l5)
l5.pop()
print(l5)
l5.pop(1)
print(l5)
print("---")

l6 = [34,11,23,6346,732,13216,34213,52]
l6.sort()
print(l6)
l6.sort(reverse=True)
print(l6)
print("---")

mdl = [[1,3,4,5],[12,45,564],[456,56756]]
print(mdl[2][1])
print("---")

l7 = [23,123,141,]
l7 += "python"
print(l7)
print("---")

tup = (12312,2346,45546,423)
print(type(tup))
print(tup[1])
print(tup[::-1])
print("---")

tup1 = (1,1,1,1,1,2,2,3,4)
print(tup1.count(1))
print(tup1.count(3))
print(tup1.count(10))
print("---")

tup2 = ("aa","bb","cc","dd")
print(tup2.index("aa"))
print(tup2.index("cc"))
print("---")

dict1 = {"bir":1,"iki":2,"uc":"merhaba"}
print(type(dict1))
print(dict1["bir"])
print(dict1["uc"])
dict1["dort"] = "selam"
print(dict1)
dict1["bir"] = 10
print(dict1)
dict1["bir"] += 1
print(dict1)
print("---")

dicta ={"bir":[1,23,43,54],"iki":[[12,12312,3],[123,12312],[213,312]]}
print(dicta)
print(dicta["bir"])
print(dicta["iki"][1][1])