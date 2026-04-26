from gpiozero import Servo
from gpiozero.pins.pigpio import PiGPIOFactory
from time import sleep

myFactory = PiGPIOFactory()

inp = ''
servo = Servo(19, pin_factory = myFactory)  # Servo conectado no pino 19

while True:
    inp = input("Digite o angulo: ")
    if inp == "girar":
        n = 0
        while True:
            n += 0.01
            servo.value = n%2-1
            sleep(0.1)
    inp = float(inp)/10
    servo.value = inp
