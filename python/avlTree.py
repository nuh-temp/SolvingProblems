

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.level = 0


class AvlTree:
    def __init__(self, nodes=[]):
        self.root = None
        self.maxLevel = 0

        for n in nodes:
            self.insert(n)

    def avlRotType(self, value, parent, child):
        # Returns:     1 insertion on left tree of left child
        #              2 insertion on right subtree of left child
        #              3 insertion on left subtree of right child
        #              4 insertion on right subtree of right child
        #              0 if value == child, i.e. child is leaf node

        if (value < parent):
            # insert to the left
            if (value < child):
                return 1
            elif (value > child):
                return 2
            else:
                return 0
        else:
            # insert to the right
            if (value < child):
                return 3
            elif (value > child):
                return 4
            else:
                return 0

    def setLevel(self, node):
        leftLevel = -1
        rightLevel = -1

        if (node.left):
            leftLevel = node.left.level
        if (node.right):
            rightLevel = node.right.level

        if (leftLevel > rightLevel):
            node.level = leftLevel + 1
        else:
            node.level = rightLevel + 1

        return node.level

    def __insert(self, node, value):
        rotType = 0
        leftLevel = -1
        rightLevel = -1

        if (node is None):
            return Node(value)

        if node.left:
            leftLevel = node.left.level

        if node.right:
            rightLevel = node.right.level

        # print "compare {0} to {1}".format(value, node.value)
        if (value < node.value):
            node.left = self.__insert(node.left, value)
            leftLevel = node.left.level
            rotType = self.avlRotType(value, node.value, node.left.value)
        elif (value > node.value):
            node.right = self.__insert(node.right, value)
            rightLevel = node.right.level
            rotType = self.avlRotType(value, node.value, node.right.value)
        else:
            raise Exception('EEXISTS', value)

        # print "value: {0}, rotType: {1}, lLev: {2}, rLev: {3}".format(value, rotType, leftLevel, rightLevel)
        delta = leftLevel - rightLevel
        if (delta >= 2 or delta <= -2):
            # print "######## AVL {2} imbalance : {0} AVL type: {1}, node: {3}".format(delta, rotType, value, node.value)
            node = self.rotate(rotType, node)

        self.setLevel(node)
        return node

    def rotate(self, rotType, node):
        if rotType == 1:
            return self.__rotateRight(node)
        elif rotType == 2:
            return self.__rotateLeftRight(node)
        elif rotType == 3:
            return self.__rotateRightLeft(node)
        elif rotType == 4:
            return self.__rotateLeft(node)
        else:
            return node

    def insert(self, value):
        # print "insert:", value
        self.root = self.__insert(self.root, value)

    def __rotateLeft(self, top):
        # print " <<< Rotate Left"
        pivot = top.right

        top.right = pivot.left
        self.setLevel(top)

        pivot.left = top
        self.setLevel(pivot)

        return pivot

    def __rotateLeftRight(self, top):
        # to right on top.left as root
        # phase 1
        root = top.left
        pivot = root.right

        root.right = pivot.left

        pivot.left = root
        self.setLevel(root)

        # phase 2
        root = top
        root.left = pivot.right
        self.setLevel(top)

        pivot.right = root
        self.setLevel(pivot)

        return pivot

    def __rotateRightLeft(self, top):
        # phase 1
        root = top.right
        pivot = root.left

        root.left = pivot.right

        pivot.right = root
        self.setLevel(root)

        # phase 2
        root = top
        root.right = pivot.left
        self.setLevel(top)

        pivot.left = root
        self.setLevel(pivot)

        return pivot

    def __rotateRight(self, top):
        # print " >>> Rotate Right"
        pivot = top.left

        top.left = pivot.right
        self.setLevel(top)

        pivot.right = top
        self.setLevel(pivot)

        return pivot

    def search(self, value):
        pass

    def remove(self, value):
        pass

    def __printNodes(self, node, level):
        maxLevel = self.root.level
        if (level > maxLevel):
            return

        if (level not in self.tree):
            self.tree[level] = []
        elif (len(self.tree[level]) >= 2 ** level):
            return

        if (node is None):
            self.tree[level].append('-')
            for n in xrange(level, maxLevel):
                for key in range(2):
                    self.__printNodes(None, n + 1)
            return

        self.tree[level].append("{0}({1})".format(node.value, node.level))

        # print ' ' * (maxLevel - level), "{0}({1})".format(node.data, level)
        self.__printNodes(node.left, level + 1)
        self.__printNodes(node.right, level + 1)

    def printTree(self):
        self.tree = {}

        self.__printNodes(self.root, 0)
        # print self.tree
        print '-' * 60
        out = ''
        maxLen = len(self.tree[self.tree.keys()[-1]]) * (1 + 2)
        maxLevel = self.root.level

        for level in self.tree:
            levelLen = len(self.tree[level]) * (1 + 1)
            intend = ' ' * ((maxLen - levelLen) / 2)
            if (level == 0):
                out += intend + " {0}".format(self.tree[level][0])
            else:
                line1 = ''
                line2 = (" " * ((maxLevel - level + 1))).join(self.tree[level])
                out += intend + line1 + "\n"
                out += intend + line2
            out += "\n"

        print out

values = [
    [14, 17, 23, 19, 50, 72, 54, 76, 67, 9, 12],
    [50, 17, 72, 12, 23, 54, 76, 9, 14, 19, 67],
    [35, 23, 12, 15, 20, 16],
    [13, 15, 17],
    [15, 13, 14],
    [13, 15, 14]
]


def prTree(node):
    if (node is None):
        return

    print "value:", node.value
    prTree(node.left)
    prTree(node.right)

for vals in values:

    print '=' * 60, "\n", vals
    tree = AvlTree()
    for n in vals:
        tree.insert(n)
        # tree.printTree()

    # prTree(tree.root)

    tree.printTree()
