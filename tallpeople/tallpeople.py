array = [3,6,3,4,1]


def fWitnesses(heights):
    witnesses = [heights[-1]]
    iCurMaxVal = heights[-1]
    for i in range(len(heights)):
        if(heights[-(i+1)] > iCurMaxVal):
            witnesses.append(heights[-(i+1)])
            iCurMaxVal = heights[-(i+1)]
    return witnesses


def fPrint(witnesses):
    print('People there : ',array)
    print('Number of witnesses : ',len(fWitnesses(array)))
    print('Actual witnesses : ',fWitnesses(array))


fPrint(array)

