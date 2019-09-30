nums1 = [2, 3, 1, 2, 4, 3]

def fSortArray(l):
    lsorted = sorted(l,reverse = True)
    return lsorted

def fNewArray(s,a):
    tot = 0
    lNewArray = []
    for i in a:
        if tot < s:
            lNewArray.append(i)
            tot = tot+i
    return lNewArray


def fShortestString(s,l):
    lSortedArray = fSortArray(l)
    lNewArray = fNewArray(s, lSortedArray)
    print('The number you gave was ',s)
    print('The subarray is ',lNewArray)
    print('The minimal length is ',len(lNewArray))
    return




fShortestString(7,nums1)
