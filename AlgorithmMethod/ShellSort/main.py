import random





def InRanNumList(List):
    for i in range(5):
        randomNumber = random.randint(0,100)
        List.append(randomNumber)    
    print("Unsorted: " + str(List))


def InsertionSortInterleaved(List):
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


"""
38, 12, 55, 33, 29, 14, 72, 47, 54

Gap Value 4: 29, 12, 55, 33, 38, 14, 72, 47, 54
Gap Value 3: 33, 12, 14, 38, 29, 54, 72, 47, 55

"""

