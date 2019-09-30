def intersection(a, b):
    if a == b:
        print(a)
    else:
        a = a.next
        b = b.next
    return a

class Node(object):
    def __init__(self, val):
        self.val = val
        self.next = None

    def prettyPrint(self):
        c = self
        while c:
            print(c.val)
            c = c.next

ptrA = Node(1)
ptrA.next = Node(2)
ptrA.next.next = Node(3)
ptrA.next.next.next = Node(4)
print('*'*40)
print('This is linked list for A nodes')
ptrA.prettyPrint()
ptrB = Node(6)
ptrB.next = ptrA.next.next
print('*'*40)
print('This is the linked list for B nodes')
ptrB.prettyPrint()
#for each object in a, print a.val

print('*'*40)
ptrTmpAroot = ptrA
while ptrTmpAroot:
    print(ptrTmpAroot.val)
    ptrTmpBroot = ptrB
    while ptrTmpBroot:
        print(ptrTmpBroot.val)
        if ptrTmpAroot == ptrTmpBroot:
            print('The intersection is ',ptrTmpAroot.val)
        ptrTmpBroot = ptrTmpBroot.next
    ptrTmpAroot = ptrTmpAroot.next



#c = intersection(a, b)
#c.prettyPrint()
