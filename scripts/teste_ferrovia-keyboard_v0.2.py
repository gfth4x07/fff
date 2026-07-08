comandos = '''#  Controle pelo teclado
#  L Vai
#  K Volta
#  TODO: Cima e baixo controlar a velocidade (PWM?)
#
#  Q Ativa o segmento de traz
#  W Ativa o segmento do meio
#  E Ativa o segmento da curva
#  R Ativa o segmento da direita
#
#  A Ativa o desvio do fundo
#  S Ativa o desvio da frente
#
#
#  Espaço para sair'''

import keyboard
from time import sleep
from gpiozero import Device, LED, Servo


try:
    from gpiozero.pins.pigpio import PiGPIOFactory
    _factory = PiGPIOFactory()
    ON_PI = True
except ImportError:
    from gpiozero.pins.mock import MockFactory, MockPWMPin
    _factory = MockFactory(pin_class=MockPWMPin)
    ON_PI = False

# Define factory global ANTES de criar qualquer device
Device.pin_factory = _factory
servoFactory = _factory

def __main__():
    print(f"Rodando em: {'Raspberry Pi' if ON_PI else 'PC (modo mock)'}")
    print(comandos)

    Segmento1 = Segmento('Q',4)
    Segmento2 = Segmento('W',17)
    Segmento3 = Segmento('E',27)
    Segmento4 = Segmento('R',22)
    
    Desvio1 = Desvio('A', 13, 0, -0.7,)
    Desvio2 = Desvio_led('S', 19, 0, -0.8, 1, 2, 3)
      #def __init__(self, key, servo_pin, angle_on, angle_off, led_r, led_g,led_b):
    while True: 
        #Andar é prioridade entre mudar segmento e desvios
        if  keyboard.is_pressed('l'):
            #Go Right
            print('Direita')
            while keyboard.is_pressed('l'):
                sleep(0.01)
            print("Soltou")
        elif keyboard.is_pressed('k'):
            #Go Left
            print('Esquerda')
            while keyboard.is_pressed('k'):
                sleep(0.01)
            print("Soltou")
            
        # Se não estiver andando: liga os segmentos ou troca desvios
        else:
            Segmento1.verificar()
            Segmento2.verificar()
            Segmento3.verificar()
            Segmento4.verificar()
            Desvio1.verificar()
            Desvio2.verificar()
            
            
        if  keyboard.is_pressed('space'):
            #Exits
            print('exit')
            Segmento1.off()
            Segmento2.off()
            Segmento3.off()
            Segmento4.off()
            #Desligar ou voltar pra posição original
            break





class Segmento:
    def __init__(self, key, pin):
        self.key = key
        self.state = True
        self.led = LED(pin)
        self.led.on()

    def on(self):
        self.led.on()
        self.state = True

    def off(self):
        self.led.off()
        self.state = False


    def verificar(self):
        if  keyboard.is_pressed(self.key):
            self.state = not self.state
            self.led.toggle()
            print(self.key, 'on' if self.state else 'off')
            while keyboard.is_pressed(self.key):
                sleep(0.01)


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


class Desvio:
    def __init__(self, key, servo_pin, angle_on, angle_off):
        self.key = key
        self.state = False
        self.value_off = float(angle_off)
        self.value_on = float(angle_on)
        self.servo = Servo(servo_pin, pin_factory=servoFactory)
        self.servo.value = self.value_off
        
    def on(self):
        self.state = True
        self.servo.value = self.value_on
        
    def off(self):
        self.state = False
        self.servo.value = self.value_off
        
    
    def toggle(self):  #Testar
        self.off() if self.state else self.on()
            
    def verificar(self):
        if  keyboard.is_pressed(self.key):
            self.toggle()
            while keyboard.is_pressed(self.key):
                sleep(0.01)
            print(self.key, 'on' if self.state else 'off')

    def calibrar(self):
        pass  # TODO: mudar os valores de on e off


class Desvio_led(Desvio, Led_rgb):
    def __init__(self, key, servo_pin, angle_on, angle_off, led_r, led_g, led_b):
        Led_rgb.__init__(self, led_r, led_g, led_b)
        Desvio.__init__(self, key, servo_pin, angle_on, angle_off)
    
    def on(self):
        Desvio.on(self)
        Led_rgb.green(self)
    
    def off(self):
       Desvio.off(self)
       Led_rgb.red(self)

        


'''
def setup():

    global bg, b1, b2, b3, b4, s1, s2, L, R

    b1 = Botao_toggle(115, 5, 60, 60, "1", 4)
    b2 = Botao_toggle(10, 120, 60, 60, "2", 17)
    b3 = Botao_toggle(37, 252, 60, 60, "3", 27)
    b4 = Botao_toggle(460, 93, 60, 60, "4", 22)

    s1 = Botao_toggle_servo(410, 133, 40, 40, "s1", 13, 0, -0.7)
    s2 = Botao_toggle_servo(520, 50, 40, 40, "s2", 19, 0, -0.8)

    L = Botao_push(520, 325, 60, 60, "←", 3)
    R = Botao_push(590, 325, 60, 60, "→", 2)

    b1.on()
    b2.on()
    b3.on()
    b4.on()


def draw():
    background(255)
    shape(bg, 0, 0)
    b1.display()
    b2.display()
    b3.display()
    b4.display()
    L.display()
    R.display()
    s1.display()
    s2.display()

    if is_key_pressed:
        if key_code == LEFT:
            L.on()
            L.pressed = True
        elif key_code == RIGHT:
            R.on()
            R.pressed = True
        else:
            if key == "1":
                b1.off() if b1.state else b1.on()
            elif key == "2":
                b2.off() if b2.state else b2.on()
            elif key == "3":
                b3.off() if b3.state else b3.on()
            elif key == "4":
                b4.off() if b4.state else b4.on()
            elif key in {"z", "Z"}:
                s1.off() if s1.state else s1.on()
            elif key in {"x", "X"}:
                s2.off() if s2.state else s2.on()
            sleep(0.4)


def mouse_pressed():
    pass


def key_released():
    L.off()
    L.pressed = False
    R.off()
    R.pressed = False


class Botao_push():
    def __init__(self, x, y, w, h, t, pin):
        self.x, self.y = x, y
        self.w, self.h = w, h
        self.t = t
        self.pressed = False
        self.led = LED(pin)
        self.led.off()

    def on(self):
        self.led.on()

    def off(self):
        self.led.off()

    def mouse_over(self):
        return (self.x < mouse_x < self.x + self.w and
                self.y < mouse_y < self.y + self.h)

    def display(self):
        mouse_over = self.mouse_over()
        if mouse_over and is_mouse_pressed:
            fill(140)
        elif mouse_over:
            fill(205)
        else:
            fill(255)
        rect_mode(CORNER)
        rect(self.x, self.y, self.w, self.h, 5)
        fill(0)
        text_align(CENTER, CENTER)
        text(self.t, self.x + self.w / 2, self.y + self.h / 2)

        if mouse_over and self.pressed and not is_mouse_pressed:
            self.pressed = False
            self.off()
            return True
        elif mouse_over and is_mouse_pressed or self.pressed:
            self.pressed = True
            self.on()
        else:
            self.pressed = False
            self.off()

        return False


class Botao_toggle():
    def __init__(self, x, y, w, h, t, pin):
        self.x, self.y = x, y
        self.w, self.h = w, h
        self.t = t
        self.pressed = False
        self.state = False
        self.led = LED(pin)
        self.led.off()

    def on(self):
        self.led.on()
        self.state = True

    def off(self):
        self.led.off()
        self.state = False

    def mouse_over(self):
        return (self.x < mouse_x < self.x + self.w and
                self.y < mouse_y < self.y + self.h)

    def display(self):
        mouse_over = self.mouse_over()
        if mouse_over:
            fill((not self.state) * 185, self.state * 185, 0)
        else:
            fill((not self.state) * 255, self.state * 255, 0)
        rect_mode(CORNER)
        rect(self.x, self.y, self.w, self.h, 5)
        fill(0)
        text_align(CENTER, CENTER)
        text(self.t, self.x + self.w / 2, self.y + self.h / 2)

        if mouse_over and self.pressed and not is_mouse_pressed:
            self.pressed = False
            self.state = not self.state
            self.led.toggle()
            return True

        if mouse_over and is_mouse_pressed:
            self.pressed = True
        else:
            self.pressed = False

        return False


class Botao_toggle_servo():
    def __init__(self, x, y, w, h, t, pin, off, on):
        self.x, self.y = x, y
        self.w, self.h = w, h
        self.t = t
        self.pressed = False
        self.state = False
        self.value_off = float(off)
        self.value_on = float(on)
        self.servo = Servo(pin, pin_factory=servoFactory)
        self.off()

    def on(self):
        self.servo.value = self.value_on
        self.state = True

    def off(self):
        self.servo.value = self.value_off
        self.state = False

    def mouse_over(self):
        return (self.x - self.w / 2 < mouse_x < self.x + self.w / 2 and
                self.y - self.h / 2 < mouse_y < self.y + self.h / 2)

    def display(self):
        mouse_over = self.mouse_over()
        if mouse_over:
            fill(self.state * 185, self.state * 185, (not self.state) * 185)
        else:
            fill(self.state * 200 + 55, self.state * 200 + 55, (not self.state) * 255)
        ellipse(self.x, self.y, self.w, self.h)
        fill(0)
        text_align(CENTER, CENTER)
        text(self.t, self.x, self.y)

        if mouse_over and self.pressed and not is_mouse_pressed:
            self.pressed = False
            if self.state:
                self.on()
            else:
                self.off()
            self.state = not self.state
            return True

        if mouse_over and is_mouse_pressed:
            self.pressed = True
        else:
            self.pressed = False

        return False
'''
__main__()