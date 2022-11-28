def finddivs(num):
    divs = []

    for i in range(2, num):
        if(num % i == 0):
            divs.append(i)
    return divs
    
print(finddivs(18))