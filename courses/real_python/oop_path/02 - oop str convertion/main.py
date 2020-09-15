'''

Pythonic Way to convert an object to string

    __str__ vs __repr__


    __str__: params on string
    ( 
        an easy to read presentation for your class 
        for human consumption
    )
    
    
    __repr__: is an self unambiguous representation  from the object
    ( 
        Internal use, for easy debug 
        valid python to recreate the same object  
        more meaning for developers 
    )

    At least add a __repr__ to your classes :) 

'''

class Car:
    def __init__(self, color, mileage):
        self.color = color
        self.mileage = mileage


# bad way
my_car = Car('red',12345)
print(my_car) # this print an object

my_car

print(my_car.color, my_car.mileage)


class Car_with_dunder:

    def __init__(self, color, mileage):
        self.color = color
        self.mileage = mileage

    def __repr__(self):
        # return 'Car_with_dunder({self.color}, {self.mileage})'.format(self=self)
        return '{self.__class__.__name__}(\'{self.color}\', {self.mileage})'.format(self=self) 

    def __str__(self):
        return 'a {self.color} car'.format(self=self)


# good way
new_car = Car_with_dunder('blue',12345)
print(new_car)
print(repr(new_car))


print(str(new_car))
print(str([new_car, new_car, new_car]))