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
    return lNewArray


def fShortestString(s,l):
    lSortedArray = fSortArray(l)
    lNewArray = fNewArray(s, lSortedArray)
    print('The number you gave was ',s)
    print('The subarray is ',lNewArray)
    print('The minimal length is ',len(lNewArray))
    return




fShortestString(7,nums1)
nums2 = [2, 3, 1, 2, 4, 1]
fShortestString(6,nums2)
nums1 = [2, 3, 1, 2, 4, 3]
nums1 = [2, 3, 1, 2, 4, 3]
fShortestString(7,nums1)
fShortestString(7,nums1)
fShortestString(7,nums1)
fShortestString(7,nums1)
