
class TreeNode(object):
    def __init__(self, name: 'str' = ""):
        self.name = name
        self.parent: TreeNode = None
        self.childs: list = []

    def addChildNode(self, node: 'TreeNode') -> 'None':
        node.parent = self
        self.childs.append(node)

    def addReturnChildNode(self, node: 'TreeNode') -> 'TreeNode':
        node.parent = self
        self.childs.append(node)
        return self.childs[-1]

    def returnChildNode(self, index: 'int') -> 'TreeNode':
        return self.childs[index]

    def length(self) -> 'int':
        return len(self.childs)

    def getIndex(self) -> 'int':
        return self.parent.childs.index(self)

    def clearChilds(self):
        self.childs = list()