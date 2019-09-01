##--Complex object
class Car(object):
    def __init__(self):
        self.__engine = None
        self.__wheels = list()
        self.__body = None

    def set_wheel(self,wheel):
        self.__wheels.append(wheel)

    def set_body(self,body):
        self.__body = body

    def set_engine(self,engine):
        self.__engine = engine

    def specs(self):
        print("Car specifications are::")
        print("Engine : ", self.__engine.horsepower)
        print("Body : ", self.__body.shape)
        for i in self.__wheels:
            print("Wheel size : ", i.size)



##--- simple objects
class Engine(object):
    horsepower = None

class Wheel(object):
    size = None

class Body(object):
    shape = None


class Director(object):
    def __init__(self):
        self.__builder = None

    def set_builder(self, builder):
        self.__builder = builder

    def get_car(self):
        car = Car()

        body = self.__builder.get_body()
        car.set_body(body)

        engine = self.__builder.get_engine()
        car.set_engine(engine)

        i = 0
        for i in range(4):
            wheel = self.__builder.get_wheel()
            car.set_wheel(wheel)
        return  car


class BuilderInterface:
    def get_wheel(self): pass
    def get_engine(self): pass
    def get_body(self): pass


class JeepBuilder(BuilderInterface):
    def get_wheel(self):
        wheel = Wheel()
        wheel.size = 14
        return wheel


    def get_engine(self):
        engine = Engine()
        engine.horsepower = 1000
        return engine


    def get_body(self):
        body = Body()
        body.shape = "Jeep"
        return body




if  __name__ == '__main__':
    d = Director()

    d.set_builder(JeepBuilder())
    c = d.get_car()

    c.specs()


