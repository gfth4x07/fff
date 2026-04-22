from gpiozero import Servo
from gpiozero.pins.pigpio import PiGPIOFactory
myFactory = PiGPIOFactory()

inp = ''
servo = Servo(19, pin_factory = myFactory)  # Servo conectado no pino 19

while True:
    inp = input("Digite o angulo: ")
    inp = int(inp)
    servo.value = inp
