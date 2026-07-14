from gpiozero import Button
from time import sleep

sensor = Button(26)

while True:
    if sensor.is_pressed:
        print("Button is pressed")
    else:
        print("Button is not pressed")
    sleep(0.1)