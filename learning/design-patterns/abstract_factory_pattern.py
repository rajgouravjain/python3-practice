#--------Abstract classes -------
class Shape2DInterface:
    def draw(self):
        pass

class Shape3DInterface:
    def build(self):
        pass

#-------- Concrete classes -------

class Circle(Shape2DInterface):
    def draw(self):
        print("Circle.draw")

class Square(Shape2DInterface):
    def draw(self):
        print("Square.draw")


class Sphere(Shape3DInterface):
    def build(self):
        print("Sphere.build")

class Qube(Shape3DInterface):
    def build(self):
        print("Qube.build")

##----- Abstract factory Interface
class ShapeFactoryInterface:
    def get_shape(self,sides):
        pass

## Factory concrete class
class Shape2DFactory(ShapeFactoryInterface):
    def get_shape(self, sides):
        if sides == 1:
            return Circle()
        if side == 4:
            return  Square()
        assert 0, "bad argument side == " + sides
class Shapre3DFactory(ShapeFactoryInterface):
    def get_shape(self,sides):
        if sides == 1 :
            return Sphere()
        if sides == 12:
            return Qube()
        assert 0, "bad argument side == " + sides


if __name__ == '__main__':
    shape_2d = Shape2DFactory()
    c = shape_2d.get_shape(1)
    c.draw()

    shape_3d = Shapre3DFactory()
    q = shape_3d.get_shape(12)
    q.build()





