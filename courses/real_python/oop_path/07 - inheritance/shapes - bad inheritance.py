'''
Notes:
    * This is an example for bad inheritance
    * We use Inheritance if:
        - Relation ship is only one way
            Example: 
                A Rectangle can be a Square with diferents sites
                A Square can be a Rectangle with same sites

        - Methods on Interfaces must be diferents
            resize method must be rewrite by square because,
            it has only one size
'''
class Rectangle:
    def __init__(self, length, height):
        self._length = length
        self._height = height

    @property
    def area(self):
        return self._length * self._height

    def resize(self, new_length, new_height):
        self._length = new_length
        self._height = new_height
    

class Square(Rectangle):
    def __init__(self, side_size):
        super().__init__(side_size,side_size)


rectangle = Rectangle(2,4)
assert rectangle.area == 8

square = Square(2)
assert square.area == 4


rectangle.resize(3,5)
assert rectangle.area == 15

square.resize(3,5)
print(f'Square area: {square.area}') # this is not okay, we must to rewrite resize method

print('OK :)')