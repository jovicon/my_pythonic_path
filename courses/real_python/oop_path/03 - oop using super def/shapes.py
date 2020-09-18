class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * self.length + 2 * self.width

    def what_am_i(self):
        return 'Rectangle'

# without super() and Inheritance
# class Square:
#     def __init__(self, length)
#         self.length = length

#     def area(self):
#         return 4 * self.length

#     def perimeter(self):
#         return 4 * self.length




class Square(Rectangle):
    def __init__(self, length):
        super().__init__(length,length)

    def what_am_i(self):
        return 'Square'



class Cube(Square):
    # same parameters as Square, no need to redefine __ini__

    def surface_area(self):
        face_area = self.area()
        return face_area * 6

    def volume(self):
        face_area = super().area()
        return face_area * self.length

    def what_am_i(self):
        return 'Cube'

    def family_tree(self):
        # super() is a shortcut for super(Cube, self)
        return self.what_am_i() + ' child of ' + super().what_am_i()

