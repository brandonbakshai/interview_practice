def sortNearlySorted(inputList):
    # traverse the array
    for i in range(1, len(inputList)):
        # if at any point the elements i and i-1 are out of order, begin switch
        j = i
        while j > 0 and inputList[j] < inputList[j-1]:
            temp = inputList[j]
            inputList[j] = inputList[j-1]
            inputList[j-1] = temp
            j = j - 1


inputList = [1, 4, 5, 2, 3, 7, 8, 6, 10, 9]
sortNearlySorted(inputList)

print("input: ", inputList)
assert inputList == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
