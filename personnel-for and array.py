data = []


def addpersonel():
    x = input("enter the name of the new personel :")
    data.append(x)


for x in range(5):
    addpersonel()
print(data)
