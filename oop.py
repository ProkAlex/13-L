

class Car:
    color = 'red'
    driver = True

    def bipbip(self):
        print("Бип бип")
'''
lada = Car()
bmw = Car()
lada.color = "black"
print(lada.color)
print(bmw.color)
lada.bipbip()
print(lada.__dir__())
print('hello world'.__dir__())
print(lada)
'''
#
'''
lada = Car()
print(lada.color)
lada.color = 'black'
print(lada.color)

print(lada.__dict__)
bmw = Car()
print(bmw.__dict__)
del lada.color
print(lada.__dict__)
print(lada.color)
'''
class Bio:
    mass = 10
    color = 'black'

class Human(Bio):
    head = 1
    name = 'Ivan'

    def hi(self):
        print(f"My name is {self.name}")


b1 = Bio()

adam = Human()
chelik1 = Human()
chelik2 = Human()
chelik2.name = 'Fedor'
chelik1.hi()
chelik2.hi()
chelik2.hends = 2
chelik1.legs = 2
print(chelik1.__dict__)
print(chelik2.__dict__)

class Car():
    def __init__(self, color, driver, speed):
        self.color = color
        self.driver = driver
        self.__speed = speed

    def __del__(self):
        print("Delete")

    def show_speed(self):
        return self.__speed

    def set_speed(self, x):
        self.__speed = x


bmw = Car("balck", True, 100)
lada = Car("white", False, 100)
# print(bmw.__speed)
bmw.set_speed(200)
print(bmw.show_speed())

 