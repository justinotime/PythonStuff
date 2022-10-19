import random


def InRanNumList(List):
    for i in range(5):
        randomNumber = random.randint(0,100)
        List.append(randomNumber)    
    print(List)
    

def SelectionSort(List, size):
    for i in range(size):
        indexSmallest = i
        for j in range(i + 1, size):
            if (List[j] < List[indexSmallest]):
                indexSmallest = j
        temp = List[i]
        List[i] = List[indexSmallest]
        List[indexSmallest] = temp

    print(List)
    


def main():
    randList = []
    InRanNumList(randList)

    size = len(randList)
    SelectionSort(randList, size)

if __name__ == "__main__":
    main()