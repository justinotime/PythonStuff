import random


def InRanNumList(List):
    for i in range(5):
        randomNumber = random.randint(0,100)
        List.append(randomNumber)
    List.sort()
    print(*List, sep = ", ")

def generateKeyNumber(List): 
    key = random.randint(0, len(List)) 
    print(f'{List[key]} indexed at {key}')  

def BinSearch(List, key):

    lengthList = len(List)
    low = 0
    high = lengthList - 1 # Index format

    while low <= high:
        mid = low + (high - low) // 2
        if List[mid] == key:
            return mid
        elif List[mid] < key:
            low = mid + 1
        else:
            high = mid - 1
    


def main():
    randList = []

    InRanNumList(randList)
    userKey = generateKeyNumber(randList)
    result = BinSearch(randList, userKey)

    
    
    


            

if __name__ == "__main__":
    main()