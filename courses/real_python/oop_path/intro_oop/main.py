from classes.brand import Brand
from classes.toy import Toy


mattel = Brand("Mattel","This a great toys brand")
spiderman = Toy("Spiderman", "Red", mattel, 123456, 1.56)

print("***********************************************************************************")
print("***************************** TOY DESCRIPTION *************************************")
print("***********************************************************************************")
print(f'This is the toy you are buying {spiderman.name}')
print(f'This is the toy brand {spiderman.brand.name}')
print(f'This is the toy brand description {spiderman.brand.description}')
print(f'This is the toy price {spiderman.price}')
print(f'This is the toy size {spiderman.size}')


print(spiderman.speech_button())

spiderman.inbox = False
spiderman.battery = True

print(spiderman.speech_button())

