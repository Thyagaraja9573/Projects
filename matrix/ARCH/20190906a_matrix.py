m = [['f','a','c','i'],
     ['o','b','q','p'],
     ['a','n','o','b'],
     ['m','a','s','s']]

bDebug = bool(False)
#bDebug = bool(True)
def fSplitString(s):
    return list(s)

def fNestedForL2R(sCurSearchParm):
    for i in range(len(m)):
        curStr = ''
        for j in range(len(m)):
            curStr = curStr + m[i][j]
        if curStr.find(sCurSearchParm) != -1:
            print(curStr)
    return

def fNestedForR2L(sCurSearchParm):
    for i in range(len(m)):
        curStr = ''
        for j in range(len(m)):
            curStr = curStr + m[i][len(m)-j-1]
        if curStr.find(sCurSearchParm) != -1:
            print(curStr)
    return

def fNestedForU2D(sCurSearchParm):
    for j in range(len(m)):
        curStr = ''
        for i in range(len(m)):
            curStr = curStr + m[i][j]
        if curStr.find(sCurSearchParm) != -1:
            print(curStr)
    return

def fNestedForD2U(sCurSearchParm):
    for j in range(len(m)):
        curStr = ''
        for i in range(len(m)):
            curStr = curStr + m[len(m)-i-1][j]
        if curStr.find(sCurSearchParm) != -1:
            print(curStr)
    return


def fFindString(sCurString):
    fNestedForL2R(sCurString)
    fNestedForR2L(sCurString)
    fNestedForU2D(sCurString)
    fNestedForD2U(sCurString)
    return



fFindString('mass')
fFindString('foam')
fFindString('foam')
fFindString('bona')
fFindString('ffff')
