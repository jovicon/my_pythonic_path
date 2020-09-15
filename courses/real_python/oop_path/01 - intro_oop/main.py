from classes.brand import Brand
from classes.toy import Toy, ToyWithSound

mattel = Brand("Mattel","This a great toys brand")
wolverine = Toy("wolverine", "Yellow", mattel, 123456, 1.56)
spiderman = ToyWithSound("Spiderman", "Red", mattel, 123456, 1.56)

print("***************************************************************************************")
print("***************************** TOY DESCRIPTION - 1 *************************************")
print("***************************************************************************************")
print(f'This is the toy you are buying {spiderman.name}')
print(f'This is the toy brand {spiderman.brand.name}')
print(f'This is the toy brand description {spiderman.brand.description}')
print(f'This is the toy price {spiderman.price}')
print(f'This is the toy size {spiderman.size}')
print(f'This is the toy size {spiderman.action()}')

print("***************************************************************************************")
print("***************************** TOY DESCRIPTION - 1 *************************************")
print("***************************************************************************************")
print(f'This is the toy you are buying {wolverine.name}')
print(f'This is the toy brand {wolverine.brand.name}')
print(f'This is the toy brand description {wolverine.brand.description}')
print(f'This is the toy price {wolverine.price}')
print(f'This is the toy size {wolverine.size}')
print(f'This is the toy size {wolverine.action()}')

print(spiderman.speech_button())

spiderman.inbox = False
spiderman.battery = True

print(spiderman.speech_button())

