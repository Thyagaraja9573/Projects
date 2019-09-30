m = [['f','a','c','i'],['o','b','q','p'],['a','n','o','b'],['m','a','s','s']]



def fSplitString(s):
    return list(s)



def fTraverseMatrix(m,sLi,i,sLen):
    for j in range(sLen):
        if m[i][j] == sLi:
            return bool(True)
    return bool(False)


def fFindString(sCurString):
    sList = fSplitString(sCurString)
#    print(sList[:4])
    for i in range(len(sList)):
        fTraverseMatrix(m, sList[:i], i, len(sList))
        print(sList[:i+1])
    return



fFindString('foam')
fFindString('mass')
fFindString('foam')
fFindString('bona')
fFindString('ffff')
