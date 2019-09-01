import os

class bst(object):
    def __init__(self, name= None, value=None):
        self.value = value
        self.left = None
        self.right = None
        self.name = name

    def insert(self, name, value):
        if self.value >= value :
            if not self.left :
                self.left = bst(name,value)
            else:
                self.left.insert(name, value)
        else:
            if not self.right :
                self.right = bst(name, value)

            else:
                self.right.insert(name, value)

    def display(self,level=0):
        ret = "hello"
        if ( self.right is not None ):
            sr = self.right.display(level+1)
        else :
            sr = "None"

        if ( self.left is not None ) :
            sl =  self.left.display(level+1)
        else :
            sl = "None"

        if ( self is not None )    :
            ret = self.name + "  =>"
            #self.left.display(level+1))
            ret += "\n" + "\t" * (level+1) + "[ left:" + sl + ",\n" + "\t" * (2*level +1) + "  right:" +  sr + " ] "
        return ret

if __name__ == '__main__':
    a = bst(name="a",value=100)
    #b = bst(50)
    #c = bst(110)
    #d = bst(40)

    a.insert("b",50)
    a.insert("c",110)
    a.insert("d",40)
    a.insert('z',300)

    print(a.display())
