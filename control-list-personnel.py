personnel = []
price = []


def addpersonnel():
    x = input("enter the name of the new personnel :")
    if x in personnel:
        print("personnel already exists")
    else:
        h = input("enter the price hqoq :")
        personnel.append(x)
        price.append(h)

        print(personnel)


def statsper():
    x = input("enter the name of personnel :")
    if x not in personnel:
        print("personnel does not exist")
    else:
        print("personnel stats name : " + x + "price is " + price[personnel.index(x)])


def removepersonnel():
    x = input("enter the name of the remove personnel :")
    if x not in personnel:
        print("personnel does not exist")
    else:
        personnel.remove(x)
        personnel.
        price.remove(personnel.index(x))
    print(personnel)


while True:
    quest = input("enter what you do? remove ,add ,stats and exit : ")
    if quest == "remove":
        removepersonnel()
    elif quest == "add":
        addpersonnel()
    elif quest == "stats":
        statsper()
    elif quest == "exit":
        print("Thank you for using fucking code amirwopi this program barde dari nigger")
        break
    elif quest == "":
        print("please enter a valid input")
    else:
        print("please kos khol bazi dar nayar")
