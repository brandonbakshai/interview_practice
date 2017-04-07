import math

def solution(lsts):
    counters = [0 for i in range(5)]

    while sum(counters) < 20:
        (indexOfSmallest, smallest) = whichSmallest(lsts, counters)

        print(smallest)
        counters[indexOfSmallest] = counters[indexOfSmallest] + 1

def whichSmallest(lsts, counters):
    smallest = math.inf
    indexOfSmallest = -1

    for i in range(5):
        if counters[i] < 4 and lsts[i][counters[i]] < smallest:
            smallest = lsts[i][counters[i]]
            indexOfSmallest = i

    return (indexOfSmallest, smallest)


inputList = [[ 10, 20, 30, 40 ],\
[ 15, 25, 35, 45 ],\
[ 27, 29, 37, 48 ],\
[ 32, 33, 39, 50 ],\
[ 16, 18, 22, 28 ]]

solution(inputList)

