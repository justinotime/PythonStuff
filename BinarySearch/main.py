import random


def InRanNumList(List):
    for i in range(10):
        randomNumber = random.randint(0,100)
        List.append(randomNumber)
    
    List.sort()
    print(*List, sep = ", ")

def generateKeyNumber(List):
    key = random.randint(0, len(List)) 
    print(f'{List[key]} indexed at {key}')  
    return key

def BinSearch(List):
    lengthList = len(List)
    middle = (lengthList / 2) - 1
    middle = int(middle)
    high = lengthList - 1

    if (key == middle):
        return


def main():
    
    randList = []
    InRanNumList(randList)
    generateKeyNumber(randList)
    BinSearch(randList)
    

    # print(f'{randList[int(middle)]} indexed at {middle}') 
    


            

if __name__ == "__main__":
    main()