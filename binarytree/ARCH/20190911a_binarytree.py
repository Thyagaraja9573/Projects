class Node:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value
    def printMin(self):
        c = self
        while c:
            print(c.value)
            if c.left == None:
                print('The min is ',c.value)
            c = c.left

    def printMax(self):
        c = self
        while c:
            print(c.value)
            if c.right == None:
                print('The max is',c.value)
            c = c.right

    def findLeft(self, value):
        c = self
        while c:
            print(c.value)
            if c.value == value:
                print('Value is found',c.value)
            c = c.left

    def findRight(self, value):
        c = self
        while c:
            print(c.value)
            if c.value == value:
                print('Value is found',c.value)
            c = c.right


    def findInTree(self, val, node):
        print('Entering find tree')
        if(val == node.value):
            print('*'*20)
            print('Value found',node.value)
#            return node
        elif(val < node.value and node.left != None):
            print('Moving Left')
            self.findInTree(val, node.left)
            print('Finished moving left')
        elif(val > node.value and node.right != None):
            print('Moving right')
            self.findInTree(val, node.right)
            print('Finished moving right')
        print('Exiting find tree')

#def fListOfTree(root):
#    valList = []
#    if root:
#        valList.append(root.value)
#        print(root.value)
#        fListOfTree(root.left)
#        fListOfTree(root.right)
#    print(valList)
#    return valList

def findCeilingFloor(root_node, k, floor, ceil):

    if root_node:
        print(root_node.value)
        if root_node.value <= k:
            if floor <= root_node.value:
                floor = staticFloor
                print('Floor changes to', floor)
        else:
            de
            if root_node.value <= ceil:
                ceil = staticCeil
                print('Ceil changes to', ceil)
        findCeilingFloor(root_node.left, int(k),floor, ceil)
        findCeilingFloor(root_node.right, int(k),floor, ceil)

#    print(valList)
#    for i in valList:
#        if valList[:i+1] <= k:
#            if floor <= valList[:i+1]:
#                floor = valList[:i+1]
#        if valList[:i+1] >= k:
#            if ceil >= valList[:i+1]:
#                ceil = valList[:i+1]

    return floor, ceil





root = Node(8)
root.left = Node(4)
root.right = Node(12)

root.left.left = Node(2)
root.left.right = Node(6)

root.right.left = Node(10)
root.right.right = Node(14)

c = root

c.printMin()
print('*'*20)
c.printMax()
#print(findCeilingFloor(root, 5, 0, 10))
print('*'*20)
#c.findCurVal(4)
ptrNodeFound = c.findInTree(10, c)
#print(c.value)
#if ptrNodeFound:
#    print('node found',ptrNodeFound.value)
#else:
#    print('The value was not found')
