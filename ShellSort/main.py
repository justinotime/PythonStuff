import random





def InRanNumList(List):
    for i in range(5):
        randomNumber = random.randint(0,100)
        List.append(randomNumber)    
    print("Unsorted: " + str(List))


def InsertionSort(List):
    i = 0
    j = 0
    temp = 0
    sizeList = len(List)
    for i in range(sizeList):
        j = i
        while (j > 0 and List[j] < List[j - 1]):
            temp = List[j]
            List[j] = List[j - 1]
            List[j - 1] = temp
            j -= 1
            
    print("Sorted: " + str(List))
    print(compar)


def main():
    randList = []

    InRanNumList(randList)
    


if __name__ == "__main__":
    main()


# 22 58 92 70 36 15 98 81 90 82

