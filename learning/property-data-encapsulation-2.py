class CC(object):
    def __init__(self,v=1000):
        self.__value = v
        #self.setx(i)
    @property
    def name(self):
        print("Retreiving attribute name")
        return self.__value
    @name.setter
    def name(self, value):
        print("setting attibute name value to ", value)
        if int(value) < 10:
            self.__value = value
    @name.deleter
    def name(self):
        print("Deleting attribute name")
        del self.__value


y = CC()
print("============Action Get:: =========",y.name)
y.name = 9
y.__value = 50
print("Object attributes",y.__value)
print("Object property",y.name)
print("Object attributes are stored in dictionary::",y.__dict__)
print("Action Set:: =============")
print(y.name)


print("Action Delete :: =============")
del y.name
#print(y.delx())
