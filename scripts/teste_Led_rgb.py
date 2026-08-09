from gpiozero import LED

class Led_rgb:
    def __init__(self, led_r, led_g, led_b):
        self.led_r = LED(led_r)
        self.led_g = LED(led_g)
        self.led_b = LED(led_b)
        self.led_r.off()
        self.led_g.off()
        self.led_b.off()

    def red(self):
        self.led_r.on()
        self.led_g.off()
        self.led_b.off()

    def green(self):
        self.led_r.off()
        self.led_g.on()
        self.led_b.off()

r = input("Digite o pino red: ")
g = input("Digite o pino green: ")
b = input("Digite o pino blue: ")

led = Led_rgb(int(r),int(g),int(b))