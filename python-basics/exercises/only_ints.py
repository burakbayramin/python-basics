l =  ["345","sadas","324a","14","abc"]

for i in l:
    try:
        i = int(i)
        print(i)
    except ValueError:
        pass