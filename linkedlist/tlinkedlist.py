
class Node(object):
    def __init__(self, val):
        self.val = val
        self.next = None

    def prettyPrint(self):
        c = self
        while c:
            print(c.val)
            c = c.next

def fptrIntersection(a, b):
    ptrA = a
    ptrB = b
    ptrCurIntersection = None
    while ptrA:
        if ptrCurIntersection == None:
            ptrB = b
            while ptrB:
                if ptrB == ptrA:
                    ptrCurIntersection = ptrA
                ptrB = ptrB.next
            ptrA = ptrA.next
        else:
            return ptrCurIntersection


a = Node(1)
a.next = Node(2)
a.next.next = Node(3)
a.next.next.next = Node(4)

b = Node(6)
b.next = a.next.next

c = fptrIntersection(a, b)
if c:
    c.prettyPrint()
else:
    print('There is no intersection point')
