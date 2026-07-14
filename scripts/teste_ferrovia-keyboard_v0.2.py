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
#  Z Ativa o trem ir e depois voltar (TODO)
#
#  Espaço para sair'''

import keyboard
from time import sleep
from gpiozero import Device, LED, Servo, Button


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

    Trem1 = Trem(3,2)

    Segmento1 = Segmento('q',4)
    Segmento2 = Segmento('w',27)
    Segmento3 = Segmento('e',17)
    Segmento4 = Segmento('r',22)

    Desvio1 = Desvio('a', 13, 0, -0.75,)
    Desvio2 = Desvio_led('s', 19, 0, -0.9, 16, 20, 21)
    
    Sensor1 = Button(5, pull_up = None, active_state = True)
    Sensor2 = Button(6, pull_up = None, active_state = True)
    
    modo_automatico = False
    
   
    while True: 

        Trem1.verificar()
        Segmento1.verificar()
        Segmento2.verificar()
        Segmento3.verificar()
        Segmento4.verificar()
        Desvio1.verificar()
        Desvio2.verificar()
        
        if  keyboard.is_pressed('z'):  # Faz o trem ir do Sensor 1 ao Sensor2
            modo_automatico = True
            print("Automode on: z")
            
            if Sensor1.is_pressed and not Sensor2.is_pressed:
                # TODO: Também fazer a checagem dos desvios.
                print("Trem em posição")
                Trem1.go_right()
                Sensor2.wait_for_press()
                Trem1.stop()
                print("Chegou ao destino")
            else:
                print("Trem fora de posição")
                
            while keyboard.is_pressed('z'):
                sleep(0.01)
            modo_automatico = False
            print("Automode off: z")
        
        if  keyboard.is_pressed('space'):
            #Exits
            print('exit')
            Segmento1.off()
            Segmento2.off()
            Segmento3.off()
            Segmento4.off()
            #Desligar ou voltar pra posição original
            break

class Trem:
    def __init__(self, pin_l, pin_r):
        self.left = LED(pin_l)
        self.right = LED(pin_r)
        self.left.off()
        self.right.off()

    def go_right(self):
        self.left.off()
        self.right.on()

    def go_left(self):
        self.right.off()
        self.left.on()

    def stop(self):
        self.left.off()
        self.right.off()

    def verificar(self):
        if  keyboard.is_pressed('l'):
            self.go_right()
            print('Direita')
            while keyboard.is_pressed('l'):
                sleep(0.01)
            print("Soltou")
            self.stop()
        elif keyboard.is_pressed('k'):
            self.go_left()
            print('Esquerda')
            while keyboard.is_pressed('k'):
                sleep(0.01)
            print("Soltou")
            self.stop()


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
        self.red()
    
    def on(self):
        Desvio.on(self)
        Led_rgb.green(self)
    
    def off(self):
       Desvio.off(self)
       Led_rgb.red(self)


__main__()