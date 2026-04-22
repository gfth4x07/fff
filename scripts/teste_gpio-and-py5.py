from gpiozero import LED
from time import sleep

led = LED(15)

def setup():
    size(200,200)
    background(124)

def draw():
    if is_mouse_pressed:
        background(0,255,0)
        led.on()
    else:
        background(255,0,0)
        led.off()