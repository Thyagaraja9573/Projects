class Node(object):
    def __init__(self, val):
        self.val = val
        self.right = None
        self.left = None


def fDeepest(n):
    b = bool(False)
    if n != None:
        fDeepest(n.left)
        fDeepest(n.right)
        if b == bool(True):
            return
        print(n.val)
        return b = bool(True)

root = Node('a')
root.left = Node('b')
root.left.left = Node('d')
root.right = Node('c')

c = root
print(fDeepest(c))
