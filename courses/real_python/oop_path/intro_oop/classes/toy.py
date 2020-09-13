from classes.brand import Brand

class Toy:

    sound = True
    inbox = True
    battery = False

    def __init__(self, name: str, color: str, brand: Brand, price: int, size: float):
        self.name = name
        self.color = color
        self.price = price
        self.brand = brand
        self.size = size # meters

    def speech_button(self):
        if self.sound and self.battery:
            return 'Hi! My name is {}, I want to play with you. I really love to play.'.format(self.name)
        else:
            return 'you have to buy batteries kid.'
