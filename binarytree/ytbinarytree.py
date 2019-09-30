

class Node:
    def __init__(self, val):
        self.left = None
        self.right = None
        self.value = val

class Tree:
    def __init__(self):
        self.root = None
        self.curCeiling = []
        self.curFloor = []

    def PrintTree(self):
        if(self.root != None):
            self._PrintTree(self.root)

    def _PrintTree(self, node):
        if(node != None):
            self._PrintTree(node.left)
            print(node.value)
            self._PrintTree(node.right)

    def rPrintCeiling(self, rkey):
        if(self.root != None):
            self._rPrintCeiling(self.root,rkey)

    def _rPrintCeiling(self, node, rkey):
        if(node != None):
            if(node.value == rkey):
                self.curCeiling.append(node.value)
                return
            self._rPrintCeiling(node.left,rkey)
            if(node.value > rkey):
                self.curCeiling.append(node.value)
                return
            self._rPrintCeiling(node.right,rkey)

    def rPrintFloor(self, rkey):
        if(self.root != None):
            self._rPrintFloor(self.root,rkey)

    def _rPrintFloor(self, node, rkey):
        if(node != None):
            if(node.value == rkey):
                self.curFloor.append(node.value)
                return
            self._rPrintFloor(node.right,rkey)
            if(node.value < rkey):
                self.curFloor.append(node.value)
                return node
            self._rPrintFloor(node.left,rkey)

    def PrintFloorCeiling(self, node):
        self.curFloor = []
        self.curCeiling = []
        myTree.rPrintFloor(node)
        myTree.rPrintCeiling(node)
        return self.curFloor[:1], self.curCeiling[:1]

    def makeList(self):
        if(self.root != None):
            return self._makeList(self.root)

    def _makeList(self, node, a = []):
        if node != None:
            print('a before left',a)
            self._makeList(node.left, a)
            print('a after left',a)
            a = a + [node.value]
            print('a before right',a)
            self._makeList(node.right, a)
            print('a after right', a)
            return a

#    def _makeList(self, node):
#        a = []
#        x = self._inOrder(node)
#        a = a +[x]
#        print(a)

    def _find(self, val, node):
        if(val == node.value):
            return node
        elif(val < node.value and node.left != None):
            return self._find(val, node.left)
        elif(val > node.value and node.right != None):
            return self._find(val, node.right)

    def add(self, val):
        if(self.root == None):
            self.root = Node(val)
        else:
            self._add(val, self.root)

    def _add(self, val, node):
        if(val < node.value):
            if(node.left != None):
                self._add(val, node.left)
            else:
                node.left = Node(val)
        else:
            if(node.right != None):
                self._add(val, node.right)
            else:
                node.right = Node(val)

    def find(self, val):
        if(self.root != None):
            return self._find(val, self.root)
        else:
            return None

    def _find(self, val, node):
        print('Entering find tree',node.value)
        if(val == node.value):
            print('Found', node.value)
            return node
        elif(val < node.value and node.left != None):
            print('Moving left',node.value)
            return self._find(val, node.left)
            print('Moved left',node.value)
        elif(val > node.value and node.right != None):
            print('Moving right',node.value)
            return self._find(val, node.right)
            print('Moved right',node.value)
        print('Exiting find tree',node.value)



myTree = Tree()
myTree.add(8)
myTree.add(4)
myTree.add(12)
myTree.add(2)
myTree.add(6)
myTree.add(10)
myTree.add(14)
myTree.add(16)
myTree.add(5)
myTree.add(11)
myTree.add(20)
myTree.add(3)


print('Floor and Ceiling is ',myTree.PrintFloorCeiling(a))
#print(myTree.curCeiling)
#print('*'*20)
#myTree.rPrintFloor(15)
#print(myTree.curFloor)

exit()

#myTree.PrintTree()
#print('*'*20)
#if myTree.find(20):
#    print('Found')
#else:
#    print('Not found')
myTree.inOrder()
print('*'*20)
x = myTree.makeList()
print(x)
#if myTree.find(40):
#    print('Found')
#else:
#    print('Not found')
