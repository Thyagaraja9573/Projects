def fReverseString(sCurString):
    return sCurString[::-1]
def fIsPalindrome(sCurString):
    if sCurString == fReverseString(sCurString):
        return bool(True)
    return bool(False)
def fLongestPalindrome(s):
    sCurString = s
    lCurStringList = []
    lCurStringList.append(sCurString)
#    sCurReverseString = fReverseString(lCurStringList[0])
#    if sCurString == sCurReverseString:
    for sCurSubString in lCurStringList:
        if fIsPalindrome(sCurSubString):
            print('Current String :', sCurSubString)
            print('Longest Palindrome :',fReverseString(sCurSubString))
            return

# n-1
    del lCurStringList[:]
    lCurStringList.append(sCurString[1:])
    lCurStringList.append(sCurString[:-1])
    print(lCurStringList)
    for sCurSubString in lCurStringList:
        if fIsPalindrome(sCurSubString):
            print('Current String :', sCurSubString)
            print('Longest Palindrome :',fReverseString(sCurSubString))
            return
# n-2
    del lCurStringList[:]
    lCurStringList.append(sCurString[:-2])
    lCurStringList.append(sCurString[1:-1])
    lCurStringList.append(sCurString[2:])
    print(lCurStringList)
    for sCurSubString in lCurStringList:
        if fIsPalindrome(sCurSubString):
            print('Current String :', sCurSubString)
            print('Longest Palindrome :',fReverseString(sCurSubString))
            return
#n-3
    del lCurStringList[:]
    lCurStringList.append(sCurString[:-3])
    lCurStringList.append(sCurString[1:-2])
    lCurStringList.append(sCurString[2:-1])
    lCurStringList.append(sCurString[3:])
    print(lCurStringList)
    for sCurSubString in lCurStringList:
        if fIsPalindrome(sCurSubString):
            print('Current String :', sCurSubString)
            print('Longest Palindrome :',fReverseString(sCurSubString))
            return
#n-4
    del lCurStringList[:]
    lCurStringList.append(sCurString[:-4])
    lCurStringList.append(sCurString[1:-3])
    lCurStringList.append(sCurString[2:-2])
    lCurStringList.append(sCurString[3:-1])
    lCurStringList.append(sCurString[4:])
    print(lCurStringList)
    for sCurSubString in lCurStringList:
        if fIsPalindrome(sCurSubString):
            print('Current String :', sCurSubString)
            print('Longest Palindrome :',fReverseString(sCurSubString))
            return
#n-5
    del lCurStringList[:]
    lCurStringList.append(sCurString[:-5])
    lCurStringList.append(sCurString[1:-4])
    lCurStringList.append(sCurString[2:-3])
    lCurStringList.append(sCurString[3:-2])
    lCurStringList.append(sCurString[4:-1])
    lCurStringList.append(sCurString[5:])
    print(lCurStringList)
    for sCurSubString in lCurStringList:
        if fIsPalindrome(sCurSubString):
            print('Current String :', sCurSubString)
            print('Longest Palindrome :',fReverseString(sCurSubString))
            return
    return
fLongestPalindrome('makemeemekam')
fLongestPalindrome('tracecars')
fLongestPalindrome('forsesrof')
fLongestPalindrome('million')
fLongestPalindrome('amanaplanacanalpanama')
fLongestPalindrome('100001')
fLongestPalindrome('racecar')
fLongestPalindrome('ace')
fLongestPalindrome('bace')
fLongestPalindrome('face')
fLongestPalindrome('faceca')
fLongestPalindrome('b99129b')
fLongestPalindrome('aa')
fLongestPalindrome('abcdefgaazyxyw')
