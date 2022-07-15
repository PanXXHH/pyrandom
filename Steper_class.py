from TreeNode_class import TreeNode
from multipledispatch import dispatch


class Steper(object):
    """docstring for Steper"""
    __currenttree: TreeNode = TreeNode()

    def __init__(self, length: int = 0):
        for i in range(length):
            self.__currenttree.addChildNode(TreeNode())

    @dispatch(int)
    def into(self, index: int):
        nodelen = self.__currenttree.length()
        if index >= nodelen:
            for i in range(index - nodelen + 1):
                self.__currenttree.addChildNode(TreeNode())
        self.__currenttree = self.__currenttree.returnChildNode(index)

    @dispatch(str)
    def into(self, path: str):
        for i in path.split("/"):
            if i:
                # into
                self.into(int(i))
            else:
                while self.__currenttree.parent:
                    self.__currenttree = self.__currenttree.parent

    def length(self):
        return self.__currenttree.length()

    def full(self, target_length: int):
        inf_length = len(self.__currenttree.childs)
        if inf_length >= target_length:
            return
        for i in range(target_length - inf_length):
            self.__currenttree.addChildNode(TreeNode())

    def fullAndRemove(self, target_length: int):
        inf_length = len(self.__currenttree.childs)
        if inf_length >= target_length:
            del self.__currenttree.childs[target_length:]
            return
        for i in range(target_length - inf_length):
            self.__currenttree.addChildNode(TreeNode())

    def set(self, length: int):
        self.__currenttree.clearChilds()
        for i in range(length):
            self.__currenttree.addChildNode(TreeNode())

    def back(self):
        if not self.__currenttree.parent:
            return

        self.__currenttree = self.__currenttree.parent

    def getCurrentPath(self):
        _temp_tree = self.__currenttree
        path_list = []
        while _temp_tree.parent:
            path_list.append(str(_temp_tree.getIndex()))
            _temp_tree = _temp_tree.parent
        path_list.reverse()
        return "/"+"/".join(path_list)

    def __dict__(self) -> dict:
        _temp_tree = self.__currenttree
        while _temp_tree.parent:
            _temp_tree = _temp_tree.parent

        return {'name':_temp_tree.name,'childs':self.__todict(_temp_tree)}

    def __todict(self, node: 'TreeNode') -> dict:
        # 核心变量 node['childs']

        # (-1) 嵌套封尾语句
        if not node.childs:
            return {}

        # (-2) 进入消减语句
        # 模型：{X: {'name': '', 'childs': {0: {'name': '', 'childs': {}}}}}
        childs_dict = {i: {'name': child.name, 'childs': self.__todict(child)} for i, child in enumerate(node.childs)}
        return childs_dict

    def setName(self, name):
        self.__currenttree.name = name
    
    def restep(self):
        while self.__currenttree.parent:
            self.__currenttree = self.__currenttree.parent