import random


def InRanNumList():
    List = []
    for i in range(10):
        randomNumber = random.randint(0,100)
        List.append(randomNumber)
    List.sort()
    
    return List, randomNumber

    # print(*List, sep = ", ")

def generateKeyNumber():
    List, randomNumber = InRanNumList() 
    key = random.randint(0, len(List)) 
    print(f'{List[key]} indexed at {key}')  
    return key

def BinSearch():
    lengthList = len(List)
    middle = (lengthList / 2) - 1
    middle = int(middle)
    high = lengthList - 1

    # if (key == middle):
    #     return


def main():
    
    randList = []
    InRanNumList()
    generateKeyNumber()
    # BinSearch(randList)
    

    # print(f'{randList[int(middle)]} indexed at {middle}') 
    


            

if __name__ == "__main__":
    main()