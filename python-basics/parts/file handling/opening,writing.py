file = open("testfile.txt","w")
file.write("lorem ipsum")
file.close()

file = open("testfile.txt","a")
file.write("\tipsum lorem")
file.close()

file = open("testfile.txt","a")
file.write("\nlorem ipsum")
file.close()

file = open("testfile2.txt","w")
file.write("Francesca Hughes\nPatrick Vincent\nRay Hatfield\nWalker Cross\nAyaan Stevens")
file.close()
