#TAKES A LIST OF CANIDATES AND ASSIGNS THEM CANDIDATE ADDRESSES

#10 randomly generated n-addresses
addressBook = ['n8999-84-5143',
               'n4789-95-6433',
               'n6670-60-6872',
               'n5103-76-9712',
               'n3264-37-9449',
               'n8488-55-1834',
               'n6660-21-4621',
               'n7162-43-6445',
               'n3825-76-7862',
               'n5963-30-8919']

v_address = "v5962-30-7599"

def convert(n_address):
    c_address = "vn" + str(v_address[1:]) + "." + str(n_address[1:])
    return c_address
    
def assessPool(book):
    candidatePool = []
    for i in range(len(book)):
        n_address = book[i]
        print("Does " + n_address + " want to be a candidate?")
        become = input()
        while True:
            if become == "0":
                break
            if become == "1":
                break
            print("Must be binary. 0 or 1.")
            become = input()
        if become == "0":
            continue
        elif become == "1":
            candidate = convert(n_address)
            candidatePool.append(candidate)
    return candidatePool

candidates = assessPool(addressBook)

def printPool(pool):
    print("HERE ARE THE CANDIDATES:")
    for i in range(len(pool)):
        print(pool[i])

printPool(candidates)

            
