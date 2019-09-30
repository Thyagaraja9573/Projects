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
#        sCurSubString = lCurStringList[0]
        if fIsPalindrome(sCurSubString):
            print('Current String :', sCurSubString)
            print('Longest Palindrome :',fReverseString(sCurSubString))
            return

    del lCurStringList[:]
    lCurStringList.append(sCurString[1:])
    lCurStringList.append(sCurString[:-1])
    print(lCurStringList)
#    iStrLen = len(sCurString)
#    print(sCurString[0:iStrLen-1])
#    print(s,sCurReverseString)

#    sLongestPalindrome =
    return

#    s = s.lower
#    r = []
#
#    for i in range(len(s)):
#        for j in range(0,i):
#            conc = s[j:i+1]
#
#            if conc == conc[::-1]:
#                r.append(conc)
#
#    return s.index(max(r, key=len)), r
fLongestPalindrome('banana')
fLongestPalindrome('makemeemekam')
fLongestPalindrome('tracecars')
fLongestPalindrome('forsesrof')
fLongestPalindrome('million')
fLongestPalindrome('amanaplanacanalpanama')
fLongestPalindrome('100001')
fLongestPalindrome('racecar')
