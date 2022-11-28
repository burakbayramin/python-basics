print('''
    select your operation
    op 1 -> +
    op 2 -> -
    op 3 -> *
    op 4 -> /
      ''')

a = int(input("enter first number\t"))
b = int(input("enter second number\t"))
c = int(input("enter operation\t"))

if(c == 1):
    print("{}+{}={}".format(a,b,a+b))
elif(c == 2):
    print("{}-{}={}".format(a,b,a-b))
elif(c == 2):
    print("{}*{}={}".format(a,b,a*b))
elif(c == 2):
    print("{}/{}={}".format(a,b,a/b))
else:
    print("invalid operation")