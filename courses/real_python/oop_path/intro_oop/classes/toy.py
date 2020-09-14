from classes.brand import Brand

class Toy:

    sound = False
    inbox = True

    def __init__(self, name: str, color: str, brand: Brand, price: int, size: float):
        self.name = name
        self.color = color
        self.price = price
        self.brand = brand
        self.size = size # meters

    def walk(self):
        return '{} is walking.'.format(self.name)

    def action(self):
        return '{} is scratching.'.format(self.name)


class ToyWithSound(Toy):

    sound = True
    battery = False

    def speech_button(self):
        if self.sound and self.battery:
            return 'Hi! My name is {}, I want to play with you. I really love to play.'.format(self.name)
        else:
            return 'you have to buy batteries kid.'

    def action(self):
        return '{} is punching.'.format(self.name)