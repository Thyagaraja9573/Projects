class Node:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value

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
                floor = root_node.value
                print('Floor changes to', floor)
        else:
            if root_node.value <= ceil:
                ceil = root_node.value
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

print(findCeilingFloor(root, 5, 0, 10))
