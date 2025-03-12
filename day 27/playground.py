def add(*args):
    print(sum(args))

add(5,6,3,2,1,8,4,5,4,55,46)

def calculate(n,**kwargs):
    print(kwargs)
    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)
calculate(4,add=5, multiply=6)

class Car:
    def __init__(self, **kw):
        # self.make = kw['make']
        # self.model = kw["model"]
        self.make = kw.get("make")
        self.model = kw.get('model')


my_car = Car(make="Ford", model="Explorer")
print(my_car.make, my_car.model)