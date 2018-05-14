import random

#RANDOM UNIQUE ADDRESS GENERATOR
addressBook = []

print("Enter the kind")
kind = input()
while True:
    if kind.isalpha() == True:
        break
    elif kind == "":
        break
    print("Single Letter Only.")
    kind = input()
print("Enter the amt")
amt = input()
while True:
    if amt.isdecimal() == True:
        break
    print("Must be an integer.")
    amt = input()

def addressGen(kind, amt):
    for i in range(int(amt)):
        global addressBook
        x0 = random.randint(0,9)
        x1 = random.randint(0,9)
        x2 = random.randint(0,9)
        x3 = random.randint(0,9)
        x4 = random.randint(0,9)
        x5 = random.randint(0,9)
        x6 = random.randint(0,9)
        x7 = random.randint(0,9)
        x8 = random.randint(0,9)
        x9 = random.randint(0,9)
        string_p1 = str(x0)+str(x1)+str(x2)+str(x3)
        string_p2 = str(x4)+str(x5)
        string_p3 = str(x6)+str(x7)+str(x8)+str(x9)
        r_address = string_p1 + string_p2 + string_p3
        if kind == "v":
            header = "v"
        else:
            header = "n"
        address = header + string_p1 + "-" + string_p2 + "-" + string_p3
        try:
            addressBook.index(address)
            print("DUPLICATE FOUND")
            i = i-1
            continue
        except ValueError:
            addressBook.append(address)
        
addressGen(kind, amt)

def printAddresses(book):
    for i in range(len(book)):
        print(book[i])

printAddresses(addressBook)
