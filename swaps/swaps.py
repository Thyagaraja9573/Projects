def fSwap(str1, str2):
    if(len(str1) != len(str2)):
        return bool(False)
    else:
        print('Strings you gave : ',str1,str2)
        for i in range(len(str1)):
            if(str1[i] != str2[i]):
                sDiff = str2[i:i+2]
                sDiff = sDiff[::-1]
                str2 = str2.replace(str2[i:i+2], sDiff)
                print('Replaced string : ',str1,str2)
                if(str1 == str2):
                    return bool(True)
                else:
                    return bool(False)


print(fSwap('ab', 'ba'))
print(fSwap('aaaabc', 'aaaacb'))
print(fSwap('aaaabc', 'acaaba'))
print(fSwap('aaaab', 'aaaba'))
print(fSwap('agha','ahga'))
print(fSwap('aghaaabca','ahgaaacba'))
