
class Node(object):
    def __init__(self, val):
        self.val = val
        self.next = None

    def prettyPrint(self):
        c = self
        while c:
            print (c.val)
            c = c.next

a = Node('Saniasi Pillai')
a.next = Node('Rajaratnam Pillai')
a.next.next = Node('Ramamurthy')
a.next.next.next = Node('Raja Segaran')
a.next.next.next.next = Node('Thyagaraja Rathnam Pillai')

a.prettyPrint()


