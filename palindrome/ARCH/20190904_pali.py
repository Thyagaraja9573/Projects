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
#            print('Current String :', sCurSubString)
            print('Longest Palindrome :',fReverseString(sCurSubString))
            return

# n-1
    del lCurStringList[:]
    lCurStringList.append(sCurString[1:])
    lCurStringList.append(sCurString[:-1])
#    print(lCurStringList)
    for sCurSubString in lCurStringList:
        if fIsPalindrome(sCurSubString):
#            print('Current String :', sCurSubString)
            print('Longest Palindrome :',fReverseString(sCurSubString))
            return
# n-2
    del lCurStringList[:]
    lCurStringList.append(sCurString[:-2])
    lCurStringList.append(sCurString[1:-1])
    lCurStringList.append(sCurString[2:])
#    print(lCurStringList)
    for sCurSubString in lCurStringList:
        if fIsPalindrome(sCurSubString):
#            print('Current String :', sCurSubString)
            print('Longest Palindrome :',fReverseString(sCurSubString))
            return
#n-3
    del lCurStringList[:]
    lCurStringList.append(sCurString[:-3])
    lCurStringList.append(sCurString[1:-2])
    lCurStringList.append(sCurString[2:-1])
    lCurStringList.append(sCurString[3:])
#    print(lCurStringList)
    for sCurSubString in lCurStringList:
        if fIsPalindrome(sCurSubString):
#            print('Current String :', sCurSubString)
            print('Longest Palindrome :',fReverseString(sCurSubString))
            return
#n-4
    del lCurStringList[:]
    lCurStringList.append(sCurString[:-4])
    lCurStringList.append(sCurString[1:-3])
    lCurStringList.append(sCurString[2:-2])
    lCurStringList.append(sCurString[3:-1])
    lCurStringList.append(sCurString[4:])
#    print(lCurStringList)
    for sCurSubString in lCurStringList:
        if fIsPalindrome(sCurSubString):
#            print('Current String :', sCurSubString)
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
#    print(lCurStringList)
    for sCurSubString in lCurStringList:
        if fIsPalindrome(sCurSubString):
#            print('Current String :', sCurSubString)
            print('Longest Palindrome :',fReverseString(sCurSubString))
            return
#n-6
    del lCurStringList[:]
    lCurStringList.append(sCurString[:-6])
    lCurStringList.append(sCurString[1:-5])
    lCurStringList.append(sCurString[2:-5])
    lCurStringList.append(sCurString[3:-3])
    lCurStringList.append(sCurString[4:-2])
    lCurStringList.append(sCurString[5:-1])
    lCurStringList.append(sCurString[6:])
#    print(lCurStringList)
    for sCurSubString in lCurStringList:
        if fIsPalindrome(sCurSubString):
#            print('Current String :', sCurSubString)
            print('Longest Palindrome :',fReverseString(sCurSubString))
            return
#n-7
    del lCurStringList[:]
    lCurStringList.append(sCurString[:-7])
    lCurStringList.append(sCurString[1:-6])
    lCurStringList.append(sCurString[2:-5])
    lCurStringList.append(sCurString[3:-4])
    lCurStringList.append(sCurString[4:-3])
    lCurStringList.append(sCurString[5:-2])
    lCurStringList.append(sCurString[6:-1])
    lCurStringList.append(sCurString[7:])
#    print(lCurStringList)
    for sCurSubString in lCurStringList:
        if fIsPalindrome(sCurSubString):
#            print('Current String :', sCurSubString)
            print('Longest Palindrome :',fReverseString(sCurSubString))
            return
#n-8
    del lCurStringList[:]
    lCurStringList.append(sCurString[:-8])
    lCurStringList.append(sCurString[1:-7])
    lCurStringList.append(sCurString[2:-6])
    lCurStringList.append(sCurString[3:-5])
    lCurStringList.append(sCurString[4:-4])
    lCurStringList.append(sCurString[5:-3])
    lCurStringList.append(sCurString[6:-2])
    lCurStringList.append(sCurString[7:-1])
    lCurStringList.append(sCurString[8:])
#    print(lCurStringList)
    for sCurSubString in lCurStringList:
        if fIsPalindrome(sCurSubString):
#            print('Current String :', sCurSubString)
            print('Longest Palindrome :',fReverseString(sCurSubString))
            return
#n-9
    del lCurStringList[:]
    lCurStringList.append(sCurString[:-9])
    lCurStringList.append(sCurString[1:-8])
    lCurStringList.append(sCurString[2:-7])
    lCurStringList.append(sCurString[3:-6])
    lCurStringList.append(sCurString[4:-5])
    lCurStringList.append(sCurString[5:-4])
    lCurStringList.append(sCurString[6:-3])
    lCurStringList.append(sCurString[7:-2])
    lCurStringList.append(sCurString[8:-1])
    lCurStringList.append(sCurString[9:])
#    print(lCurStringList)
    for sCurSubString in lCurStringList:
        if fIsPalindrome(sCurSubString):
#            print('Current String :', sCurSubString)
            print('Longest Palindrome :',fReverseString(sCurSubString))
            return
#n-10
    del lCurStringList[:]
    lCurStringList.append(sCurString[:-10])
    lCurStringList.append(sCurString[1:-9])
    lCurStringList.append(sCurString[2:-8])
    lCurStringList.append(sCurString[3:-7])
    lCurStringList.append(sCurString[4:-6])
    lCurStringList.append(sCurString[5:-5])
    lCurStringList.append(sCurString[6:-4])
    lCurStringList.append(sCurString[7:-3])
    lCurStringList.append(sCurString[8:-2])
    lCurStringList.append(sCurString[9:-1])
    lCurStringList.append(sCurString[10:])
#    print(lCurStringList)
    for sCurSubString in lCurStringList:
        if fIsPalindrome(sCurSubString):
#            print('Current String :', sCurSubString)
            print('Longest Palindrome :',fReverseString(sCurSubString))
            return
#n-11
    del lCurStringList[:]
    lCurStringList.append(sCurString[:-11])
    lCurStringList.append(sCurString[1:-10])
    lCurStringList.append(sCurString[2:-9])
    lCurStringList.append(sCurString[3:-8])
    lCurStringList.append(sCurString[4:-7])
    lCurStringList.append(sCurString[5:-6])
    lCurStringList.append(sCurString[6:-5])
    lCurStringList.append(sCurString[7:-4])
    lCurStringList.append(sCurString[8:-3])
    lCurStringList.append(sCurString[9:-2])
    lCurStringList.append(sCurString[10:-1])
    lCurStringList.append(sCurString[11:])
#    print(lCurStringList)
    for sCurSubString in lCurStringList:
        if fIsPalindrome(sCurSubString):
#            print('Current String :', sCurSubString)
            print('Longest Palindrome :',fReverseString(sCurSubString))
            return
#n-12
    del lCurStringList[:]
    lCurStringList.append(sCurString[:-12])
    lCurStringList.append(sCurString[1:-11])
    lCurStringList.append(sCurString[2:-10])
    lCurStringList.append(sCurString[3:-9])
    lCurStringList.append(sCurString[4:-8])
    lCurStringList.append(sCurString[5:-7])
    lCurStringList.append(sCurString[6:-6])
    lCurStringList.append(sCurString[7:-5])
    lCurStringList.append(sCurString[8:-4])
    lCurStringList.append(sCurString[9:-3])
    lCurStringList.append(sCurString[10:-2])
    lCurStringList.append(sCurString[11-1])
    lCurStringList.append(sCurString[12:])
#    print(lCurStringList)
    for sCurSubString in lCurStringList:
        if fIsPalindrome(sCurSubString):
#            print('Current String :', sCurSubString)
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
