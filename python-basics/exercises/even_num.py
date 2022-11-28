l1 = [34,2,1,3,33,100,61,1800]

def even(num):
    if (num % 2 == 0):
        return num
    else:
        raise ValueError

for i in l1:
    try:
        print(even(i))
    except ValueError:
        pass