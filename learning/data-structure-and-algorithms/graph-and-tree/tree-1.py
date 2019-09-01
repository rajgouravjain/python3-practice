import os


class SimpleNodeInTree(object):
    def __init__(self,value=None, children=None ):
        self.children = children or []
        self.value = value


    def __repr__(self,level=0):
        ret= "\t"*level+repr(self.value)+"\n"
        for child in self.children:
            ret += child.__repr__(level+1)
        return ret

if __name__ == '__main__':
    z = SimpleNodeInTree('z')
    y = SimpleNodeInTree('y')
    x = SimpleNodeInTree('x')

    b = SimpleNodeInTree('b',children=[x])
    c = SimpleNodeInTree('c',children=[y,z])

    a = SimpleNodeInTree('a',children=[b,c])



    print(a)

    



