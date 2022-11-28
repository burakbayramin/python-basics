leng = int(input("write the fibonacci length"))
a = 0
b = 1
fib = [a,b]
for i in range(leng+1):
    a, b = b, a+b
    fib.append(b)
print(fib)    