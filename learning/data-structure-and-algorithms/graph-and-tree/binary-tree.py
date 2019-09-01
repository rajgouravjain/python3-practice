import os

class NodeInBinaryTree(object):
    def __init__(self, value=None):
        self.value = value
        self.left = None
        self.right = None
    def insert_left(self, new_node_value):
        if not self.left :

            self.left = NodeInBinaryTree(new_node_value)
        else :
            self.left.insert_left(new_node_value)
    def __repr__(self):
        ret = self.value + "\n"
        ret  += repr(self.left)
        return  ret

    #__repr__(self,level=0):

if __name__ == '__main__':
    a = NodeInBinaryTree(value='a')
    #b = NodeInBinaryTree('b')
    #c = NodeInBinaryTree('c')

    #x = NodeInBinaryTree('x')
    #y = NodeInBinaryTree('y')
    #z = NodeInBinaryTree('z')

    a.insert_left("b")
    a.insert_left('c')
    a.insert_left('d')
    a.insert_left('e')
    print(a)


