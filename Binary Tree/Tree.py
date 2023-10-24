class TreeNode:
    def __init__(self, value, children=[]):
        self.value = value
        self.children = children

    def __str__(self, level=0):
        ret = " " * level + str(self.value) + '\n'
        for child in self.children:
            ret += child.__str__(level+1)
        return ret
    
    def addChild(self, TreeNode):
        self.children.append(TreeNode)

tree = TreeNode('Drinks', [])
hot = TreeNode('Hot', [])
cold = TreeNode('Cold', [])
tree.addChild(hot)
tree.addChild(cold)
print(tree)