class Node(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        c = self
        answer = ""
        while c:
            answer += str(c.val) if c.val else ""
            c = c.next
        return answer

def merge(a, b):
    ptrA = a
    ptrB = b
    temp = None
    if not ptrA:
        return ptrB
    if not ptrB:
        return ptrA
    if ptrA and ptrB:
        if ptrA.val <= ptrB.val:
            temp = ptrA
            ptrA = temp.next
        else:
            temp = ptrB
            ptrB = temp.next
        head = temp

    while ptrA and ptrB:
        if ptrA.val <= ptrB.val:
            temp.next = ptrA
            temp = ptrA
            ptrA = temp.next
        else:
            temp.next = ptrB
            temp = ptrB
            ptrB = temp.next

    if not ptrA:
        temp.next = ptrB
    if not ptrB:
        temp.next = ptrA
    return head





a = Node(1, Node(3, Node(5)))
b = Node(2, Node(4, Node(6)))
print(merge(a, b))
