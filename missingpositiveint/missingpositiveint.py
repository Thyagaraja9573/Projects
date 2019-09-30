array = [-7,-6,-4,-3,-1,0,1,2,4,7]

def fSmallestPositiveInt(a):
    posInt = max(a)
    for i in a:
        if i > 0 and i-1 > 0 and i-1 < posInt:
            if not i-1 in a:
                posInt = i-1
    return posInt


print(fSmallestPositiveInt(array))

