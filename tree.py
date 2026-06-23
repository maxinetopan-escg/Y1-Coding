class Tree:
    def __init__(self, root:Node):
        self.root = root

    def AddNode(self, currentNode:Node, newNode:Node):
        if currentNode.value < newNode.value:
            if currentNode.right == None:
                currentNode.right = newNode
            else:
                self.AddNode(self, currentNode.right, newNode)
        else:
            if currentNode.left == None:
                currentNode.left = newNode
            else:
                self.AddNode(self, currentNode.left, newNode)
        

class Node:
    def __init__(self, value:int):
        self.value = value
        self.left = None
        self.right = None

rootNode = Node(50)
tree = Tree(rootNode)

newNode = Node(38)
tree.AddNode(rootNode, newNode)
tree.AddNode(rootNode, Node(70))

print(tree.root.value)
print(tree.root.left.value)
print(tree.root.right.value)