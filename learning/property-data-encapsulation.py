class CC(object):
    def __init__(self,p=1000):
        self.__pocket_money = p
        #self.setx(i)
    def getx(self):
        print("Retreiving attribute pocket_money")
        return self.__pocket_money

    def setx(self, p):
        if int(p) < 10:
            print("setting attibute pocket_money to ", p)
            self.__pocket_money = p

    def delx(self):
        print("Deleting attribute pocket_money")
        del self.__pocket_money
    pocket_money = property(getx, setx, delx, "I'm the 'pocket_money' property.")

y = CC()
print("===========Action Get:: ======= ")
print(y.pocket_money)


print("===========Action Set:: =============")
y.pocket_money = 9

y.pocket_money = 100

print(y.pocket_money)
print("Action Delete :: =============")
del y.pocket_money
#print(y.delx())
