grid = [[1, 2, 3, 4, 5],
        [6, 7, 8, 9, 10],
        [11,12,13,14,15],
        [16,17,18,19,20]]



def fFindRow(g):
    numrows = len(g)
    return numrows

def fFindCol(g):
    numcols = len(g[0])
    return numcols

def fSpiralPrint(grid):
    iEndRow  = fFindRow(grid)
    iEndCol  = fFindCol(grid)
    iStartRow = 0
    iStartCol = 0

    while(iStartRow < iEndRow and iStartCol < iEndCol):
#        print('going in 1st for loop')
        for i in range(iStartCol, iEndCol):
            print(grid[iStartRow][i])
        iStartRow += 1

#        print('Going in 2nd for loop')
        for i in range(iStartRow, iEndRow):
            print(grid[i][iEndCol - 1])
        iEndCol -= 1

#        print('going in 1st if statement')
        if(iStartRow < iEndRow):
            for i in range(iEndCol-1, iStartCol-1, -1):
                print(grid[iEndRow-1][i])
            iEndRow -= 1

#        print('Going in 2nd if statement')
        if(iStartCol , iEndCol):
            for i in range(iEndRow-1, iStartRow-1, -1):
                print(grid[i][iStartCol])
            iStartCol += 1



fSpiralPrint(grid)
