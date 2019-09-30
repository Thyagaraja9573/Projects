class Node(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        c = self
        answer = ''
        while c:
            answer += str(c.val) if c.val else ''
            c = c.next
            return answer
ptrAB = []

def merge(ptrA, ptrB):
    if ptrA is None:
        ptrAB.append(ptrB.val)
    if ptrB is None:
        ptrAB.append(ptrA.val)

    if (ptrA.val < ptrB.val):
        ptrA.next = merge(ptrA.next, ptrB)
        ptrAB.append(ptrA.val)

    else:
        ptrB.next = merge(ptrB.next, ptrA)
        ptrAB.append(ptrB.val)
    return

a = Node(1, Node(3, Node(5)))
b = Node(2, Node(4, Node(6)))

merge(a, b)
print(ptrAB)
