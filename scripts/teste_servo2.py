from gpiozero import Servo
from gpiozero.pins.pigpio import PiGPIOFactory
from time import sleep

myFactory = PiGPIOFactory()

inp = ''
servo1 = Servo(19, pin_factory = myFactory)  # Servo conectado no pino 19
servo2 = Servo(13, pin_factory = myFactory)
i = 1

while True:
    i = i%2
    print("Servo",i,end=" ")
    inp = input("Digite o angulo: ")
    inp = float(inp)/10
    if i:
        print(1)
        servo1.value = inp
    else:
        print(2)
        servo2.value = inp
    i += 1
