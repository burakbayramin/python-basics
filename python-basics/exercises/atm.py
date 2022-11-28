print("balance inquiry 1\ndeposit 2\nwithdrawal 3")
balance = 1000

while True:
    op = input("select yout operation\nfor exit press q")
    if(op == "q"):
        print("you went out")
        break
    elif(op == "1"):
        print(balance)
    elif(op == "2"):
        amount = int(input("write the amount you will deposit\n"))
        balance += amount
    elif(op == "3"):
        amount = int(input("write the amount you will withdraw\n"))
        if(amount > balance):
            print("you can't withdraw this amount")
            continue
        else:
            balance -= amount
    else:
        print("invalid operation")