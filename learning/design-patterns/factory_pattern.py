class ShapeInterface:
    def draw(self):
        pass

class Circle(ShapeInterface):
    def draw(self):
        print("Circle.draw")

class Sqaure(ShapeInterface):
    def draw(self):
        print("Square.draw")


class ShapeFactory():
    def get_shape(self,type):
        if type == 'circle':
            return Circle()
        if type == 'square':
            return Sqaure()

        assert 0, "bad argument " + type

if __name__ == '__main__':

    f = ShapeFactory()\

    c  =  f.get_shape('circle')
    c.draw()

    s = f.get_shape('square')
    s.draw()

    t = f.get_shape('triangle')
    #t.draw()



